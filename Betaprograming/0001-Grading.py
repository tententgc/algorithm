def func():
    a = int(input())
    b = int(input())
    c = int(input())
    total = a+b+c
    if total >= 80:
        print('A')
    elif total >= 75:
        print('B+')
    elif total >= 70:
        print('B')
    elif total >= 65:
        print('C+')
    elif total >= 60:
        print('C')
    elif total >= 55:
        print('D+')
    elif total >= 50:
        print('D')
    else:
        print('F')


func()
