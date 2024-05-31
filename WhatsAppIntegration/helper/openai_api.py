import os


from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

#client = OpenAI()
client = OpenAI(api_key='')
model_name = "ft:gpt-3.5-turbo-0613:personal::9CB4CCRl"


def text_complition(prompt: str) -> dict:
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "system", "content": "You are a mental healthcare professional and an expert in mental health that helps people with their mental health welfare."},
                      {"role": "user", "content": prompt}]
        )
        #print(response.choices[0].message.content)
        return response.choices[0].message.content

    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
        