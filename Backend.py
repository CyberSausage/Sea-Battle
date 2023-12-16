
l_s = {0: "| ▢ ", 1: "| ■ ", -1: "| ▨ ", 2: "| ▣ ", 3: "| ▩ ", 4: "№ǁА ǁ Б ǁ В ǁ Г ǁ Д ǁ Е ǁ Ж ǁ З ǁ Иǁ К ǁ\n"}
l_s_c = {0: "| ▢ ", 1: "| ■ ", -1: "| ▨ ", 2: "| ▣ ", 3: "| ▩ ", 4: "№ǁА ǁ Б ǁ В ǁ Г ǁ Д ǁ Е ǁ Ж ǁ З ǁ Иǁ К ǁ\n"}
example = f"1  {l_s[0] * 10}|"

def draw(list_place):
    strk = f"{l_s[4]}"
    for i in range(0, len(list_place)):
        if (i != 9):
            strk += f"{i+1}  "
        else:
            strk += "10"
        for l in range(0, len(list_place)):
            strk += l_s[int(list_place[l][i])]
        strk += "|\n"

    return strk

def view(list_place, list_koords):
    count = 0
    if (list_koords[0] == 1):
        if (list_koords[1] == 1):
            for i in range(list_koords[1]-1, list_koords[3]+1):
                for l in range(list_koords[0]-1, list_koords[2]+1):
                    if (list_place[l][i] == 0):
                        pass
                    else:
                        return False
            return True
        elif (list_koords[3] == 10):
            for i in range(list_koords[1]-2, list_koords[3]):
                for l in range(list_koords[0]-1, list_koords[2]+1):
                    if (list_place[l][i] == 0):
                        pass
                    else:
                        return False
            return True
        else:
            for i in range(list_koords[1]-2, list_koords[3]+1):
                for l in range(list_koords[0]-1, list_koords[2]+1):
                    if (list_place[l][i] == 0):
                        pass
                    else:
                        return False
            return True
    else:
        count += 1

    if (list_koords[2] == 10):
        if (list_koords[1] == 1 or list_koords[3] == 1):
            for i in range(list_koords[1]-1, list_koords[3]+1):
                for l in range(list_koords[0]-2, list_koords[2]):
                    if (list_place[l][i] == 0):
                        pass
                    else:
                        return False
            return True
        elif (list_koords[1] == 10 or list_koords[3] == 10):
            for i in range(list_koords[1]-2, list_koords[3]):
                for l in range(list_koords[0]-2, list_koords[2]):
                    if (list_place[l][i] == 0):
                        pass
                    else:
                        return False
            return True
        else:
            for i in range(list_koords[1]-2, list_koords[3]+1):
                for l in range(list_koords[0]-2, list_koords[2]):
                    if (list_place[l][i] == 0):
                        pass
                    else:
                        return False
            return True
    else:
        count += 1

    if (list_koords[1] == 1):
        for i in range(list_koords[0]-2, list_koords[2]+1):
            for l in range(list_koords[1]-1, list_koords[3]+1):
                if (list_place[i][l] == 0):
                    pass
                else:
                    return False
        return True
    else:
        count += 1

    if (list_koords[3] == 10):
        for i in range(list_koords[0]-2, list_koords[2]+1):
            for l in range(list_koords[1]-2, list_koords[3]):
                if (list_place[i][l] == 0):
                    pass
                else:
                    return False
        return True
    else:
        count += 1

    if (count == 4):
        for i in range(list_koords[0]-2, list_koords[2]+1):
            for l in range(list_koords[1]-2, list_koords[3]+1):
                if (list_place[i][l] == 0):
                    pass
                else:
                    return False
        return True
    return True

def view_revers(list_place, list_koords):
    for i in range(list_koords[0]-1, list_koords[2]):
        for l in range(list_koords[1]-1, list_koords[3]):
            if (list_place[i][l] == 1):
                pass
            else:
                return False
    for i in range(list_koords[0]-2, list_koords[2]+1):
        for l in range(list_koords[1]-2, list_koords[3]+1):
            try:
                if i >= 0 and l >= 0:
                    if (list_place[i][l] == 0 and ((i < (list_koords[0]-1) or i > (list_koords[2]-1)) or (l < (list_koords[1]-1) or l > (list_koords[3]-1)))):
                        pass
                    elif (list_place[i][l] == 1 and ((i >= (list_koords[0]-1) and i <= (list_koords[2]-1)) and (l >= (list_koords[1]-1) and l <= (list_koords[3]-1)))):
                        pass
                    else:
                        return False
            except:
                pass
    return True