import mysql.connector as mysql
db_name = "osborne_bank"

mydb = mysql.connect(
    host="localhost",
    user="root",
    passwd="santoryuu"
)
banKursor = mydb.cursor()
def basic_tasks():
    banKursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    banKursor.execute(f"USE {db_name}")

def show_databases():
    banKursor.execute("SHOW DATABASES")
    for db in banKursor:
        print(db)

def setup_table():
    ine = "INE VARCHAR(255) NOT NULL"
    names0 = "First_Names VARCHAR(255) NOT NULL"
    name1 = "Name VARCHAR(255) NOT NULL"
    phone = "Phone VARCHAR(255) NOT NULL"
    password = "Password VARCHAR(255) NOT NULL"
    pri_key = "PRIMARY KEY(INE)"
    banKursor.execute("CREATE TABLE IF NOT EXISTS clients({}, {}, {}, {}, {}, {})".format(ine, names0, name1, phone, password, pri_key))


def filler(ine, names0, name1, phone, password):
    sqlFormula = "INSERT INTO clients (INE, First_Names, Name, Phone, Password) VALUES (%s, %s, %s, %s, MD5(%s))"
    sqlVals = (ine, names0, name1, phone, password)
    try:
        banKursor.execute(sqlFormula, sqlVals)
    except mysql.Error as err:
        if (err.errno == 1062):
            sqlError = "This account already exists"
            return sqlError

    mydb.commit()

basic_tasks()
setup_table()
filler("sd", "dfb", " vbbbvb", "3453434", "dsfs")