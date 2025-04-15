import sqlite3

file_list = (
    "information.docx",
    "Hello.txt",
    "myImage.png",
    "myMovie.mpg",
    "World.txt",
    "data.pdf",
    "myPhoto.jpg",
)


conn = sqlite3.connect("academy.db")

# this block of code creates a table in our database
with conn:
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS tbl_files(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            file_name TEXT\
    )"
    )

    conn.commit()

conn.close()


conn = sqlite3.connect("academy.db")

# this block of code goes through the file_list list and adds all .txt files to the table
for file in file_list:
    if file.endswith(".txt"):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", (file,))
            print(file)
        conn.commit()

conn.close()
