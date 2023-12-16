# -*- coding: utf-8 -*-
import traceback

from Token import token
from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from Qwery_SQL import registr, select_stata, search_opponents, set_Online, search_player, update_opponents, select_id_otprav, save_pole
from Kewboard_markap import main_menu, play_menu, back_menu, fire_menu_f, fire_menu_s, spravka_menu, back_place_menu, spravka_gotov_menu, spravka_clear_menu
from Qwery_War import *
from Backend import draw, view, view_revers
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(text=["start", "старт", "Start", "Старт", "Начнём", "начнём", "Регистрация", "рег", "Рег", "регистрация"])
async def doska(message: Message):
    registr(str(message.chat.id), str(message.from_user.username), f"{message.chat.first_name} {message.chat.last_name}")
    await message.answer(text=f"{message.chat.first_name}, вы зарегистрировались.", reply_markup=main_menu)

@dp.message_handler(text=["Меню", "меню", "main", "Main", "Menu", "menu"])
async def doska(message: Message):
    await message.answer(text=f"Меню:", reply_markup=main_menu)

@dp.callback_query_handler(text="Stata")
async def stata(callback: CallbackQuery):
    stat = select_stata(callback.from_user.id)
    # callback.from_user.first_name
    await bot.edit_message_text(text=f"Побед: {stat[0]}\nПоражений: {stat[1]}", chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=back_menu)

@dp.callback_query_handler(text="back_main_menu")
async def Back_menu(callback: CallbackQuery):
    await bot.edit_message_text(text=f"Меню:", chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=main_menu)

@dp.callback_query_handler(text="Search_vs")
async def search_vs(callback: CallbackQuery):
    search_opponents()
    await bot.edit_message_text(text="Оппоненты:", chat_id=callback.message.chat.id, message_id=callback.message.message_id)

@dp.callback_query_handler(text="Set_Online")
async def set_online(callback: CallbackQuery):
    set_Online(callback.from_user.id)
    await bot.send_message(chat_id=callback.message.chat.id, text="Онлайн включен!")

l_s = {0: "| ▢ ", 1: "| ■ ", -1: "| ▨ ", 2: "| ▣ ", 3: "| ▩ ", 4: "№ǁА ǁ Б ǁ В ǁ Г ǁ Д ǁ Е ǁ Ж ǁ З ǁ Иǁ К ǁ\n"}
pole_defolt = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

@dp.callback_query_handler(text="Yes")
async def Play(callback: CallbackQuery):
    first_id = update_opponents(callback.message.chat.id, callback.message.text.split("@")[1])
    save_pole(pole_defolt, callback.message.chat.id)
    save_pole(pole_defolt, first_id)
    await bot.edit_message_text(text="Игра принята.", chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_message(chat_id=first_id, text=f"@{callback.from_user.username} принял(а) игру.")
    message_ = await bot.send_message(chat_id=callback.message.chat.id, text=f"{l_s[4]}1  {l_s[0]*10}|\n2  {l_s[0]*10}|\n3  {l_s[0]*10}|\n4  {l_s[0]*10}|\n5  {l_s[0]*10}|\n6  {l_s[0]*10}|\n7  {l_s[0]*10}|\n8  {l_s[0]*10}|\n9  {l_s[0]*10}|\n10{l_s[0]*10}|", reply_markup=spravka_menu)

    message = await bot.send_message(chat_id=first_id, text=f"{l_s[4]}1  {l_s[0] * 10}|\n2  {l_s[0] * 10}|\n3  {l_s[0] * 10}|\n4  {l_s[0] * 10}|\n5  {l_s[0] * 10}|\n6  {l_s[0] * 10}|\n7  {l_s[0] * 10}|\n8  {l_s[0] * 10}|\n9  {l_s[0] * 10}|\n10{l_s[0] * 10}|", reply_markup=spravka_menu)
    idTG_list = [callback.message.chat.id, first_id]
    mess_id = [message_.message_id, message.message_id]
    save_message_id(idTG_list, mess_id)

@dp.callback_query_handler(text="No")
async def No_Play(callback: CallbackQuery):
    await bot.send_message(chat_id=callback.message.chat.id, text="Игра отклонена.")
    await bot.send_message(chat_id=select_id_otprav(callback.message.text.split("@")[1]), text=f"@{callback.from_user.username} отклонил(а) игру.")

@dp.callback_query_handler(text="sprav")
async def Spravka(callback: CallbackQuery):
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                text="Укажите координаты крайних клеток короблей:\n-сообщение должно начинаться с: +\n-для удаления корабля пропишите: !+\n-если корабль расположен горизонтально, сначала координату левого края, затем правого\n-если корабль расположен вертикально, сначала верхний край, затем нижний.",
                                message_id=callback.message.message_id, reply_markup=back_place_menu)

@dp.callback_query_handler(text="back_sprav")
async def Back_Spravka(callback: CallbackQuery):
    flot_now = str(get_my_flot(callback.from_user.id)).replace(" ", "").split(",")
    if (int(flot_now[0][-1]) == flot_example[1] and int(flot_now[1][-1]) == flot_example[2] and int(flot_now[2][-1]) == flot_example[3] and int(flot_now[3][-1]) == flot_example[4] and get_can_enter(callback.from_user.id)):
        await bot.edit_message_text(chat_id=callback.message.chat.id, text=draw(get_new_place(callback.from_user.id)), message_id=callback.message.message_id, reply_markup=spravka_gotov_menu)
    elif (get_can_enter(callback.from_user.id)):
        await bot.edit_message_text(chat_id=callback.message.chat.id, text=draw(get_new_place(callback.from_user.id)), message_id=callback.message.message_id, reply_markup=spravka_clear_menu)
    else:
        await bot.edit_message_text(chat_id=callback.message.chat.id, text=draw(get_new_place(callback.from_user.id)), message_id=callback.message.message_id, reply_markup=spravka_menu)

@dp.callback_query_handler(text="readu")
async def Ready_Play(callback: CallbackQuery):
    update_can_enter(callback.from_user.id)
    update_can_fire(callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.message.chat.id, text=draw(get_new_place(callback.from_user.id)), message_id=get_message_id(callback.from_user.id), reply_markup=spravka_menu)

@dp.callback_query_handler(text="clear_place")
async def Clear_Place(callback: CallbackQuery):
    save_pole(pole_defolt, callback.message.chat.id)
    await bot.edit_message_text(chat_id=callback.message.chat.id, text=draw(get_new_place(callback.from_user.id)), message_id=get_message_id(callback.from_user.id), reply_markup=spravka_menu)

b_c = {"А": 1, "Б": 2, "В": 3, "Г": 4, "Д": 5, "Е": 6, "Ж": 7, "З": 8, "И": 9, "К": 10}
flot_example = {1: 4, 2: 3, 3: 2, 4: 1}

@dp.message_handler()
async def habdler(message: Message):
    text_message = message.text
    if (text_message.find("играть с") != -1 or text_message.find("Играть с") != -1):
        id_tg = search_player(text_message.replace("играть с", "").replace("Играть с", "").strip())
        await bot.send_message(chat_id=id_tg, text=f"Принимаете игру от @{message.from_user.username}", reply_markup=play_menu)
        await message.answer(text="Запрос отправлен.")
    if (text_message.find("+") == 0 and text_message.find("!") == -1 and get_can_enter(message.from_user.id)):
        kord1 = text_message.split("-")[0].replace("+", "").replace(" ", "")
        k_list = []
        k_list.append(b_c[str(kord1[0]).upper()])
        k_list.append(int(kord1[1:]))
        kord2 = text_message.split("-")[1].replace(" ", "")
        k_list.append(b_c[str(kord2[0]).upper()])
        k_list.append(int(kord2[1:]))
        if (k_list[0] == k_list[2] or k_list[1] == k_list[3]) and (k_list[2] - k_list[0] <= 3) and (k_list[3] - k_list[1] <= 3) and (view(get_new_place(message.from_user.id), k_list)):
            flot_now = str(get_my_flot(message.from_user.id)).replace(" ", "").split(",")
            long = (k_list[2]-k_list[0]+1)*(k_list[3]-k_list[1]+1)
            if (int(flot_now[long-1][-1]) < flot_example[long]):
                filling_place(k_list, message.from_user.id)
                update_my_flot(message.from_user.id, long, 1)
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                await bot.edit_message_text(chat_id=message.chat.id, text=draw(get_new_place(message.from_user.id)), message_id=get_message_id(message.from_user.id), reply_markup=spravka_menu)
            elif (int(flot_now[0][-1]) == flot_example[1] and int(flot_now[1][-1]) == flot_example[2] and int(flot_now[2][-1]) == flot_example[3] and int(flot_now[3][-1]) == flot_example[4]):
                try:
                    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                    await bot.edit_message_text(chat_id=message.chat.id, text=f"Поле заполнено!😎\n{draw(get_new_place(message.from_user.id))}", message_id=get_message_id(message.from_user.id), reply_markup=spravka_gotov_menu)
                except:
                    pass
            else:
                try:
                    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                    if (get_can_enter(message.from_user.id)):
                        await bot.edit_message_text(chat_id=message.chat.id, text=f"А где разнообразие?😳\n{draw(get_new_place(message.from_user.id))}", message_id=get_message_id(message.from_user.id), reply_markup=spravka_clear_menu)
                except:
                    pass
        else:
            try:
                if (get_can_enter(message.from_user.id)):
                    await bot.edit_message_text(chat_id=message.chat.id, text=f"Неверные координаты!🤬\n{draw(get_new_place(message.from_user.id))}", message_id=get_message_id(message.from_user.id), reply_markup=spravka_clear_menu)
                    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            except:
                pass

    if (text_message.find("!+") == 0 and get_can_enter(message.from_user.id)):
        kord1 = text_message.split("-")[0].replace("!+", "").replace(" ", "")
        k_list = []
        k_list.append(b_c[str(kord1[0]).upper()])
        k_list.append(int(kord1[1:]))
        kord2 = text_message.split("-")[1].replace(" ", "")
        k_list.append(b_c[str(kord2[0]).upper()])
        k_list.append(int(kord2[1:]))
        flot_now = str(get_my_flot(message.from_user.id)).replace(" ", "").split(",")
        long = (k_list[2] - k_list[0] + 1) * (k_list[3] - k_list[1] + 1)
        print(view_revers(get_new_place(message.from_user.id), k_list), k_list)
        if (k_list[0] == k_list[2] or k_list[1] == k_list[3]) and (k_list[2] - k_list[0] <= 3) and (k_list[3] - k_list[1] <= 3) and view_revers(get_new_place(message.from_user.id), k_list):
            update_my_flot(message.from_user.id, long, -1)
            back_filling_place(k_list, message.from_user.id)
            await bot.edit_message_text(chat_id=message.chat.id, text=draw(get_new_place(message.from_user.id)), message_id=get_message_id(message.from_user.id), reply_markup=spravka_clear_menu)
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        else:
            try:
                await bot.edit_message_text(chat_id=message.chat.id, text=f"Неверные координаты!🤬\n{draw(get_new_place(message.from_user.id))}", message_id=get_message_id(message.from_user.id), reply_markup=spravka_clear_menu)
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            except:
                pass

    if (text_message.find("*") == 0 and get_can_fire(message.from_user.id)):
        if (len(text_message) == 3 or (len(text_message) == 4 and text_message[2:] == "10")):
            text_message = text_message.replace("*", "").replace(" ", "")
            k_list = []
            k_list.append(b_c[text_message[0].upper()])
            k_list.append(int(text_message[1:]))
            fire(message.from_user.id, k_list)


#| ▢ | - пустая клетка
# | ▩ | - часть уничтоженного корабля
# | ▣ | - часть раненного корабля
# | ■ | - целая часть корабля
# | ▨ | - обстрелянная клетка
# №ǁА ǁ Б ǁ В ǁ Г ǁ Д ǁ Е ǁ Ж ǁ З ǁ Иǁ К ǁ

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)