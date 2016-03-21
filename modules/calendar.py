#-*- encoding: utf-8 -*-
"""
Calendar Modul with threading
Autor: Matthias Kittler
"""
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

from tkinter import *
import threading
import logging
#import time
import datetime


from inc.modul import modul

class calendar(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container
        self.window = window
        self.config = config

        try:

            ##############
            # init section

            self.addWidget("headline", Label(self.window, fg=self.config.get("calendar","main_color"), font=self.config.get("calendar","main_font"), bg='black'))
            self.addWidget("calendar", Label(self.window, fg=self.config.get("calendar","color"), font=self.config.get("calendar", "font"), bg='black', justify='left'))

            self.posWidget("headline", xPos, yPos, anc)
            self.posWidget("calendar", xPos, yPos+25, anc)

            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):

        while 1: #infinite loop from thread - on exit, thread dies
            try:

                ##############
                # code section

                """Gets valid user credentials from storage.

                If nothing has been stored, or if the stored credentials are invalid,
                the OAuth2 flow is completed to obtain the new credentials.

                Returns:
                    Credentials, the obtained credential.
                """
                self.txtWidget("headline", "Aktuelle Termine:")

                home_dir = os.path.expanduser('~')
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

                eventsResult = service.events().list(
                    calendarId='primary', timeMin=now, maxResults=self.config.getint("calendar", "max_events"), singleEvents=True,
                    orderBy='startTime').execute()
                events = eventsResult.get('items', [])

                self.calendar_text = ""
                if not events:
                    self.calendar_text = " Keine Einträge gefunden "
                for event in events:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    day = start[8:10]
                    month = start[5:7]
                    year = start[0:4]
                    hour = start[11:13]
                    minute = start[14:16]
                    dauer = start[20:22] + ":" + start[23:25]

                    self.calendar_text += day + "." + month + "." + year
                    if hour != "":
                         self.calendar_text += " um " + hour + ":" + minute + " Uhr (" + dauer + "h)"
                    else:
                        self.calendar_text += "\t\t"
                    self.calendar_text += "\t" +  event['summary'] + "\n"

                self.txtWidget("calendar", self.calendar_text)


                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                self.wait(self.config.getfloat("calendar","update_interval"))
