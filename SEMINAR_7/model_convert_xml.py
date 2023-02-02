phone_book = []
def create_xml():
    with open ('phone_book.txt','r',encoding = 'utf-8') as stream:
        phone_book_raw = stream.readlines()
        # print(phone_book_raw)
        for record in phone_book_raw:
            record_l = record.removesuffix('\n')
            phone_book.append(record_l)
        print(phone_book)
        size = len(phone_book)
        print(size)
    with open ('xml_book.xml','w',encoding = 'utf-8') as stream:
        stream.write('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE phone_book>\n<phone_book>\n<list = "Список записей">\n')
        for i in range(1, size + 1):
            stream.write(f'<record_{i}>{phone_book[i - 1]}</record_{i}>\n')
        stream.write('</list>\n</phone_book>')

# create_xml()

