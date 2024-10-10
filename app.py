from sales import *

class App:
    def __init__(self):
        self.user = None
        self.permission = None

    def start(self):
        self.user = auth()
        self.permission = sales_funcs.get_permisson(self.user)
        print(f'\n---Пользователь {self.user}, уровень доступа: {self.permission}---\n')
        if self.permission == 1:
            sale()
        elif self.permission == 2:
            admin()



if __name__=="__main__":
    app = App()
    app.start()