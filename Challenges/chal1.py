import sqlite3

values = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))

with sqlite3.connect('challenge.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", values)


connection = sqlite3.connect('challenge.db')
c = connection.cursor()
c.execute("UPDATE Roster SET Species=? WHERE Name=?", ('Human', 'Korben Dallas'))
