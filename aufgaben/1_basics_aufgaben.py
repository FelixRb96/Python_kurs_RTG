"""
RTG Pythonkurs
@Date: 07.05.2021

Einführung Python Aufgaben
Basics Datentypen, Kontrollstrukturen und Libraries
"""

# Aufgabe 1: 
# 
# a)
# Schreiben Sie eine Funktion "add_values" die die Parameter x1 und x2 erhält. 
# Die Funktion soll "x1 + x2" zurückgeben. 
#
# b) 
# Testen Sie die oben erstellte Funktion mit den Variablen:
x1, x2 = 3, 4
y1, y2 = "Hallo", "RTG"
# Was fällt auf? (Denken sie dabei an die Datentypen der Variblen)
# Schreiben sie ihre Beobacktungen als Kommentar in dieses File.

# Aufgabe 2:
# Es sei die folgende Liste gegeben:
list_for_exercise = [
        2, 
        3.0, 
        ["This", "might", "be", "a", "list", "in", "a", "list"],
        {
            "can_we_put_random_things_in_lists" : "yes",
            "xyz" : [1,2,3]
            }
        ]

# a) Lassen Sie sich per print die Datentypen der Listenelemente ausgeben.
# b) Printen Sie sich aus dem dritten Element von "list_for_exercise" das zweite Element.
# c) Printen sie sich aus dem vierten Element von "list_for_exercise" das Element mit dem key "xyz".

# Aufgabe 3
# a) Importieren Sie die Library "time".
# b) Schreiben Sie sich eine Funktion "get_time()" die keine Parameter übergeben bekommt,
#    die aktuelle Uhrzeit printet und als Rückgabewert ebenfalls die aktuelle Zeit hat. 
#    Finden Sie dazu eine angemessene Funktion in der Library "time" (Tipp: verwenden Sie "help(time)" nachdem 
#    sie die Library geladen haben).
