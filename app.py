from database import db_sales
from sales import *
from main import admin, sale

class App:
    def __init__(self):
        self.user = None
        self.permission = None

    def start(self):
        self.user = auth()
        print(self.user)
        self.permission = db_sales.get_permisson(self.user)
        print(f'\n---Пользователь {self.user}, уровень доступа: {self.permission}---\n')
        if self.permission == 1:
            sale()
        elif self.permission == 2:
            admin()
        else:
            pass



if __name__=="__main__":
    app = App()
    app.start()