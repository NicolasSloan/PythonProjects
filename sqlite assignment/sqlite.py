import sqlite3
connection = sqlite3.connect("C:/Users/sonic/OneDrive/Documents/GitHub/PythonProjects/sqlite assignment/test_database.db")
c = connection.cursor()

c.execute('CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)')
