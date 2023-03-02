import mysql.connector


# Connect to the database function
def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="CloudComputing"
    )
    return mydb


def createTables():
    mydb = connect()

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS teams (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), "
                     "founded INT, stadium VARCHAR(255))")

    mycursor.execute("CREATE TABLE IF NOT EXISTS players (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), "
                     "age INT, position VARCHAR(255), shirt_number VARCHAR(255) , team_id INT, FOREIGN KEY (team_id) "
                     "REFERENCES teams(id))")

