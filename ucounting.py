from random import randint as rt
import time

list_of_titles = []
list_of_prices = []
list_of_quantity = []
    
list_of_1pc_prices = []
    
examples = ['Молоко Коровье', 'Масло маслянное', 'Кошачий корм на 8 лет вперед', 'Коньяк со вкусом  спирта', 'Банановые бананы, одна штука', 'Какао из какао бобов', 'Кофейный нескафэээ', 'Сладкий сахар', 'Соленая соль', 'Суп в супнице']

fuckin = ['wtf', 'втф', 'вот даз зе фокс сээй', 'хз', 'хоре', 'шо', 'неа', 'ага', 'че каво', 'чекак', 'че как', 'чекаво', 'ась', 'нет', 'да', 'fuck', 'sup', 'yo']

def adding():
    ran = rt(0, 9)
    a = input('Введи название товара (например: ' + examples[ran]  + ')\n> ')
    b = input('Введи стоимость\n> ')
    try:
        int(b)
    except ValueError:
        print('Ошибка: введенные данные не относятся к числовому типу')
        exit()
    c = input('Введи количество (в граммах или миллилитрах)\n> ')
    try:
        int(c)
    except ValueError:
        print('Ошибка: введенные данные не относятся к числовому типу')
        exit()
    list_of_titles.append(a)
    list_of_prices.append(int(b))
    list_of_quantity.append(int(c))
        
def ucount():
    list_0 = list_of_prices
    list_1 = list_of_quantity
    
    for elem in list_0:
        elem = list_0.index(elem)
        a = list_0[elem]
        b = list_1[elem]
        c = a / b
        list_of_1pc_prices.append(c)
    b = list_of_1pc_prices.index(min(list_of_1pc_prices))
    print('Я думаю, ' + list_of_titles[b] + ' - твой лучший выбор!')
    print('Это стоит всего ' + str(list_of_1pc_prices[b]) + ' рублей за 1 грамм (миллилитр). Килограмм (или литр) стоит ' + str(list_of_1pc_prices[b] * 1000) + ' рублей.')
    print('Всегда рад помочь!')
        
print('Шалом!')
print('Снова дуплишь в магазе, думая что выгодней? Я помогу!')
print('По очереди вбивай товары, я посчитаю самый выгодный!')
add = 'y'
while add == 'y' or add == 'д':
    adding()
    add = input('Добавить еще один товар? (y/д/n/н)\n> ')
    #joke
    if add == 'meow':
        print('Тебе тут не зоомагазин, и не питомни.. а, это мой кот. Все забываю покормить..')
        time.sleep(2)
        exit()
    elif add == 'usu4lc0d3r':
        print('Мой автор долбанутый. Публикует прогу, которую написал для себя. Совсем уже колпак поехал..')
        time.sleep(2.6)
        exit()
    elif add in fuckin:
        print('Ти глупый или что-то?')
        time.sleep(1.2)
        exit()
    else:
        print('Не, я не знаю такого')
        exit()
ucount()
