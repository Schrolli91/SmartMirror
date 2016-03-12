# Copyright by Kampis-Elektroecke
# Modified by Julian R.
# extended by Bastian Schroll & Matthias Kittler

from xml.dom.minidom import *
from tkinter import *
import urllib.request



# Liste fuer den Wetterbericht
# 1. Dimension = heute, 2. Dimension = naechster Tag
# 1. Element = Tag, 2. Element = Datum, 3. = Niedrigste Temperatur, 4. Element = Hoechste Temperatur, 5. Element = Wettersituation

class weather:
    def __init__(self, window, config):
        self.window = window
        self.config = config


        self.startx = self.window.winfo_screenwidth()/2
        self.starty = self. window.winfo_screenheight()/2 - 20
        self.stepy = 22

        self.cloud = PhotoImage(file="Icons/cloudy.gif")
        self.normal = PhotoImage(file="Icons/fair.gif")
        self.fehler = PhotoImage(file="Icons/Fehler.gif")
        self.partlycloudy = PhotoImage(file="Icons/partlycloudy.gif")
        self.fog = PhotoImage(file="Icons/Fog.gif")

        #Ort setzen
        self.ort = Label(self.window, fg=self.config.get("weather","main_color"), font=self.config.get("weather","main_font"), bg='black')
        self.ort.place(x=self.startx, y=self.starty, anchor=N)
        #Text mit heutiges Wetter
        self.wetterheute = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","main_font"), bg='black')
        self.wetterheute.place(x=self.startx, y=self.starty+1*self.stepy, anchor=N)
        #Aktuelle Temperatur darstellen
        self.tempakt = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black')
        self.tempakt.place(x=self.startx, y=self.starty+2*self.stepy, anchor=N)
        #Max. Temerpatur darstellen
        self.tempmax = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black')
        self.tempmax.place(x=self.startx, y=self.starty+3*self.stepy, anchor=N)
        #Min. Temperatur darstellen
        self.tempmin = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black')
        self.tempmin.place(x=self.startx, y=self.starty+4*self.stepy, anchor=N)
        #Wettersituation darstellen
        self.wettersituation = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black')
        self.wettersituation.place(x=self.startx, y=self.starty+5*self.stepy, anchor=N)
        self.wettericon = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black')
        self.wettericon.place(x=self.startx+250, y=self.starty, anchor=N)
        #Wetter am Nächsten Tag
        self.wettermorgen = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","main_font"), bg='black')
        self.wettermorgen.place(x=self.startx, y=self.starty+7*self.stepy, anchor=N)
        #Max. Temperatur am nächsten Tag
        self.tempmaxtag2 = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","main_font"), bg='black')
        self.tempmaxtag2.place(x=self.startx, y=self.starty+8*self.stepy, anchor=N)
        #Min. Temperatur am nächsten Tag
        self.tempmintag2 = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","main_font"), bg='black')
        self.tempmintag2.place(x=self.startx, y=self.starty+9*self.stepy, anchor=N)
        #Wettersituation am nächsten Tag
        self.wettersit2 = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","main_font"), bg='black')
        self.wettersit2.place(x=self.startx, y=self.starty+10*self.stepy, anchor=N)
        #Upadte routine
        self.update()
        
    def update(self):

        self.fetch_data()
        self.ort.configure(text=self.ort1)
        self.wetterheute.configure(text=" Heutiges Wetter")
        self.tempakt.configure(text=self.tempakt1)
        self.tempmax.configure(text=self.tempmax1)
        self.tempmin.configure(text=self.tempmin1)
        self.wettersituation.configure(text=self.wettersituation1)
        self.wettericon.configure(image=self.wettericonauswahl)
        self.wettermorgen.configure(text=" Wetter am naechsten Tag")
        self.tempmaxtag2.configure(text=self.tempmax2)
        self.tempmintag2.configure(text=self.tempmin2)
        self.wettersit2.configure(text=self.wettersituation2)
        self.tempakt.after(self.config.get("weather","update_interval"), self.update)



    def fetch_data(self):

        self.Wetter = [["", "", "", "", ""] , ["", "", "", "", ""]]

    # URL oeffnen und XML Daten einlesen
        self.Baum = urllib.request.urlopen('http://weather.yahooapis.com/forecastrss?w=12837685').read()
    # XML Daten parsen und in Baumstruktur anordnen
        self.Baum = parseString(self.Baum)

    # Ort einlesen
        self.Ort = self.Baum.getElementsByTagName('yweather:location')[0]
        self.Stadt = self.Ort.attributes["city"].value
        self.Land = self.Ort.attributes["country"].value

    # Datum einlesen
        self.Datum = self.Baum.getElementsByTagName('lastBuildDate')[0].firstChild.data

    # Koordinaten auslesen
        self.Geo_Lat = self.Baum.getElementsByTagName('geo:lat')[0].firstChild.data
        self.Geo_Long = self.Baum.getElementsByTagName('geo:long')[0].firstChild.data

    # Wetterdaten von heute einlesen
        self.Today = self.Baum.getElementsByTagName('yweather:condition')[0]

    # Wind einlesen
        self.Wind = self.Baum.getElementsByTagName('yweather:wind')[0]
        self.Richtung = float(self.Wind.attributes["direction"].value)
        self.Speed = float(self.Wind.attributes["speed"].value)
        self.Speed = round((self.Speed*1.609),2)

    # Sonnenaufgang einlesen
        self.Sonne = self.Baum.getElementsByTagName('yweather:astronomy')[0]
        self.Aufgang = self.Sonne.attributes["sunrise"].value
        self.Untergang = self.Sonne.attributes["sunset"].value

    # Wettertext einlesen
        self.Wetterlage = self.Today.attributes["text"].value

    # Temperatur in Fahrenheit einlesen, umrechnen und runden
        self.Temperatur = float(self.Today.attributes["temp"].value)
        self.Temperatur = round((self.Temperatur - 32.0) * (5.0 / 9.0) , 1)

    # Daten in einer Liste speichern
        for Counter in range(2):

    # Wetterdaten fuer die beiden Tage einlesen
    # Daten einlesen
            self.Future = self.Baum.getElementsByTagName('yweather:forecast')[Counter]

    # Daten verarbeiten
            self.Wetter[Counter][0] = self.Future.attributes["day"].value
            self.Wetter[Counter][1] = self.Future.attributes["date"].value
            self.Wetter[Counter][2] = float(self.Future.attributes["low"].value)
            self.Wetter[Counter][3] = float(self.Future.attributes["high"].value)
            self.Wetter[Counter][4] = self.Future.attributes["text"].value
    # Umrechnen der Temperatur in Grad Celsius
            self.Wetter[Counter][2] = round((self.Wetter[Counter][2] - 32.0) * (5.0 / 9.0) , 1)
            self.Wetter[Counter][3] = round((self.Wetter[Counter][3] - 32.0) * (5.0 / 9.0) , 1)
    # Umrechung Windrichtung
        if self.Richtung >= 0:
            self.Windrichtung = "Nord"
        elif self.Richtung >= 45:
            self.Windrichtung = "Nord-Ost"
        elif self.Richtung >= 90:
            self.Windrichtung = "Ost"
        elif self.Richtung >= 135:
            self.Windrichtung = "Sued-Ost"
        elif self.Richtung >= 180:
            self.Windrichtung = "Sued"
        elif self.Richtung >= 225:
            self.Windrichtung = "Sued-West"
        elif self.Richtung >= 270:
            self.Windrichtung = "West"
        elif self.Richtung >= 315:
            self.Windrichtung = "Nord-Ost"
        else:
            self.Windrichtung = "Fehler!"

        self.ort1 = " Wetterbericht für " + self.Stadt + " in " + self.Land
        self.tempakt1 = " Temperatur: " +str(self.Temperatur) + " C Celsius "
        self.tempmax1 = " Max. Temperatur: " + str(self.Wetter[0][3]) + " C Celsius "
        self.tempmin1 = " Min. Temperatur: " + str(self.Wetter[0][2]) + " C Celsius "
        self.tempmax2 = " Max. Temperatur: " + str(self.Wetter[1][3]) + " C Celsius "
        self.tempmin2 = " Min. Temperatur: " + str(self.Wetter[1][2]) + " C Celsius "
        self.wettersituation2 = " Wettersituation: " + self.Wetter[1][4]
        
    #Funktion für Wettersituation

        self.wettersituation1 = " Wettersituation: " + self.Wetterlage
        if self.Wetterlage == "Mostly Cloudy":
            self.wettericonauswahl = self.cloud
        elif self.Wetterlage == "Fair":
            self.wettericonauswahl = self.normal
        elif self.Wetterlage == "Partly Cloudy":
            self.wettericonauswahl = self.partlycloudy
        elif self.Wetterlage == "Fog":
            self.wettericonauswahl = self.fog
        else:
            self.wettericonauswahl = self.fehler
