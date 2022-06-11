"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
sum_sold_allpr = 0
for phone in phones:
    sum_sold_pr = sum(phone['items_sold'])
    print(f'Суммарное количество продаж {phone["product"]}: {sum_sold_pr}')
    avg_sold_pr = round(sum(phone['items_sold'])/len(phone['items_sold']), 2)
    print(f'Cреднее количество продаж {phone["product"]}: {avg_sold_pr}')
    sum_sold_allpr += sum_sold_pr
print(f'Суммарное количество продаж всех товаров: {sum_sold_allpr}')
avg_sold_allpr = sum_sold_allpr/len(phones)
print(f'Cреднее количество продаж всех товаров: {avg_sold_allpr}')

