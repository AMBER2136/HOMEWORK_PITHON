phone_book = []
with open ('phone_book.txt','r',encoding = 'utf-8') as stream:
    a = stream.readlines()
    print(a)
    a_l = (a[0]).split(', ')
    a_l_1= (a[1]).split(', ')
    a_l_2= (a[2]).split(', ')
    print(a_l)
    print(a_l_1)
    print(a_l_2)
    a_t = tuple(a_l)
    a_t_1 = tuple(a_l_1)
    a_t_2 = tuple(a_l_2)
    print(a_t)
    print(a_t_1)
    print(a_t_2)
    if a_t_2[1] == '(303)712 23 44\n':
        print(a_t_2[0],a_t[1])
    else:
        print('Ничего не найдено')
    phone_book.append(a_t)
    phone_book.append(a_t_1)
    phone_book.append(a_t_2)

    print(phone_book)
    print(phone_book[1][1])
    with open ('phone_book.txt','a',encoding = 'utf-8') as stream:
        stream.write('Петр Федотов, (303)712 23 44')
    



   