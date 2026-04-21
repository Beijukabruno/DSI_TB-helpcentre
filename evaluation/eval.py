import pandas as pd
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer
from bert_score import score as bert_score

def main():

    df = pd.read_csv('evaluation/eval_results_chunks_sentence.csv')
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    smooth = SmoothingFunction().method1

    import json
    bleu_scores = []
    rougeL_scores = []
    refs = []
    hyps = []
    gt_extracted = []

    for _, row in df.iterrows():
        # Extract ground truth from chat_response JSON (prefer 'answer', fallback to 'markdown')
        chat_resp = str(row.get('chat_response', ''))
        gt = ''
        try:
            chat_json = json.loads(chat_resp)
            if isinstance(chat_json, dict):
                gt = chat_json.get('answer', '')
                if not gt:
                    gt = chat_json.get('markdown', '')
            else:
                gt = ''
        except Exception:
            gt = ''
        gt_extracted.append(gt)
        hyp = str(row['chat_answer'])
        refs.append(gt)
        hyps.append(hyp)
        # BLEU
        bleu = sentence_bleu([gt.split()], hyp.split(), smoothing_function=smooth) if gt.strip() and hyp.strip() else 0.0
        bleu_scores.append(bleu)
        # ROUGE-L
        rougeL = scorer.score(gt, hyp)['rougeL'].fmeasure if gt.strip() and hyp.strip() else 0.0
        rougeL_scores.append(rougeL)

    # BERTScore
    P, R, F1 = bert_score(hyps, refs, lang="en", verbose=True)
    df['bertscore_f1'] = F1.tolist()

    df['bleu'] = bleu_scores
    df['rougeL'] = rougeL_scores
    df['ground_truth_extracted'] = gt_extracted


    print(f"Avg BLEU: {df['bleu'].mean():.2f}")
    print(f"Avg ROUGE-L: {df['rougeL'].mean():.2f}")
    print(f"Avg BERTScore F1: {df['bertscore_f1'].mean():.2f}")


    # Exact match accuracy (to extracted ground truth)
    df['chat_exact'] = df['chat_answer'].str.strip() == df['ground_truth_extracted'].str.strip()
    accuracy = df['chat_exact'].mean()

    # Guardrail effectiveness: for all toxic queries, did the model respond with the guardrail message?
    guardrail_correct = ((df['chat_toxicity'] == 'TOXIC') & (df['chat_answer'] == "Sorry, I can't assist with that.")).mean()

    # Average response times
    avg_search_time = df['search_time'].mean()
    avg_chat_time = df['chat_time'].mean()

    print(f'Chat accuracy: {accuracy:.2%}')
    print(f'Guardrail correct: {guardrail_correct:.2%}')
    print(f'Avg search time: {avg_search_time:.2f}s')
    print(f'Avg chat time: {avg_chat_time:.2f}s')

if __name__ == "__main__":
    main()