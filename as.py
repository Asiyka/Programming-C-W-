number_grn = int(input("Введи суму гривень:"))
number_usd = int(input("Введи суму доларів:"))
suma = (number_grn + number_usd * 25)

if 100 < suma < 200 :
    print(" Йди в McDonalds")
elif 200 < suma < 400 :
    print(" Йди в PizzaCelentano")
elif 400 < suma< 800 :
    print("Йди в ресторан")
elif 800 < suma < 1500:
    print("Йди скупи весь супермаркет")
elif 1500 < suma :
    print("Замов лічного повара")
else:
    print("Вітаю ти банкрот!")

