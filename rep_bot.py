import requests
import time
import random

WEBHOOK_URL = "Webhook_url_here"

# replace the words in " with custom ones.
words = ["legit", "fast", "trusted", "good trader", "nice guy", "vouch"]

def send_rep():
    random_word = random.choice(words)
    payload = {
        "content": f"+rep {random_word}"
    }
  
    requests.post(WEBHOOK_URL, json=payload)
    print(f"Odesláno: +rep {random_word}")

while True:
    send_rep()
    time.sleep(300)
