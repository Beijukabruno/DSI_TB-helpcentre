import os
from typing import Dict
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # load .env in local/dev, but don't fail at import — validate at call time


def call_gemma_model(prompt: str, model_name: str = 'gemma-3-4b-it') -> Dict:
    """
    Independent function to call Gemma model with any prompt.
    Returns a dictionary with response, llm_model, and llm_model_version.
    """
    api_key = os.getenv("GEMMA_API_KEY")
    if not api_key or api_key == "your_gemma_api_key_here":
        raise ValueError("GEMMA_API_KEY environment variable is not set or is using placeholder value")

    genai.configure(api_key=api_key)

    try:
        model = genai.GenerativeModel(model_name)
    except Exception:
        # some versions of the client expose a different factory; try getattr fallback
        try:
            model = getattr(genai, 'GenerativeModel')(model_name)
        except Exception as e:
            raise RuntimeError(f"Failed to construct Gemma model client: {e}")

    try:
        response = model.generate_content(prompt)

        # Extract a simple model version from model_name if possible
        model_version = model_name.split('-', 1)[-1] if '-' in model_name else "unknown"

        # response may be an object; try to read .text or str(response)
        text = None
        try:
            text = response.text
        except Exception:
            try:
                text = str(response)
            except Exception:
                text = ""

        return {
            "response": text,
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