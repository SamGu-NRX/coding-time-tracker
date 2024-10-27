# src/main.py

import os
import requests
import datetime
import pickle
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

# Configuration
WAKATIME_API_KEY = os.getenv('WAKATIME_API_KEY')
SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_FILE = os.path.join('..', 'credentials', 'credentials.json')
TOKEN_FILE = 'token.pickle'
CALENDAR_ID = os.getenv('CALENDAR_ID', 'primary')
MINUTES_THRESHOLD = int(os.getenv('MINUTES_THRESHOLD', 5))

def authenticate_google_calendar():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    # If no valid credentials, let user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    return service

def fetch_wakatime_activity():
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=1)  # Adjust as needed
    end_date = today
    url = f'https://wakatime.com/api/v1/users/current/summaries?start={start_date}&end={end_date}'
    headers = {'Authorization': f'Bearer {WAKATIME_API_KEY}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Aggregate total coding time in minutes
        total_seconds = sum(day['grand_total']['total_seconds'] for day in data['data'])
        total_minutes = total_seconds / 60
        return total_minutes
    else:
        print(f"Error fetching Wakatime data: {response.status_code}")
        return 0

def update_google_calendar(service, minutes_coded):
    if minutes_coded < MINUTES_THRESHOLD:
        print(f"Active coding time {minutes_coded} minutes is below the threshold.")
        return

    # Create an event for the current time
    now = datetime.datetime.utcnow()
    end_time = now + datetime.timedelta(minutes=minutes_coded)

    event = {
        'summary': 'Coding Session',
        'description': f'Active coding time: {minutes_coded} minutes.',
        'start': {
            'dateTime': now.isoformat() + 'Z',
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time.isoformat() + 'Z',
            'timeZone': 'UTC',
        },
    }

    try:
        event_result = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        print(f"Event created: {event_result.get('htmlLink')}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    service = authenticate_google_calendar()
    minutes_coded = fetch_wakatime_activity()
    update_google_calendar(service, minutes_coded)

if __name__ == '__main__':
    main()
