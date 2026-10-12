import os

from google import genai


def get_llm_client():
    api_key = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)
    return client

def get_llm_content(model_name="gemini-3.5-flash-lite",prompt='', config=None):
    client = get_llm_client()
    llm =client.models.generate_content(
    model=model_name,
    contents=prompt,
    config={**config})
    return llm