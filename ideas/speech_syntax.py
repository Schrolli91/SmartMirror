import re

pattern = "(er|sie) soll (dich|mich|uns) mal anrufen (heute)"
pattern = pattern.replace("(", "(?:") #um keinen eigenen match für die gruppe zu erstellen
pattern = pattern.replace(")", ")?") #gruppe genau kein oder einmal
pattern = pattern.replace(" ", "\s?") #leerzeichen variabel

pattern = "("+ pattern +")"

print(pattern)
 #https://regex101.com/r/gV0dP7/4
