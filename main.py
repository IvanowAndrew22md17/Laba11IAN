x = int(input("введите номер задания:"))

#11.1
def f1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f'Название ресторана: {self.restaurant_name} Тип кухни: {self.cuisine_type}')
        def open_restaurant(self):
            print('Открыто с 12:00')
    newRestaurant = Restaurant(input(), input())
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
    print('\n')
if x == 1:
    f1()

# 11.2
def f2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f'Название ресторана: {self.restaurant_name} Тип кухни: {self.cuisine_type}')
        def open_restaurant(self):
            print('Открыто с 12:00')
    newRestaurant = Restaurant(input(), input())
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
    print('\n')
    Restaurant1 = Restaurant('Kuznyahouse', 'европейская, авторская')
    Restaurant2 = Restaurant('Co-Op Garage', 'европейская, американская, итальянская')
    Restaurant3 = Restaurant('Kiki', 'турецкая, авторская')
    Restaurant1.describe_restaurant()
    Restaurant2.describe_restaurant()
    Restaurant3.describe_restaurant()
    print('\n')
if x==2:
    f2()

#11.3
def f3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, reiting):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.reiting = reiting
        def describe_restaurant(self):
            print(f'Название ресторана: {self.restaurant_name} Тип кухни: {self.cuisine_type}')
        def open_restaurant(self):
            print('Ресторан открыт!')
        def write_reiting(self):
            print(fr'Начальный рейтинг : {self.reiting}')
            self.reiting = input('Новый рейтинг: ')
            print(fr'Обновленный рейтинг: {self.reiting}')
    newRestaurant = Restaurant('Jungle', 'азиатская', '5')
    newRestaurant.write_reiting()
if x==3:
    f3()
if x< 0 or x > 3:
    print("Такой задачи нет(")