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
                     "REFERENCES teams(id) ON DELETE CASCADE)")


def getTeams():
    mydb = connect()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM teams")

    myresult = mycursor.fetchall()

    return myresult


def getTeamById(id):
    mydb = connect()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM teams WHERE id = " + id)

    myresult = mycursor.fetchone()

    return myresult


def createTeam(name, founded, stadium):
    mydb = connect()

    mycursor = mydb.cursor()

    sql = "INSERT INTO teams (name, founded, stadium) VALUES (%s, %s, %s)"
    val = (name, founded, stadium)
    mycursor.execute(sql, val)

    mydb.commit()

    return mycursor.lastrowid


def updateTeam(id, name, founded, stadium):
    mydb = connect()

    mycursor = mydb.cursor()

    sql = "UPDATE teams SET name = %s, founded = %s, stadium = %s WHERE id = %s"
    val = (name, founded, stadium, id)
    mycursor.execute(sql, val)

    mydb.commit()

    return mycursor.lastrowid


def deleteTeam(id):
    mydb = connect()

    mycursor = mydb.cursor()

    sql = "DELETE FROM teams WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)

    mydb.commit()

    return mycursor.lastrowid


def getPlayers():
    mydb = connect()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM players")

    myresult = mycursor.fetchall()

    return myresult


def getPlayersByTeamId(id):
    mydb = connect()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM players WHERE team_id = " + id)

    myresult = mycursor.fetchall()

    return myresult


def getPlayerById(id):
    mydb = connect()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM players WHERE id = " + id)

    myresult = mycursor.fetchone()

    return myresult


def createPlayer(name, age, position, shirt_number, team_id):
    mydb = connect()

    mycursor = mydb.cursor()

    sql = "INSERT INTO players (name, age, position, shirt_number, team_id) VALUES (%s, %s, %s, %s, %s)"
    val = (name, age, position, shirt_number, team_id)
    mycursor.execute(sql, val)

    mydb.commit()

    return mycursor.lastrowid


def updatePlayer(id, name, age, position, shirt_number, team_id):
    mydb = connect()

    mycursor = mydb.cursor()

    sql = "UPDATE players SET name = %s, age = %s, position = %s, shirt_number = %s, team_id = %s WHERE id = %s"
    val = (name, age, position, shirt_number, team_id, id)
    mycursor.execute(sql, val)

    mydb.commit()

    return mycursor.lastrowid


def deletePlayer(id):
    mydb = connect()

    mycursor = mydb.cursor()

    sql = "DELETE FROM players WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)

    mydb.commit()

    return mycursor.lastrowid