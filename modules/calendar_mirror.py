#-*- encoding: utf-8 -*-
"""
Calendar module for MirrorOS
Autor: Matthias Kittler
"""

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from tkinter import *
import datetime
import logging


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'MirrorOS'

class calendar_mirror:
    def __init__(self, window, config, xPos, yPos, anc="n"):
        try:
            logging.debug("generate " + __name__)
            self.window = window
            self.config = config

            self.yStep = 22

            #label for the refresh info
            self.loading = Label(self.window, fg=self.config.get("calendar_mirror","main_color"), font=self.config.get("calendar_miror","font"), bg='black')
            self.loading.place(x=xPos, y=yPos+10*self.yStep, anchor=anc)

            self.headline = Label(self.window, fg=self.config.get("calendar_mirror","color"), font=self.config.get("calendar_mirror","main_font"), bg='black')
            self.headline.place(x=xPos, y=yPos, anchor=anc)

            self.update() #starts his own update routine

        except:
            logging.exception("cannot generate " + __name__)


    def update(self):
        try:
            logging.debug("update " + __name__)

            self.loading.configure(text="Aktualisiere Kalenderdaten ...")
            self.window.update() #redraw window
            self.fetch_data() #reload data from web
            self.loading.configure(text="")

            logging.debug("refresh the widgets")
            #refresh the widgets for events
            self.headline.configure(text=" Einträge im Kalender: "

            self.window.after(self.config.getint("calendar_mirror","update_interval"), self.update)

        except:
            logging.exception("cannot refresh the data")



    def fetch_data(self):
        try:
            logging.debug("load entries")
            #get events

            """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
            home_dir = os.path.expanduser('C:')
            credential_dir = os.path.join(home_dir, '.credentials')
            if not os.path.exists(credential_dir):
                os.makedirs(credential_dir)
            credential_path = os.path.join(credential_dir,
                                           'calendar-python.json')

            store = oauth2client.file.Storage(credential_path)
            credentials = store.get()
            if not credentials or credentials.invalid:
                flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
                flow.user_agent = APPLICATION_NAME
                if flags:
                    credentials = tools.run_flow(flow, store, flags)
                else: # Needed only for compatibility with Python 2.6
                    credentials = tools.run(flow, store)
                print('Storing credentials to ' + credential_path)

            http = credentials.authorize(httplib2.Http())
            service = discovery.build('calendar', 'v3', http=http)

            now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
            print('Getting the upcoming 10 events')
            eventsResult = service.events().list(
                calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
                orderBy='startTime').execute()
            events = eventsResult.get('items', [])

            if not events:
                print('No upcoming events found.')
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])

        except:
            logging.exception("cannot fetch data from web")
