import sqlite3
verbindung = sqlite3.connect("/home/f.ulmer/PycharmProjects/pythonProject8/datenbank/geburtstage.db")
zeiger = verbindung.cursor()

beruehmtheiten = [('Georg Wilhelm Friedrich', 'Hegel', '27.08.1770'),
                  ('Johann Christian Friedrich', 'Hölderlin', '20.03.1770'),
                  ('Rudolf Ludwig Carl', 'Virchow', '13.10.1821')]

zeiger.executemany("""
                INSERT INTO personen 
                       VALUES (?,?,?)
                """, beruehmtheiten)
zeiger.execute("SELECT * FROM personen")
inhalt = zeiger.fetchall()
"""da wir nur daten fetchen/holen benötigen wir keine commit() anweisung."""
print(inhalt)
verbindung.close()
