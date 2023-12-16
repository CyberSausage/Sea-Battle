import sqlite3
import datetime
connection = sqlite3.connect("Морской_бой_DB.db")
cursor = connection.cursor()

l_s = {0: "| ▢ ", 1: "| ■ ", -1: "| ▨ ", 2: "| ▣ ", 3: "| ▩ ", 4: "№ǁА ǁ Б ǁ В ǁ Г ǁ Д ǁ Е ǁ Ж ǁ З ǁ Иǁ К ǁ\n"}
flot_example = {1: 4, 2: 3, 3: 2, 4: 1}

def filling_place(k_list, idTG):
    str_pole = ""
    cursor.execute(f'''select my_table from Play where id_tg="{idTG}"''')
    list_pole = str(cursor.fetchone()[0]).replace("[", "").replace("]", "").replace(" ", "").split("|")
    list_pole.remove("")
    for i in range(0, len(list_pole)):
        list_pole[i] = list_pole[i].split(",")
        for l in range(0, len(list_pole[i])):
            list_pole[i][l] = int(list_pole[i][l].replace("'", ""))

    if (k_list[0] == k_list[2]):
        for i in range(k_list[1]-1, k_list[3]):
            list_pole[k_list[0]-1][i] = 1
    else:
        for i in range(k_list[0]-1, k_list[2]):
            list_pole[i][int(k_list[1])-1] = 1

    for i in list_pole:
        str_pole += f"{str(i)}|"
    cursor.execute(f'''Update Play set my_table="{str_pole}" where id_tg="{idTG}"''')
    connection.commit()

def back_filling_place(k_list, idTG):
    str_pole = ""
    cursor.execute(f'''select my_table from Play where id_tg="{idTG}"''')
    list_pole = str(cursor.fetchone()[0]).replace("[", "").replace("]", "").replace(" ", "").split("|")
    list_pole.remove("")
    for i in range(0, len(list_pole)):
        list_pole[i] = list_pole[i].split(",")
        for l in range(0, len(list_pole[i])):
            list_pole[i][l] = int(list_pole[i][l].replace("'", ""))

    if (k_list[0] == k_list[2]):
        for i in range(k_list[1]-1, k_list[3]):
            list_pole[k_list[0]-1][i] = 0
    else:
        for i in range(k_list[0]-1, k_list[2]):
            list_pole[i][int(k_list[1])-1] = 0

    for i in list_pole:
        str_pole += f"{str(i)}|"
    cursor.execute(f'''Update Play set my_table="{str_pole}" where id_tg="{idTG}"''')
    connection.commit()

def get_new_place(idTG):
    cursor.execute(f'''select my_table from Play where id_tg="{idTG}"''')
    list_place = str(cursor.fetchone()[0]).replace("[", "").replace("]", "").replace(" ", "").split("|")
    list_place.remove("")
    for i in range(0, len(list_place)):
        list_place[i] = list_place[i].split(",")
        for l in range(0, len(list_place[i])):
            list_place[i][l] = int(list_place[i][l].replace("'", ""))
    return list_place

def save_message_id(idTG, message_id):
    cursor.execute(f'''Update Play set id_message="{message_id[0]}" where id_tg="{idTG[0]}"''')
    cursor.execute(f'''Update Play set id_message="{message_id[1]}" where id_tg="{idTG[1]}"''')
    connection.commit()

def get_message_id(idTG):
    cursor.execute(f'''select id_message from Play where id_tg="{idTG}"''')
    message_id = cursor.fetchone()[0]
    return message_id

def get_can_enter(idTG):
    cursor.execute(f'''select can_enter from Play where id_tg="{idTG}"''')
    can = bool(cursor.fetchone()[0])
    return can

def update_can_enter(idTG):
    cursor.execute(f'''update Play set can_enter="False" where id_tg="{idTG}"''')
    connection.commit()

def get_can_fire(idTG):
    cursor.execute(f'''select can_fire from Play where id_tg="{idTG}"''')
    can = bool(cursor.fetchone()[0])
    return can

def update_can_fire(idTG):
    cursor.execute(f'''Update Play set can_fire="True" where id_tg="{idTG}"''')
    connection.commit()

def get_my_flot(idTG):
    cursor.execute(f'''select my_flot from Play where id_tg="{idTG}"''')
    flot = cursor.fetchone()[0]
    return flot

def update_my_flot(idTG, new_inf, slogaim):
    cursor.execute(f'''select my_flot from Play where id_tg="{idTG}"''')
    new_my_flot = str(cursor.fetchone()[0])
    new_znach = int(new_my_flot[new_my_flot.index(str(new_inf))+3]) + slogaim
    end = new_my_flot[:new_my_flot.index(str(new_inf))+3] + str(new_znach) + new_my_flot[new_my_flot.index(str(new_inf))+4:]
    cursor.execute(f'''update Play set my_flot="{end}" where id_tg="{idTG}"''')
    connection.commit()

def get_place_opponents(idTG):
    cursor.execute(f'''select id_vs from Players where id_tg="{idTG}"''')
    id_opponent = cursor.fetchone()[0]
    cursor.execute(f'''select my_table from Play where id_tg="{id_opponent}"''')
    list_place = cursor.fetchone()[0].replace("[", "").replace("]", "").split("|")
    for i in range(0, len(list_place)):
        list_place[i] = list_place[i].split(",")
    return list_place

def get_false_opponent_table(idTG):
    cursor.execute(f'''select opponent_table from Play where ig_tg="{idTG}"''')
    list_plase_F = cursor.fetchone().replace("[", "").replace("]", "").split("|")
    for i in range(0, len(list_plase_F)):
        list_plase_F[i] = list_plase_F[i].split(",")
    return list_plase_F

def fire(idTG, list_kord):
    list_place_true = get_place_opponents(idTG)
    list_palse_false = get_false_opponent_table(idTG)
    if (list_place_true[list_kord[0]][list_kord[1]] == 1 or list_place_true[list_kord[0]][list_kord[1]] == 2):
        list_palse_false[list_kord[0]][list_kord[1]] = list_place_true[list_kord[0]][list_kord[1]] = 2

    elif (list_place_true[list_kord[0]][list_kord[1]] == 0 and list_place_true[list_kord[0]][list_kord[1]] == -1):
        list_palse_false[list_kord[0]][list_kord[1]] = list_place_true[list_kord[0]][list_kord[1]] = -1

    elif (list_place_true[list_kord[0]][list_kord[1]] == 3):
        list_palse_false[list_kord[0]][list_kord[1]] = list_place_true[list_kord[0]][list_kord[1]] = 3

