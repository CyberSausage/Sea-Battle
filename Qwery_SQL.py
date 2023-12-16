import sqlite3
import datetime
connection = sqlite3.connect("Морской_бой_DB.db")
cursor = connection.cursor()

def create_tables():
    cursor.execute('''create table Players
            (id integer primary key AUTOINCREMENT,
            id_tg text,
            user_name text,
            name text,
            online bool,
            id_vs text,
            time text,
            win integer,
            lose integer)''')

def create_table():
    cursor.execute('''create table Play
            (id integer primary key AUTOINCREMENT,
            id_tg text,
            my_table text,
            id_message text,
            can_enter bool,
            can_fire bool,
            opponent_table text,
            my_flot text)''')

def registr(idTG, username, name):
    cursor.execute(f'''select id_tg from Players where id_tg={idTG}''')
    idTG_new = cursor.fetchone()
    print(idTG_new)
    if (idTG_new != None):
        return
    name_replace = str(name).replace("'", "").replace('"', "")
    print(name_replace)
    time = datetime.datetime.now()
    cursor.execute(f'''insert into Players (id_tg, user_name, name, online, time, win, lose) values ({idTG}, '{username}', "{str(name_replace).replace('None', '')}", 'False', "{str(time)}", 0, 0)''')
    cursor.execute(f'''insert into Play (id_tg, id_message, can_enter, can_fire) values ({idTG}, "123", "True", "False")''')
    connection.commit()

def select_stata(idTG):
    cursor.execute(f'''select win, lose from Players where id_tg={idTG}''')
    stat = cursor.fetchone()
    return stat

def search_opponents():
    cursor.execute(f'''select id_tg, user_name, name from Players where online=1''')
    list_opponents = cursor.fetchone()
    print(list_opponents)
    return list_opponents


def set_Online(idTG):
    cursor.execute(f'''update Players set online=True where id_tg={idTG}''')
    connection.commit()

def search_player(key):
    key = str(key).replace("https://t.me/", "@")
    if (str(key).find("@") != -1):
        key = str(key).replace("@", "")
        cursor.execute(f'''select id_tg from Players where user_name="{key}"''')
        idTG = cursor.fetchone()
    else:
        key = key.replace('"', "").replace("'", "")
        cursor.execute(f'''select id_tg from Players where name="{key}"''')
        idTG = cursor.fetchone()
    return idTG[0]

def update_opponents(id_vs, username):
    cursor.execute(f'''update Players set id_vs={id_vs} where user_name="{username}"''')
    cursor.execute(f'''select id_tg from Players where user_name="{username}"''')
    id1 = cursor.fetchone()[0]
    cursor.execute(f'''update Players set id_vs={id1} where id_tg={id_vs}''')
    connection.commit()
    return id1

def select_id_otprav(username):
    cursor.execute(f'''select id_tg from Players where user_name="{username}"''')
    id_otprav =cursor.fetchone()[0]
    return id_otprav

def save_pole(pole_list, idTG):
    str_pole = ""
    for i in pole_list:
        str_pole += f"{str(i)}|"
    cursor.execute(f'''Update Play set my_table="{str_pole}" where id_tg="{idTG}"''')
    cursor.execute(f'''update Play set opponent_table="{str_pole}" where id_tg="{idTG}"''')
    cursor.execute('''update Play set my_flot="1: 0, 2: 0, 3: 0, 4: 0"''')
    connection.commit()