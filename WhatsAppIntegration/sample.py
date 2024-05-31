from openai import OpenAI

client = OpenAI(api_key='')

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, I am having sleep issues!"}
  ]
)
print(response.choices[0].message.content)