#-*- encoding: utf-8 -*-
"""
Calendar Modul with threading
Autor: Matthias Kittler
"""

from tkinter import *
import threading
import logging
import time

class calendar_mirror(threading.Thread):
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
            self.yStep = 22

            ##############
            # init section
            
            self.loading = Label(self.window, fg=self.config.get("calendar_mirror","main_color"), font=self.config.get("calendar_miror","font"), bg='black')
            self.loading.place(x=self.xPos, y=self.yPos+2*self.yStep, anchor=self.anc)

            self.headline = Label(self.window, fg=self.config.get("calendar_mirror","color"), font=self.config.get("calendar_mirror","main_font"), bg='black')
            self.headline.place(x=self.xPos, y=self.yPos, anchor=self.anc)

            self.calendar_text = Label(self.window, fg=self.config.get("calendar_mirror","color"), font=self.config.get("news", "font"), bg='black')
            self.calendar_text.place(x=self.xPos, y=self.yPos+4*self.yStep, anchor=self.anc)
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
                self.calendar_text1 = ""
                if not events:
                    self.calendar_text1 = " Keine Einträge gefunden "
                for event in events:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    self.calendar_text1 = (start, event['summary']) + "\n"

                self.loading.configure(text="Aktualisiere Kalenderdaten ...")
                self.loading.configure(text="")
                self.headline.configure(text=" Einträge im Kalender: ")
                self.calendar_text.configure(text=self.calendar_text1)
                # code section
                ##############

            except:
                logging.exception("cannot update " + __name__)
            finally:
                time.sleep(self.config.getfloat("calendar_mirror","update_intervall"))
