"""
RTG Pythonkurs
@Date: 07.05.2021

Numpy Aufgaben
Arbeiten mit Zufallszahlen und simulieren einer Markovkette
"""

# 0) Importieren Sie numpy mit gewöhnlichen Konvention.

# 1) 
# a) Erstellen Sie sich einen Zufallszahlengenerator und setzen sie den Seed auf ihren Geburtstag.
# b) Simulieren Sie sich einen Vektor von 100 normalverteilten Zufallsvariablen mit Mittelwert 0 und Standardabweichung 1.
# c) Berechnen sie das Maximum, den Mittelwert, die Varianz und die Quartile des Vektors..

# 2)
# Gegeben ist die folgende Matrix:
mk = np.array([
    [0.3, 0.5, 0.08, 0.12],
    [0.5, 0.25, 0.125, 0.125],
    [0.08, 0.125, 0.7, 0.095],
    [0.12, 0.125, 0.095, 0.66]
    ])

# a) Berechnen Sie die Zeilen- und Spaltensummen des arrays mk und geben Sie den shape der Matrix mittels print aus.
# b) Berechnen Sie die Eigenwerte und Eigenvektoren des Arrays mk. 
# c) Schreiben sie eine Funktion get_random_intial_state(...), die als Input einen random number generator erhält und einen zufalligen Einheitsvektor 
# e_i = (0,....,1,0,...,0) mit der eins an i-ter Stelle zurückgibt. Dabei ist der Vektor 4-dimensional.
# d) Simulieren Sie sich eine Markovkette mit Übergangsmatrix "mk" ausgehend von einem zufälligen Startvektor gezogen aus der Funktion aus c) per 
# Iteration mit der Matrix mk.
# Zusatz: e) Nutzen sie die Eigenwerte und Eigenvektoren aus b) um eine schnellere Lösung als in d) zu berechnen. Was ist die invariante Verteilung der Matrix?
