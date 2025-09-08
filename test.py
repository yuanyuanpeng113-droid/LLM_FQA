import openai
from openai import OpenAI
import socket
import time

# Create an OpenAI client with your deepinfra token and endpoint
openai = OpenAI(
    api_key="LL8I5VcS3fxVfXa3XhxQqWBlZo0VG9dJ",
    base_url="https://api.deepinfra.com/v1/openai",
)

chat_completion = openai.chat.completions.create(
    model="microsoft/WizardLM-2-7B",
    messages=[{"role": "user", "content": "Hello"}],
)

print(chat_completion.choices[0].message.content)
