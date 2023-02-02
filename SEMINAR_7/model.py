
phone_book = []
def read_file_phone_book():
    with open ('phone_book.txt','r',encoding = 'utf-8') as stream:
        phone_book_raw = stream.readlines()
        # print(phone_book_raw)
    for record in phone_book_raw:
        record_l = record.removesuffix('\n')
        # print(record_l)
        record_t = tuple(record_l.split(', '))
        phone_book.append(record_t)
    # print(phone_book)
        
def finde_name_r():
    phone_num = input('Введите номер телефона для поиска ')
    count = 0
    for el in phone_book:
        if el[1] == phone_num:
            print(f'Найдена запись: {el[0]} {el[1]}')
            count +=1
    if count == 0:
        print('Ничего не найдено')

def finde_phone_r():
    name = input('Введите имя и фамилию для поиска ')
    count = 0
    for el in phone_book:
        if el[0] == name:
            print(f'Найдена запись: {el[0]} {el[1]}')
            count +=1
    if count == 0:
        print('Ничего не найдено')

def delete_record_r():
    del_name = input('Введите имя и фамилию для удаления ')
    size = len(phone_book)
    print(size)
    for i in range(0, size):
        if phone_book[i][0] == del_name:
            del phone_book[i]
    
def write_to_file():
    new_record = input('Введите новую запись в формате "Имя Фамилия, Телефон" ')
    print(new_record)
    with open ('phone_book.txt','a',encoding = 'utf-8') as stream:
        stream.write(f'{new_record}\n')

def write_to_phone_book():
    new_record = input('Введите новую запись в формате: Имя Фамилия, Телефон ')
    new_record_t = tuple(new_record.split(', '))
    phone_book.append(new_record_t)

def write_phone_book_to_file():
    size = len(phone_book)
    print(size)
    with open ('phone_book.txt','w',encoding = 'utf-8') as stream:
        for i in range(0, size):
            stream.write(f'{phone_book[i][0]}, {phone_book[i][1]}\n')


def print_phone_book():
    with open ('phone_book.txt','r',encoding = 'utf-8') as stream:
        phone_book_raw = stream.readlines()
        # print(phone_book_raw)
    for record in phone_book_raw:
        record_l = record.removesuffix('\n')
        print(record_l)

def finde_name():
    read_file_phone_book()
    finde_name_r()

def finde_phone():
    read_file_phone_book()
    finde_phone_r()

def delete_record():
    read_file_phone_book()
    delete_record_r()
    write_phone_book_to_file()


