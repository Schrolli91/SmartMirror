import re


# line = "starte wiki schuhmacher"
# pattern = "((?:starte|beginne){0,1}\s?(?:wikipedia|wiki){1}\s?(?:suche){0,1}\s?(?P<test>.*))"
#
# matchObj = re.match(pattern, line, re.MULTILINE|re.IGNORECASE)
#
# if matchObj:
#    print ("matchObj.group() : ", matchObj.group())
#    print ("matchObj.group(1) : ", matchObj.group(1))
#    print ("matchObj.group(2) : ", matchObj.group("test"))
# else:
#    print ("No match!!")
#
#
#
# exit()

#regex suche
#https://regex101.com/r/gV0dP7/8

#https://www.danielfett.de/de/tutorials/tutorial-regulare-ausdrucke/


checkFor = []

checkFor.append("starte wiki schuhmacher")
checkFor.append("starte wikipedia das ist ein kleiner test")
checkFor.append("starte eine google suche")
checkFor.append("beginne wikipedia suche das ist ein test")
checkFor.append("wikipedia albert einstein")
checkFor.append("hallo test")

pattern = "(starte|beginne) (durchsuche) (wikipedia|wiki)+ (suche) (nach) *suchStr"
#pattern = "# in (wiki|wikipedia)+ suchen"

pattern = pattern.replace("(", "(?:") #um keinen eigenen match für die gruppe zu erstellen
pattern = re.sub("(\)(?=\s|$))", "){0,1}", pattern) #gruppe kann, muss aber nicht
pattern = pattern.replace(")+", "){1}") #gruppe muss
pattern = re.sub("(?:\*(\w*))", "(?P<\g<1>>.*)", pattern) #variablen bereich mit namen
pattern = pattern.replace(" ", "\s?") #leerzeichen variabel



pattern = "^("+ pattern +")$"




#pattern = "((?:starte|beginne){0,1}\s?(\w*)\s?(?:wikipedia|wiki){1}\s?(?:suche){0,1}\s?(.*))"
print(pattern)
print()

p = re.compile(pattern)


for checker in checkFor:

    match = re.search(pattern, checker, re.MULTILINE|re.IGNORECASE)
    if match:
        print("sayed:  " + match.group(0))
        print("found: " + match.group("suchStr"))
        print()
    else:
        print("no match for: " + checker)
        print()
