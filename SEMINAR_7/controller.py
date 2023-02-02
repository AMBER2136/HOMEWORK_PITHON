import view
import model_menu
    
def select_article():
    view.input_menu_artickle()
    article = int(input())
    print(article)
    model_menu.select(article)
    

def start():
    view.show_menu()
    select_article()
   


