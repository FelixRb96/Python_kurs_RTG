#Importieren der Packages
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#Erstellen  eines Pandas Dataframe aus der marvel_data Liste.
marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]

marvel_df = pd.DataFrame(marvel_data)

marvel_df

#Bennenen der Spalte durch die gegebene Liste.
col_names = ['name', 'sex', 'first_appearance']

marvel_df.columns = col_names

marvel_df

#Verwenden der Spalte name als Index.
marvel_df.index = marvel_df['name']
marvel_df

#Löschen der Spalte name.

marvel_df.drop('name',axis=1, inplace=True)
marvel_df

#Löschen der Zeilen von Namor und Hank Pym.
marvel_df.drop(['Namor', 'Hank Pym'], inplace=True)
marvel_df

#Anzeigen der ersten 5 Zeilen des DataFrames.
marvel_df.head()

#Anzeigen der ersten und letzten Zeile des DataFrames.
marvel_df.iloc[[0,-1]]

#Hinzufügen einer Spalte mit der Anzahl der Jahre seit der Veröffentlichung.
marvel_df['years_since'] = 2021 - marvel_df['first_appearance']
marvel_df

#Ändern der Ersterscheinung von Vision auf das Jahr 1964.
marvel_df.loc['Vision','first_appearance'] = 1964

#Alle weiblichen Superheldinnen.
marvel_df[marvel_df['sex'] == 'female']

#Durschnitt der Ersterscheinungen.
marvel_df['first_appearance'].mean()

#Plotten der Werte der Ersterscheinungen
marvel_df['first_appearance'].plot()
plt.show()

# Histogramm der Ersterscheinungen
marvel_df['first_appearance'].value_counts().plot.bar()
plt.show()

#Einlesen eines Datensatzes
stocks = pd.read_csv("C:/Users/Till/Documents/GitHub/Python_kurs_RTG/Datensatz/aac_shelter_cat_outcome_eng.csv.zip")