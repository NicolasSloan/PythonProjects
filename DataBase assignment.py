import sqlite3

#creating the database
conn = sqlite3.connect('assignment.db')

#creating the table and colums of data within the database
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_demo( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_demo TEXT \
        )")
    conn.commit()




fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


#initializing an empty list to store the .txt files
txtFiles = []

#loop to iterate though each item in fileList and put each .txt file into the db
for txt in fileList:
    if txt.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_demo(col_demo) VALUES (?)", \
                        (txt,))
            conn.commit()

        txtFiles.append(txt) #adding just the txt files to their own list

conn.close()

print(txtFiles)



                        





