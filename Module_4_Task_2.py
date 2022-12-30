import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="calculator.log")

def minicalculator(x, y, op):    
    if op in ('1', '2', '3', '4'):
        if op == '1':
            log_str = "Додаю ",x," та ",y
            logging.info(log_str)
            print("Результат: %.2f" % (x+y))
        elif op == '2':
            log_str = 'Віднімаю ',x,' та ',y
            logging.info(log_str)
            print("Результат: %.2f" % (x-y))
        elif op == '3':
            log_str = 'Множу ',x,' та ',y
            logging.info(log_str)
            print("Результат: %.2f" % (x*y))
        elif op == '4':
            if y != 0:
                log_str = 'Ділю ',x,' та ',y
                logging.info(log_str)
                print("Результат: %.2f" % (x/y))
            else:
                print("Ділення на нуль!")
                logging.info("Ділення на нуль!")
    else:
        print("Невірний код операції!")

if __name__ == "__main__":
    s = input("Введи дію, використовуючи відповідне число:\n 1 Додавання\n 2 Віднімання\n 3 Множення\n 4 Ділення\n => ")
    x = float(input("Введи компонент 1. "))
    y = float(input("Введи компонент 2. "))        
    minicalculator(x, y, s)
