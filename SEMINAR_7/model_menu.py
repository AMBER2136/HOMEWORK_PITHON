import view
import controller
import model
import model_convert_html
import model_convert_xml


def select(a):
    if a == 1:
        model.write_to_file()  
    elif a == 2:
            model.finde_phone()
    elif a == 3:
        model.finde_name()
    elif a == 4:
        model.print_phone_book()
    elif a == 5:
        model.delete_record()        
    elif a == 6:
        model_convert_xml.create_xml()
    elif a == 7:
        model_convert_html.create_html()
    


