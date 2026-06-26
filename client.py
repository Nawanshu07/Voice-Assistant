from google import genai
from google.genai import types

client = genai.Client(api_key="use your gemini API key")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello",
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful AI assistant named Astra."
    )
)

print(response.text)