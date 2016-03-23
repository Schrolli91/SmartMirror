#-*- encoding: utf-8 -*-
"""
Wikipedia Search Modul
Autor: Bastian Schroll
"""

from tkinter import *
import logging

#for json download
import urllib.request
import json

from inc.modul import modul

class wiki(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container
        self.window = window
        self.config = config

        try:

            ##############
            # init section

            self.__searchString = ""

            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):

        while 1: #infinite loop from thread - on exit, thread dies
            try:

                ##############
                # code section

                self.setStatus("W")
                self.event.wait()
                self.setStatus("R")

                logging.debug("starte wiki: " + self.__searchString)

                self.__searchString = self.__searchString.replace(" ", "+")
                self.wikiLink = "https://de.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro=1&explaintext=1&utf8=1&titles="+self.__searchString
                self.wikiRet = self.fetch_json(self.wikiLink)

                logging.debug(self.wikiRet["query"])



                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                #self.wait(1)
                self.event.clear()

    def startSearch(self, searchString):
        self.__searchString = searchString
        self.event.set()


    def fetch_json(self, link):
        try:
            logging.debug("fetch json from: %s", link)
            #get json weather data from today
            req = urllib.request.urlopen(link)
            encoding = req.headers.get_content_charset()
            logging.debug("fetching data is done")
            return json.loads(req.read().decode(encoding))

        except:
            logging.exception("cannot fetch data from web")
            return False
