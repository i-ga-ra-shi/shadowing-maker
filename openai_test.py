import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "TOEICのリーディング練習問題を200単語程度で作成してください"}
    ]
)

print(response.choices[0].message.content)
