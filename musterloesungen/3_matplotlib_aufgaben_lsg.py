## Aufgabe 1
import matplotlib.pyplot as plt 
import numpy as np
# a) Erstellen Sie einen Scatter Plot zwischen 10 normalverteilten Punkten.
plt.scatter(np.random.randn(10),np.random.randn(10))
plt.show()
# b) Erstellen Sie den Plot der Wurzelfunktion.
x = np.linspace(0,100,1000)
plt.plot(x,np.sqrt(x))


# c) Setzen Sie das x-Limit der Wurzelfunktion auf 0 bis 25 und das y-Limit auf 0 bis 5. Geben Sie zusätzlich den beiden Achsen einen Namen.
x = np.linspace(0,100,1000)
plt.plot(x,np.sqrt(x))
plt.xlim(0,25)
plt.ylim(0,5)
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.show()


## Aufgabe 2

# a) (1 dimensionaler Random Walk) Ihre Aufgabe ist es 4 Irrfahrten in einem Plot darzustellen. Nutzen Sie hierfür die Wahrscheinlichkeiten (0.5, 0.45, 0.55, 0.4) für eine 
#    Realisierung der 1  und die entsprechende Gegenwahrscheinlichkeit für eine Realisierung der -1. Erzeugen Sie für den Plot 10000 Realisierungen. Fügen Sie dem Plot außerdem eine Legende zu, welche die Wahrscheinlichkeiten der einzelnen Irrfahrten beinhält.

# Tipp: Ihr könnt einen Loop erstellen oder einen Numpy Ansatz wählen



w =np.append(0,np.random.choice([-1,1],100))
x= np.append(0,np.random.choice([-1,1],100, p=[0.45,0.55]))
y= np.append(0,np.random.choice([-1,1],100, p=[0.55,0.45]))
z= np.append(0,np.random.choice([-1,1],100, p=[0.4,0.6]))
plt.plot(np.cumsum(w),label ='p=0.5')
plt.plot(np.cumsum(x),label ='p=0.45')
plt.plot(np.cumsum(y),label ='p=0.55')
plt.plot(np.cumsum(z),label ='p=0.4')
plt.legend()
plt.show()

# b) Erstellen Sie eine 2-dimensionale symmetrische Irrfahrt beginnend in 0. Nutzen Sie hierfür 1000 Realisierungen. Geben Sie dem Plot außerdem einen Titel und speichert ihn.

#Intialisiere die Vektoren
x = np.zeros(1000)
y = np.zeros(1000)
  
# Startet ab den ersten Eintrag 
for i in range(1, 1000): 
    #Zieht eine gleichverteilte Zufallszahl aus der Menge [1,2,3,4]
    val = np.random.randint(1,5)
    #Passt die entsprechende Position an
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1
      
  
# Plottet das Ergebnis
plt.title("2 dimensionale symmetrische Irrfahrt") # Dem Plot einen Titel geben
plt.plot(x, y)
plt.savefig("2 dimensionale symmetrische Irrfahrt.png") # Speichern des Ergebnisses 
plt.show()

