from groq import Groq
import os

client = Groq(api_key=os.getenv(""))

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "who is virat kohli"}
    ]
)

print(response.choices[0].message.content)
