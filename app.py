from database import db_sales
from modules import main

class App:
    def __init__(self):
        self.user = None
        self.permission = None

    def start(self):
        self.user = main.auth()
        self.permission = db_sales.get_permisson(self.user)

        print(f'\n---Пользователь {self.user}, уровень доступа: {self.permission}---\n')
        
        if self.permission == 1:
            main.sale()
        elif self.permission == 2:
            main.admin()
        else:
            pass



if __name__=="__main__":
    app = App()
    app.start()