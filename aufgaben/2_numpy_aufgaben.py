"""
RTG Pythonkurs
@Date: 07.05.2021

Numpy Aufgaben
Arbeiten mit Zufallszahlen und simulieren einer Markovkette
"""

# 0) importieren sie numpy als die gewöhnliche konvention

# 1) 
# a) erstellen sie sich einen Zufallszahlengenerator und setzen sie einen Seed auf ihren Geburtstag
# b) simulieren sie sich einen Vektor von 100 normalverteilten zufallsvariablen mit mittelwert 0 und standardabweichung 1
# c) berechnen sie das maximum, mittelwert, varianz und die Quartile.

# 2)
# Gegeben ist die folgende Matrix
mk = np.array([
    [0.3, 0.5, 0.08, 0.12],
    [0.5, 0.25, 0.125, 0.125],
    [0.08, 0.125, 0.7, 0.095],
    [0.12, 0.125, 0.095, 0.66]
    ])

# a) berechnen sie die Zeilen- und Spaltensummen des arrays mk und geben sie den shape der matrix mittels print aus
# b) berechnen sie die Eigenwerte und Eigenvektoren des Arrays mk 
# c) schreiben sie eine Funktion get_random_intial_state(...), die als input einen random number generator erhält und einen zufalligen einheitsvektor 
# e_i = (0,....,1,0,...,0) mit der eins an i-ter stelle zurückgibt. Dabei ist der vektor 4-dimensional
# d) Simulieren sie sich eine Markovkette mit Übergangsmatrix "mk" ausgehend von einem zufälligen Startvektor gezogen aus der Funktion aus c) per 
# iteration mit der Matrix mk
# Zusatz: e) Nutzen sie die Eigenwerte und Eigenvektoren aus b) um eine schnellere Lösung als in d) zu berechnen. Was ist die invariante Verteilung der Matrix ?
