import Database


def get_competitions():
    mydb = Database.connect()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM cups")

    myresult = mycursor.fetchall()

    return myresult


def insert_competition(name, start_date, end_date, details, number_of_teams):
    mydb = Database.connect()

    mycursor = mydb.cursor()

    sql = "INSERT INTO cups (name, start_date, end_date, details, number_of_teams, cup_generated) VALUES (%s, %s, %s, "\
          "%s, %s, 0) "

    val = (name, start_date, end_date, details, number_of_teams)

    mycursor.execute(sql, val)

    mydb.commit()

    return mycursor.lastrowid


def get_junctions():
    mydb = Database.connect()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM junction")

    myresult = mycursor.fetchall()

    return myresult


def insert_junction(team_id, cup_id):
    mydb = Database.connect()

    mycursor = mydb.cursor()

    sql = "INSERT INTO junction (team_id, cup_id) VALUES (%s, %s)"

    val = (team_id, cup_id)

    mycursor.execute(sql, val)

    mydb.commit()

    return mycursor.lastrowid


def update_generated_cup(generated, id):
    mydb = Database.connect()

    mycursor = mydb.cursor()

    sql = "UPDATE cups SET cup_generated = %s WHERE id = %s"
    val = (generated, id)
    mycursor.execute(sql, val)

    mydb.commit()

    return mycursor.lastrowid

def get_teams_by_cup_id(id):
    mydb = Database.connect()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM junction WHERE cup_id = " + id)

    myresult = mycursor.fetchall()

    return myresult


def insert_team_in_group(cup_id,team_id):
    mydb = Database.connect()

    mycursor = mydb.cursor()

    sql = "INSERT INTO groups (cup_id, team_id) VALUES (%s, %s)"

    val = (cup_id, team_id)

    mycursor.execute(sql, val)

    mydb.commit()

    return mycursor.lastrowid

def get_groups():
    mydb = Database.connect()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM groups")

    myresult = mycursor.fetchall()

    return myresult