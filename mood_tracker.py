import json
from datetime import datetime
import requests

DATA_FILE = 'data.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def log_mood():
    mood = input("How are you feeling today? (e.g. happy, sad, anxious): ")
    today = datetime.today().strftime('%Y-%m-%d')

    data = load_data()
    data[today] = mood
    save_data(data)

    print(f"Mood for {today} saved!")
    get_quote()

def view_moods():
    data = load_data()
    if not data:
        print("No moods logged yet.")
    else:
        print("\nYour mood log:")
        for date, mood in sorted(data.items()):
            print(f"{date}: {mood}")

def get_quote():
    try:
        response = requests.get('https://zenquotes.io/api/random')
        if response.status_code == 200:
            quote_data = response.json()[0]
            print(f"\n💬 Quote of the Day: \"{quote_data['q']}\" — {quote_data['a']}")
    except Exception:
        print("Couldn't fetch quote today.")

if __name__ == "__main__":
    print("📆 Daily Mood Tracker")
    print("1. Log Mood")
    print("2. View Past Moods")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        log_mood()
    elif choice == '2':
        view_moods()
    else:
        print("Invalid choice.")
