from random import randint as rt

list_of_titles = []
list_of_prices = []
list_of_quantity = []
    
list_of_1pc_prices = []
    
examples = ['Молоко Коровье', 'Масло из сала', 'Кошачий корм на 8 лет вперед', 'Коньяк со вкусом спирта и швейцарской моцареллы', 'Фруктовые бананы, одна штука', 'Какао из соевых бобов', 'Кофейный нескафэээ', 'Сладкий сахар', 'Солёный сахар', 'Суп из баранины с колбасками']
def adding():
    ran = rt(0, 9)
    a = input('Введи название товара (например: ' + examples[ran]  + ')\n> ')
    b = input('Введи стоимость\n> ')
    try:
        int(b)
    except ValueError:
        print('Ошибка: ЧИСЛО!! ВВАДИ ЧИСЛОООООО!!!!1!')
        exit()
    c = input('Введи количество (в граммах или миллилитрах)\n> ')
    try:
        int(c)
    except ValueError:
        print('Ошибка: ЧИСЛО!! ВВАДИ ЧИСЛОООООО!!!!1!')
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
        
print('Снова дуплишь в магазе, думая что выгодней? Я помогу!')
print('По очереди вбивай товары, я посчитаю самый выгодный!')
add = 'y'
while add == 'y' or add == 'д':
    adding()
    add = input('Добавить еще один товар? (y/д/n/н)\n> ')
ucount()
