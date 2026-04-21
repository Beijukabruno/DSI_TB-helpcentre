# Evaluation Directory

This directory contains resources for evaluating the TB Help Centre system.

## Files
- `test_set.csv`: Test queries, expected files, and expected answers.
- `eval_script.py`: Script to run evaluation against the chatbot and search endpoints, measuring response times and logging results.

## How to Use
1. Add more queries and expected answers to `test_set.csv` as needed.
2. Run the evaluation script:
   
   ```bash
   cd evaluation
   python3 eval_script.py
   ```
3. Review the printed results for accuracy and response time.

You can expand this directory with more scripts, metrics, or analysis notebooks as your evaluation needs grow.
