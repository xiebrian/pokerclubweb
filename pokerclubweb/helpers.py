import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client.client import SignedJwtAssertionCredentials
import json

import datetime
from dateutil import parser

JSON_KEY = json.load(open('pokerclubwebsite.json'))
SCOPE = ['https://www.googleapis.com/auth/calendar.readonly']

CACHE_FILE = './pokerclubweb/cache/upcoming_events.txt'

def get_credentials():
    return SignedJwtAssertionCredentials(JSON_KEY['client_email'], JSON_KEY['private_key'], SCOPE)

def get_google_calendar_events():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """

    events, expired = try_cache()
    if expired:
        try:
            credentials = get_credentials()
            http = credentials.authorize(httplib2.Http())
            service = discovery.build('calendar', 'v3', http=http)

            now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
            print 'Getting the upcoming 10 events on home page'
            # calendarList = service.calendarList().list().execute()
            # for item in calendarList['items']:
            #     print item
            eventsResult = service.events().list(
                calendarId='mitpokerexec@gmail.com', timeMin=now, maxResults=10, singleEvents=True,
                orderBy='startTime').execute()
            events = eventsResult.get('items', [])

            update_cache(events)
        except Exception as e:
            print e
            print 'Getting events failed'
            events = []

    if not events:
        return []
    return [{'time':parser.parse(event['start'].get('dateTime', event['start'].get('date'))), 'summary':event['summary']} for event in events]

def try_cache():
    try:
        with open(CACHE_FILE, 'r') as upcoming_events:
            data = json.load(upcoming_events)
            expired = parser.parse(data['expires']).replace(tzinfo=None) < datetime.datetime.utcnow()
            return data['events'], expired
    except:
        return [], True
def update_cache(events):
    with open(CACHE_FILE, 'w') as upcoming_events:
        data = {
            'expires':(datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat()+'Z',
            'events':events
        }
        json.dump(data,upcoming_events)
