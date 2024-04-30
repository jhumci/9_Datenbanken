# Lädt das Python Paket
import sqlite3
 
# Stell eine Verbindung zu einer Datenbank her, die in der Datei "test.db" gespeichert wird
# Besteht die Datei noch nicht, wird eine leere Datenbankdatei erzeugt
connection = sqlite3.connect('test.db')

# Erstellt einen Cursor, der auf die Datenbank zeigt
cursor = connection.cursor()


#%% Tabelle Experiments
# Löscht Tabelle, sofern diese schon existiert
cursor.execute("""DROP TABLE IF EXISTS Experiments""")
connection.commit()

# Erstellt die Tabelle Experiment
cursor.execute("""  CREATE TABLE Experiments (
                    experimentID INTEGER PRIMARY KEY AUTOINCREMENT,
                    experimenter TEXT,
                    subject TEXT,
                    testname TEXT)"""
               )
connection.commit()

#%% Tabelle Steps
# Löscht Tabelle, sofern diese schon existiert
cursor.execute("""DROP TABLE IF EXISTS Steps""")
connection.commit()

# Erstellt die Tabelle Experiment
cursor.execute("""  CREATE TABLE Steps (
                    stepID INTEGER PRIMARY KEY AUTOINCREMENT,
                    duration_s TEXT,
                    power_W TEXT
                )"""
               )
connection.commit()

#%%

#%% Tabelle StepsInExperiments
# Löscht Tabelle, sofern diese schon existiert
cursor.execute("""DROP TABLE IF EXISTS StepsInExperiments""")
connection.commit()

# Erstellt die Tabelle Experiment
cursor.execute("""  CREATE TABLE StepsInExperiments (
                    StepsInExperimentsID INTEGER PRIMARY KEY AUTOINCREMENT,
                    PositionInExperiment int NOT NULL,
                    stepID int NOT NULL,
                    experimentID int NOT NULL,
                    FOREIGN KEY (stepID) REFERENCES Steps(stepID),
                    FOREIGN KEY (experimentID) REFERENCES Experiments(experimentID)
                )"""
               )
connection.commit()

#%% Fügt Einträge in Tabelle ein

# Einfügen von Daten in Tabelle
add_to_Experiments_table = "INSERT INTO Steps (duration_s, power_W) values (?, ?)"
cursor.execute(add_to_Experiments_table, (60, 100))
connection.commit()
cursor.execute(add_to_Experiments_table, (60, 150))
connection.commit()


# Definition von Variablen
name1 = "Julian"
name2 = "Julian"
test_name = "Test1"

# Einfügen von Daten in Tabelle
add_to_Experiments_table = "INSERT INTO Experiments (experimenter, subject, testname) values (?, ?, ?)"
cursor.execute(add_to_Experiments_table, (name1, name2, test_name))
connection.commit()


# Einfügen von Daten in Tabelle
add_to_Experiments_table = "INSERT INTO StepsInExperiments (PositionInExperiment, experimentID, stepID) values (?, ?, ?)"
cursor.execute(add_to_Experiments_table, (1, 1, 1))
connection.commit()
cursor.execute(add_to_Experiments_table, (2, 1, 2))
connection.commit()

#%% Auslesen der Tabelle
cursor.execute("""   SELECT * FROM Steps""")
connection.commit()
results = cursor.fetchall()
print(results)


#%% Auslesen der Tabelle mit JOIN

# Gibt alle Steps von Experiment 1 aus
cursor.execute("""   SELECT * FROM StepsInExperiments
                    JOIN Steps ON StepsInExperiments.stepID = Steps.stepID
                    WHERE experimentID = 1""")
connection.commit()
results = cursor.fetchall()
print(results)

