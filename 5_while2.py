"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Привет, не отвлекаю?": "И тебе привет, спрашивай.", 
                        "Как дела?": "Хорошо!", 
                        "Что делаешь?": "Программирую", 
                        "Получается?": "Да, хоть и медленно"}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
        answers_dict = input("Задать вопрос: ")
        if answers_dict == 'Ладно, пока!':
            print('Пока!')
            break
        print(questions_and_answers.get(answers_dict, 'Не скажу'))

        
if __name__ == "__main__":
    ask_user(questions_and_answers)
