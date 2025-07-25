import json
from datetime import datetime

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

if __name__ == "__main__":
    log_mood()
