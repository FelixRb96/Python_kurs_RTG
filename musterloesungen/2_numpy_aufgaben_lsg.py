"""
RTG Pythonkurs
@Date: 07.05.2021

Numpy Aufgaben
Arbeiten mit Zufallszahlen und simulieren einer Markovkette
"""

# 0) Importieren Sie numpy mit gewöhnlichen Konvention.
import numpy as np

# 1) 
# a) Erstellen Sie sich einen Zufallszahlengenerator und setzen sie den Seed auf ihren Geburtstag.
rng = np.random.default_rng(seed = 31071996)

# b) Simulieren Sie sich einen Vektor von 100 normalverteilten Zufallsvariablen mit Mittelwert 0 und Standardabweichung 1.
sim = rng.normal(loc=0, scale=1, size=100)
# c) Berechnen sie das Maximum, den Mittelwert, die Varianz und die Quartile des Vektors..
mean = sim.mean()
var = sim.var()
maximum = sim.max()
quartile_25_perc = np.quantile(sim, 0.25)
quartile_75_perc = np.quantile(sim, 0.75)

# 2)
# Gegeben ist die folgende Matrix:
mk = np.array([
    [0.3, 0.5, 0.08, 0.12],
    [0.5, 0.25, 0.125, 0.125],
    [0.08, 0.125, 0.7, 0.095],
    [0.12, 0.125, 0.095, 0.66]
    ])

# a) Berechnen Sie die Zeilen- und Spaltensummen des arrays mk und geben Sie den shape der Matrix mittels print aus.
colsums = np.sum(mk, axis=0)
rowsums = np.sum(mk, axis=1)

# b) Berechnen Sie die Eigenwerte und Eigenvektoren des Arrays mk. 
A1, eigen, A1T = np.linalg.svd(mk)
print(A1)
print(eigen)

# c) Schreiben sie eine Funktion get_random_intial_state(...), die als Input einen random number generator erhält und einen zufalligen Einheitsvektor 
# e_i = (0,....,1,0,...,0) mit der eins an i-ter Stelle zurückgibt. Dabei ist der Vektor 4-dimensional.
def get_random_initial_state_mk(rng):
    """ returns a random initial state as a 4-dim vector with all entries equal to zero except one entry being equal to one."""
    index = rng.integers(0,4)
    result = np.zeros(4)
    result[index] = 1
    return result

# d) Simulieren Sie sich eine Markovkette mit Übergangsmatrix "mk" ausgehend von einem zufälligen Startvektor gezogen aus der Funktion aus c) per 
# Iteration mit der Matrix mk.
def simulate_markov_chain(n, stoch_matrix, initial_state):
    """ Simulates the probabilities for each state given at discrete time n for a stochastic matrix and a inital state."""
    state = initial_state
    for i in range(n):
        state = mk @ state
    return state

initial_state = get_random_initial_state_mk(rng)
print(simulate_markov_chain(20, mk, initial_state))
# Zusatz: e) Nutzen sie die Eigenwerte und Eigenvektoren aus b) um eine schnellere Lösung als in d) zu berechnen. Was ist die invariante Verteilung der Matrix?
def simulate_markov_chain_alt(n, stoch_matrix, initial_state):
    """ Calculate a faster solution using svd. """
    A1, eigenvals, A1T = np.linalg.svd(stoch_matrix)
    return A1 @ np.diag(eigenvals ** n) @ A1T @ initial_state

print(simulate_markov_chain_alt(20, mk, initial_state))

# Für den interessierten: Eine Zeitmessung
import time 

# simple version
start = time.process_time()
simulate_markov_chain(100, mk, initial_state)
end = time.process_time()

# svd version
start_svd = time.process_time()
simulate_markov_chain_alt(100, mk, initial_state)
end_svd = time.process_time()

# Zweite variante ist etwa doppelt so schnell, kann aber abhängig vom Gerät sein.
print(f"time simple: {end - start}")
print(f"time svd: {end_svd - start_svd}")

