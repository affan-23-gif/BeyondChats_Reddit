import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_persona(posts, comments):
    content_sample = posts[:5] + comments[:5]
    input_text = "\n\n".join(
        [f"{item['type'].capitalize()}: {item.get('title', '')} {item['body']}\nSource: {item['permalink']}" for item in content_sample]
    )

    prompt = f"""
You are an AI language model. Based on the Reddit posts and comments below, generate a structured user persona with attributes like:
- Name or Alias
- Age Range
- Interests
- Writing Style
- Beliefs / Opinions
- Frequently discussed topics
- Personality traits

Cite relevant comments/posts for each point.

Posts and Comments:
{input_text}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    return response.choices[0].message.content
