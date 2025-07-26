import openai

client = openai.OpenAI(api_key="")

response = client.chat.completions.create(
    model="gpt-4.1-nano",  # 👈 Choose model here
    messages=[
        {"role": "system", "content": "You're an XML fixer."},
        {"role": "user", "content": "Fix this, and explain what's wrong with it: <root><a>hi</root>"}
    ]
)

print(response.choices[0].message.content)
