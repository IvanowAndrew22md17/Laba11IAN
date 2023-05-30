x = int(input("введите номер задания:"))

#11.1
def f1():
    class Restaurant:
        def __init__(self, name, k_type):
            self.name = name
            self.k_type = k_type
        def d_restaurant(self):
            print(f'Название ресторана: {self.name} Тип кухни: {self.k_type}')
        def open_restaurant(self):
            print('Открыто с 12:00')
    newRestaurant = Restaurant(input(), input())
    print(newRestaurant.name)
    print(newRestaurant.k_type)
    newRestaurant.d_restaurant()
    newRestaurant.open_restaurant()
    print('\n')
if x == 1:
    f1()

# 11.2
def f2():
    class Restaurant:
        def __init__(self, name, k_type):
            self.name = name
            self.k_type = k_type
        def d_restaurant(self):
            print(f'Название ресторана: {self.name} Тип кухни: {self.k_type}')
        def open_restaurant(self):
            print('Открыто с 12:00')
    newRestaurant = Restaurant(input(), input())
    print(newRestaurant.name)
    print(newRestaurant.k_type)
    newRestaurant.d_restaurant()
    newRestaurant.open_restaurant()
    print('\n')
    Restaurant1 = Restaurant('Kuznyahouse', 'европейская, авторская')
    Restaurant2 = Restaurant('Co-Op Garage', 'европейская, американская, итальянская')
    Restaurant3 = Restaurant('Kiki', 'турецкая, авторская')
    Restaurant1.d_restaurant()
    Restaurant2.d_restaurant()
    Restaurant3.d_restaurant()
    print('\n')
if x==2:
    f2()

#11.3
def f3():
    class Restaurant:
        def __init__(self, name, k_type, reiting):
            self.name = name
            self.k_type = k_type
            self.reiting = reiting
        def d_restaurant(self):
            print(f'Название ресторана: {self.name} Тип кухни: {self.k_type}')
        def open_restaurant(self):
            print('Ресторан открыт!')
        def w_reiting(self):
            print(fr'Начальный рейтинг : {self.reiting}')
            self.reiting = input('Новый рейтинг: ')
            print(fr'Обновленный рейтинг: {self.reiting}')
    newRestaurant = Restaurant('Jungle', 'азиатская', '5')
    newRestaurant.w_reiting()
if x==3:
    f3()
if x< 0 or x > 3:
    print("Такой задачи нет(")