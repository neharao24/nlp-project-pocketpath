# For the models (GPT-4o & Llama 3 (8B))

import os
from openai import OpenAI
from dotenv import load_dotenv

# Loading the API keys from .env
load_dotenv()

# Setup for llama
llama_client = OpenAI(
    api_key=os.getenv("LLAMA_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


# For smaller llama model
def run_small_model(system_prompt: str, user_query: str) -> str:
    # Sending prompt to llama
    response = llama_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    )
    return response.choices[0].message.content

# For larger llama model
def run_large_model(system_prompt: str, user_query: str) -> str:
    # Sending prompt to llama
    response = llama_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    )
    return response.choices[0].message.content
