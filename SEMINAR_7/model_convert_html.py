phone_book = []
def create_html():
    with open ('phone_book.txt','r',encoding = 'utf-8') as stream:
        phone_book_raw = stream.readlines()
        # print(phone_book_raw)
        for record in phone_book_raw:
            record_l = record.removesuffix('\n')
            phone_book.append(record_l)
        print(phone_book)
        size = len(phone_book)
        print(size)
    with open ('html_book.html','w',encoding = 'utf-8') as stream:
        stream.write('<!DOCTYPE html>\n<html lang="en">\n')
        stream.write('<head>\n<meta charset="UTF-8">\n<title>ТЕЛЕФОННАЯ КНИГА</title>\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<link rel="stylesheet" type="text/css">\n</head> ')
        stream.write('<body>\n<h1>ТЕЛЕФОННАЯ КНИГА</h1>\n')
        for i in range(0, size):
            stream.write(f'<p><h2><b><i>{phone_book[i]}</i></b><h2></p>\n') 
        stream.write('<img  style="border: 10px #FF0000 solid;"src="https://bigpicture.ru/wp-content/uploads/2014/06/lolcats01.jpg" align="top" alt="Кот висит"  height="500px" hspace="40px" vspace="15">\n')
        stream.write('</body>\n</html>')
    
# create_html()

        # for i in range(1, size + 1):
        #     stream.write(f'<record_{i}>{phone_book[i - 1]}</record_{i}>\n')
        # stream.write('</phone_book>')