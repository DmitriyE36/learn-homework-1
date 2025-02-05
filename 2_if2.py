"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def string_user(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        return 0   
    if s1 == s2:
        return 1
    if len(s1)>len(s2):  
        return 2
    if s2 == 'learn':
        return 3
    return 4

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(string_user(512, 'street'))
    print(string_user('hello', 'hello'))
    print(string_user('good', 'bad'))
    print(string_user('not', 'learn'))
    print (string_user('hot', 'cold'))
    
       
if __name__ == "__main__":
    main()
