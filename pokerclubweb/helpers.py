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

def get_credentials():
    return SignedJwtAssertionCredentials(JSON_KEY['client_email'], JSON_KEY['private_key'], SCOPE)

def get_google_calendar_events():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print 'Getting the upcoming 10 events'
    # calendarList = service.calendarList().list().execute()
    # for item in calendarList['items']:
    #     print item
    eventsResult = service.events().list(
        calendarId='mitpokerexec@gmail.com', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        return []
    return [{'time':parser.parse(event['start'].get('dateTime', event['start'].get('date'))), 'summary':event['summary']} for event in events]