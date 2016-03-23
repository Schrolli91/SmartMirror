#-*- encoding: utf-8 -*-
"""
Speech Recognition Modul for MirrorOS
using the Python Libary SpeechRecognition
you must install SpeechRecognition and pyAudio
- pip install SpeechRecognition
- pip install pyaudio
Autor: Bastian Schroll
"""

from tkinter import *
import logging
import speech_recognition as sr

from inc.modul import modul

class speech(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container
        self.window = window
        self.config = config

        try:

            ##############
            # init section

            pass

            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):

        while 1: #infinite loop from thread - on exit, thread dies
            try:

                ##############
                # code section

                r = sr.Recognizer()
                r.dynamic_energy_threshold = True

                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source,0.5)
                    #r.non_speaking_duration = 0.5
                    r.pause_threshold = 1
                    logging.debug("listen for speech")
                    self.setStatus("W")
                    audio = r.listen(source)

                self.setStatus("R")
                # recognize speech using Google Speech Recognition
                try:
                    logging.debug("process spech")
                    self.speech_data = r.recognize_google(audio, show_all=False, language = "de-DE")
                    #self.speech_data = r.recognize_wit(audio, "VER22U4DU7TLIMWUUEAPFDEWLZUDFOAY", show_all=False)
                    self.speech_data = self.speech_data.lower()
                    logging.debug("You said: "+ self.speech_data)

                    modName = {}
                    modName["clock"] = ["uhr", "zeit", "uhrzeit"]
                    modName["date"] = ["datum", "tag"]
                    modName["news"] = ["news", "nachrichten", "meldungen"]
                    modName["weather"] = ["wetter", "vorhersage"]
                    modName["calendar"] = ["termine", "kalender"]
                    modName["welcome"] = ["begrüßung"]

                    #modName["log_view"] = ["log"]
                    modName["status"] = ["status"]

                    onKey = ["anschalten", "anzeigen","zeig", "zeige", "zeigen", "einblenden"]
                    offKey = ["ausschalten", "ausblenden", "verbergen"]

                    sayedModules = []
                    mode = 0


                    if "wiki" in self.speech_data:
                        self.speech_data = self.speech_data.replace("wiki", "").replace("pedia", "").strip()
                        for mod, value in modul.getAllModules().items():
                            if "wiki" in mod:
                                value[0].startSearch(self.speech_data)



                    for name in modName:
                        for n in modName[name]:
                            if n in self.speech_data or "alles" in self.speech_data:
                                logging.debug("found: "+name+" - with: " +n)
                                sayedModules.append(name)
                                break

                    #print(sayedModules)

                    for key in onKey:
                        if key in self.speech_data:
                            logging.debug("found: "+key+" - in onKey")
                            mode = 1
                            break

                    for key in offKey:
                        if key in self.speech_data:
                            logging.debug("found: "+key+" - in offKey")
                            mode = 2
                            break

                    for sayedmod in sayedModules:
                        for mod, value in modul.getAllModules().items():
                            if sayedmod in mod:

                                if mode == 1:
                                    value[0].showAllWidgets()
                                if mode == 2:
                                    value[0].hideAllWidgets()

                                break


                    if self.speech_data == "beenden" or self.speech_data == "ende":
                        self.window.quit()


                except sr.UnknownValueError:
                    logging.debug("Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    logging.error("Could not request results from Speech Recognition service; {0}".format(e))

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                #self.wait(1)
                pass
