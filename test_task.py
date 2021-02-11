import sqlite3
import random
import time
#генерация даты рождения
def date_generation():
    b = False
    year = random.randint(1950, 2020)
    month = random.randint(1, 12)
    if month == 2:
        day = random.randint(1, 28)
    elif year % 4 == 0:
        day = random.randint(1, 29)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = random.randint(1, 31)
    if month == 4 or month == 6 or month == 9 or month == 11:
        day = random.randint(1, 30)
    if month < 10 and day < 10:
        data = '{0}-0{1}-0{2}'.format(year, month, day)
        b = True
    if month < 10:
        data = '{0}-0{1}-{2}'.format(year, month, day)
        b = True
    if day < 10:
        data = '{0}-{1}-0{2}'.format(year, month, day)
        b = True
    if b == False:
        data = '{0}-{1}-{2}'.format(year, month, day)
    return data
# генерация ФИО даты рождения и пола
def generation_data():
    m_names = ['Pavel','Ivan','Bogdan','Ilya','Vladinir','Kirill','Evgeniy','Andrey','Grigorii','Konstantin']
    f_names = ['Inga','Maria','Svetlana','Anna','Alika','Sofia',"Polina",'Paulina','Lybov','Evgenia','Alena','Alexsandar']
    m_sername=['Ignatovich','Pavlov','Peshechonzev','Alekseev','Petrov','Bortich','Paskunov','Firsov','Fun','Fuksovich','Fudiko']
    f_sername = ['Ignatovicha','Pavlova','Peshechonzeva','Alekseeva','Petrova','Bortich','Paskunova','Fasnurova','Fukorova','Fmuk','Frunzova']
    m_otchestvo =[ "Alekseevich",'Anatolievich','Alikovich','Borisovish','Antonovich','Ivanovich','Leonidovich']
    f_otchestvo =['Alekseevna','Anatolievna','Alikovna','Fedorovna','Borisovna','Vitalievna','Leonidovna','Efimovna']
    for i in range(0,500000):
        sername_index = random.randint(0,len(m_sername)-1)
        Familia = m_sername[sername_index]
        name_index = random.randint(0,len(m_names)-1)
        name = m_names[name_index]
        otch_index = random.randint(0,len(m_otchestvo)-1)
        Otchestvo = m_otchestvo[otch_index]
        Date_of_Born = date_generation()
        gender = 'male'
        user = (Familia, name, Otchestvo, Date_of_Born, gender)
        cur.execute("INSERT INTO test2_users VALUES(?, ?, ?, ?, ?);", user)
        conn.commit()
    for i in range(0,500000):
        sername_index = random.randint(0,len(f_sername)-1)
        Familia = f_sername[sername_index]
        name_index = random.randint(0,len(f_names)-1)
        name = f_names[name_index]
        otch_index = random.randint(0,len(f_otchestvo)-1)
        Otchestvo = f_otchestvo[otch_index]
        Date_of_Born = date_generation()
        gender = 'female'
        user = (Familia, name, Otchestvo, Date_of_Born, gender)
        cur.execute("INSERT INTO test2_users VALUES(?, ?, ?, ?, ?);", user)
        conn.commit()
# добавлениеданных в таблицу
def add_data():
    print("Sername:")
    F = str(input())
    print("Name:")
    I = str(input())
    print('Otchestvo:')
    O = str(input())
    print('Data in format by -: year-month-day(for example: 1999-09-01):')
    Date = str(input())
    print('Gender:')
    gender = str(input())
    user = (F,I,O,Date,gender)
    cur.execute("INSERT INTO test2_users VALUES(?, ?, ?, ?, ?);", user)
    conn.commit()
# вывод уникальных данных
def print_unique_data():
    cur.execute("SELECT DISTINCT * FROM test2_users;")
    one_result = cur.fetchall()
    for i in one_result:
        print(i)
# вывод данных где фамилия начинается на F
def print_f_data():
    cur.execute("SELECT * FROM test2_users WHERE Familia LIKE 'F%';")
    one_result = cur.fetchall()
    for i in one_result:
        print(i)


conn = sqlite3.connect('test.db')
cur = conn.cursor()
# создание таблицы
cur.execute("""CREATE TABLE IF NOT EXISTS test2_users(
   Familia TEXT, 
   name_preson TEXT, 
   Otchestvo TEXT,
   Date_of_born DATE ,
   gender TEXT);
""")
conn.commit()
print(" Insert task number:")
i = int(input())
if i == 1:
    print(("Table is created"))
if i == 2:
   print("Add data")
   add_data()
if i == 3:
    print('Unique data')
    print_unique_data()
if i == 4:
    print('Data generation')
    generation_data()
if i == 5:
    print('Select F data')
    start_time = time.time()
    print_f_data()
    print("--- %s seconds ---" % (time.time() - start_time))
