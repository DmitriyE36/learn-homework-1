"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
        user_say = input('Как твои дела? ')
        if user_say == 'Хорошо':
            print('Пока!')
            break
    
if __name__ == "__main__":
    hello_user()
