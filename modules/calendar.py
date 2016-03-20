#-*- encoding: utf-8 -*-
"""
Calendar Modul with threading
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
import threading
import logging
import time
import datetime


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


class calendar(threading.Thread):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        threading.Thread.__init__(self)
        self.name = __name__
        self.daemon = True
        try:
            logging.debug("load " + __name__)

            self.window = window
            self.config = config
            self.xPos = xPos
            self.yPos = yPos
            self.anc = anc

            ##############
            # init section

            self.loading = Label(self.window, fg=self.config.get("calendar","main_color"), font=self.config.get("calendar","font"), bg='black')
            self.loading.place(x=self.xPos, y=self.yPos-50, anchor=self.anc)

            self.headline = Label(self.window, fg=self.config.get("calendar","color"), font=self.config.get("calendar","main_font"), bg='black')
            self.headline.place(x=self.xPos, y=self.yPos-25, anchor=self.anc)

            self.calendar_text = Label(self.window, fg=self.config.get("calendar","color"), font=self.config.get("calendar", "font"), bg='black')
            self.calendar_text.place(x=self.xPos, y=self.yPos, anchor=self.anc)
            # init section
            ##############

        except:
            logging.exception("cannot load " + __name__)


    def run(self):
        logging.debug("run " + __name__)
        while 1: #infinite loop from thread - on exit, thread dies
            try:
                logging.debug("update " + __name__)

                ##############
                # code section

                """Gets valid user credentials from storage.

            If nothing has been stored, or if the stored credentials are invalid,
            the OAuth2 flow is completed to obtain the new credentials.

            Returns:
                Credentials, the obtained credential.
            """
                self.loading.configure(text="Aktualisiere Kalenderdaten ...")
                self.headline.configure(text=" Einträge im Kalender: ")

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
                    calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
                    orderBy='startTime').execute()
                events = eventsResult.get('items', [])

                self.calendar_text1 = ""
                if not events:
                    self.calendar_text1 = " Keine Einträge gefunden "
                for event in events:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    day = start[8:10]
                    month = start[5:7]
                    year = start[0:4]
                    hour = start[11:13]
                    minute = start[14:16]
                    dauer = start[20:22] + ":" + start[23:25]

                    self.calendar_text1 += " Am " + day + "." + month + "." + year + " um " + hour + ":" + minute + " Für: " + dauer + " Stunden " +" - "+ event['summary'] + "\n"
                    
                    


                self.loading.configure(text="")

                self.calendar_text.configure(text=self.calendar_text1)
                # code section
                ##############

            except:
                logging.exception("cannot update " + __name__)
            finally:
                time.sleep(self.config.getfloat("calendar","update_interval"))
