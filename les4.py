a=[]
num=int(input(":"))
for i in range(num):
    z=input(':')
    a.append(int(z))

while True:
    print("1.Введіть всі елементи які меньші за середне ариметичне")
    print("2.Вивести найбільший елемент")
    print("3.Вивести найменьший елемент")
    
    if num<4:
        print('4.Парні')
    else:
        print('4.Поміняти місцями 3 і 4')
        print('5.Парні')
    print('0.Вийти')

    menu=input(':')

    if menu=='1':
        x=sum(a)/num
        for el in a:
            if el<x:
                print(el)
    elif menu=='2':
        max = a[0]
        for el in a:
            if el>max:
                max=el
        print(max)
    elif menu=='3':
        min = a[0]
        for n in a:
            if n < min:
                min = n
            print(min)
    elif menu=='4':
        if num<4:
            print('no')
        else:
            a[2],a[3]=a[3],a[2]
            print(a)
    elif menu=='5':
        for f in a:
            if f%2 == 0:
                print(f)
    elif menu=='0':
        print("Goodbye!")
        break
    else:
        print('?:')

