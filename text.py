from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

base_url = "https://api.aimlapi.com/v1"
api_key = os.getenv("CHAT_KEY")
system_prompt = """I’m Murtaza Zaidi, a backend dev in Python, Flask, and web scraping. Built [project] to [solve problem]. #Backend #Python #Flask #WebScraping"""

user_prompt = "MAKE RESPONSE LIKE {post:your generated output, image_prompt: related image to the post}"

api = OpenAI(api_key=api_key, base_url=base_url)


def main():
    completion = api.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=256,
    )

    response = completion.choices[0].message.content

    print("User:", user_prompt)
    print("AI:", response)


if __name__ == "__main__":
    main()