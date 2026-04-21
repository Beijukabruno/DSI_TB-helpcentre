# call_gemma.py
import os
import genai

def call_gemma_model(prompt: str, model_name: str = 'gemma-3-4b-it') -> dict:
    api_key = os.getenv("GEMMA_API_KEY")
    if not api_key or api_key == "your_gemma_api_key_here":
        raise ValueError("GEMMA_API_KEY environment variable is not set or is using placeholder value")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)
    try:
        response = model.generate_content(prompt)
        model_version = model_name.split('-',1)[-1] if '-' in model_name else "unknown"
        return {
            "response": response.text,
            "llm_model": model_name,
            "llm_model_version": model_version
        }
    except Exception as e:
        error_msg = str(e)
        if "API_KEY_INVALID" in error_msg or "API key not valid" in error_msg:
            raise ValueError(f"Invalid Gemma API key: {error_msg}")
        elif "quota" in error_msg.lower() or "rate limit" in error_msg.lower():
            raise ValueError(f"API quota exceeded or rate limited: {error_msg}")
        else:
            raise Exception(f"Failed to generate model response: {error_msg}")

# Example usage
# response = call_gemma_model(prompt)