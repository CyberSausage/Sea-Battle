from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji

main_menu = InlineKeyboardMarkup()
main_menu.add(InlineKeyboardButton(text="Статистика", callback_data="Stata"),
              InlineKeyboardButton(text="Поиск оппонента", callback_data="Search_vs"),
              InlineKeyboardButton(text="Включить онлайн", callback_data="Set_Online"))

play_menu = InlineKeyboardMarkup()
play_menu.add(InlineKeyboardButton(text="Да", callback_data="Yes"),
              InlineKeyboardButton(text="Нет", callback_data="No"))

back_menu = InlineKeyboardMarkup()
back_menu.add(InlineKeyboardButton(text=f"{emoji.emojize(':fast_reverse_button:')} Назад", callback_data="back_main_menu"))

fire_menu_f = InlineKeyboardMarkup()
(fire_menu_f.add(InlineKeyboardButton(text="А", callback_data="stl"),
              InlineKeyboardButton(text="Б", callback_data="stl"),
              InlineKeyboardButton(text="В", callback_data="stl"),
              InlineKeyboardButton(text="Г", callback_data="stl"),
              InlineKeyboardButton(text="Д", callback_data="stl")
        ).add(InlineKeyboardButton(text="Е", callback_data="stl"),
              InlineKeyboardButton(text="Ё", callback_data="stl"),
              InlineKeyboardButton(text="Ж", callback_data="stl"),
              InlineKeyboardButton(text="З", callback_data="stl"),
              InlineKeyboardButton(text="И", callback_data="stl")))

fire_menu_s = InlineKeyboardMarkup()
fire_menu_s.add(InlineKeyboardButton(text="1", callback_data="str"),
                InlineKeyboardButton(text="2", callback_data="str"),
                InlineKeyboardButton(text="3", callback_data="str"),
                InlineKeyboardButton(text="4", callback_data="str"),
                InlineKeyboardButton(text="5", callback_data="str")
          ).add(InlineKeyboardButton(text="6", callback_data="str"),
                InlineKeyboardButton(text="7", callback_data="str"),
                InlineKeyboardButton(text="8", callback_data="str"),
                InlineKeyboardButton(text="9", callback_data="str"),
                InlineKeyboardButton(text="10", callback_data="str"))

spravka_menu = InlineKeyboardMarkup()
spravka_menu.add(InlineKeyboardButton(text="Справка", callback_data="sprav"))

spravka_clear_menu = InlineKeyboardMarkup()
spravka_clear_menu.add(InlineKeyboardButton(text="Очистить поле", callback_data="clear_place"),
                       InlineKeyboardButton(text="Справка", callback_data="sprav"))

spravka_gotov_menu = InlineKeyboardMarkup()
spravka_gotov_menu.add(InlineKeyboardButton(text="Готов.", callback_data="readu"),
                             InlineKeyboardButton(text="Справка", callback_data="sprav"))

back_place_menu = InlineKeyboardMarkup()
back_place_menu.add(InlineKeyboardButton(text=f"{emoji.emojize(':fast_reverse_button:')} Назад", callback_data="back_sprav"))