import sys
import os
from reddit_scraper import scrape_user_data
from persona_generator import generate_persona

def extract_username(url):
    return url.strip("/").split("/")[-1]

def save_persona(username, persona_text):
    os.makedirs("output", exist_ok=True)
    with open(f"output/{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona_text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <reddit_profile_url>")
        sys.exit(1)

    profile_url = sys.argv[1]
    username = extract_username(profile_url)

    print(f"Scraping data for: {username}")
    posts, comments = scrape_user_data(username)

    print("Generating persona...")
    persona = generate_persona(posts, comments)

    save_persona(username, persona)
    print(f"Persona saved to output/{username}_persona.txt")
