from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s- %(message)s', level=logging.INFO, filename='log.log', encoding='utf-8')


operands_list = []
command = None

def help_command(update: Update, context: CallbackContext):
    logging.info(f'{update.effective_user.first_name} starts bot')
    res_str = ""
    res_str += " --- КАЛЬКУЛЯТОР ---\n"
    res_str += "Выберите действие, затем поочередно введите два числа:\n"
    res_str += "Сложение /sum\n"
    res_str += "Вычитание /sub\n"
    res_str += "Умножение /mul\n"
    res_str += "Деление /div\n"
    res_str += "Комплексное число следует записывать без пробелов. Мнимая единица - j"
    keyboard = ReplyKeyboardMarkup([['/sum', '/sub', '/mul', '/div'], ['1', '2', '3'], ['4', '5', '6'],['7', '8', '9'], ['0'] ], resize_keyboard=True)
    update.message.reply_text(res_str, reply_markup=keyboard)


def check_update(update: Update, context: CallbackContext):
    global operands_list
    if len(operands_list) < 2:
        if update.message.text.isdigit():
            operands_list.append(int(update.message.text))
        elif '+' in update.message.text or '-' in update.message.text:
            operands_list.append(complex(update.message.text))
        else:
            update.message.reply_text("Ошибка. Введённые данные не являются числом.")
    if len(operands_list) == 2:
        if command == 1:
            update.message.reply_text(f"Результат: {sum(operands_list)}")
            logging.info(f'{update.effective_user.first_name}: gets {sum(operands_list)}')
        if command == 2:
            update.message.reply_text(f"Результат: {operands_list[0] - operands_list[1]}")
            logging.info(f'{update.effective_user.first_name}: gets {operands_list[0] - operands_list[1]}')
        if command == 3:
            update.message.reply_text(f"Результат: {operands_list[0] * operands_list[1]}")
            logging.info(f'{update.effective_user.first_name}: gets {operands_list[0] * operands_list[1]}')
        if command == 4:
            update.message.reply_text(f"Результат: {operands_list[0] / operands_list[1]}")
            logging.info(f'{update.effective_user.first_name}: gets {operands_list[0] * operands_list[1]}')

def sum_command(update: Update, context: CallbackContext):
    global operands_list
    global command
    operands_list = []
    command = 1

def sub_command(update: Update, context: CallbackContext):
    global operands_list
    global command
    operands_list = []
    command = 2
    
def mul_command(update: Update, context: CallbackContext):
    global operands_list
    global command
    operands_list = []
    command = 3

def div_command(update: Update, context: CallbackContext):
    global operands_list
    global command
    operands_list = []
    command = 4