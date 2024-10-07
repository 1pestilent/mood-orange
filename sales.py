import sales_funcs

running = True

while running:
    n = int(input("""--- Выберите действие ---

    1. Добавить товар
    2. Добавить покупателя
    3. Добавить продажу
    0. Закончить

Выберите действие: """))
    if n == 1:
        print("""\n--- Добавление товара ---
Выберите сорт апельсина:
    """)
        sorts = [f"{row[0]} - {row[1]}" for row in sales_funcs.sorts()]
        for i in range(len(sorts)):
            print(sorts[i])
            
        sort = int(input("\n Сорт апельсина: "))
        x = True
        while x:
            if 0 < sort < (len(sorts)+1):
                x = False
            else:
                sort = int(input("\n Вы указали сорт апельсина неверно, попробуйте ещё раз: "))

        print("""\n--- Добавление товара ---
Выберите страну производства:
    """)
        countries = [f"{row[0]} - {row[1]}" for row in sales_funcs.countries()]
        for i in range(len(countries)):
            print(countries[i])
            
        country = int(input("\n Страна апельсина: "))
        x = True
        while x:
            if 0 < country < (len(countries)+1):
                x = False
            else:
                sort = int(input("Вы указали страну неверно, попробуйте ещё раз: "))   
        price = float(input("\n Укажите цену за штуку: "))
        confirm = int(input(f"""\n--- Вы хотите добавить товар со следущими параметрами: ---

    Сорт: {sorts[sort-1]}
    Страна: {countries[country-1]}
    Цена: {price} руб/шт

--- Подтвердите действие: --- 

1 - продолжить
0 - отменить

    Ответ: """))
        if confirm == 1:
            result = sales_funcs.add_product(sort, country, price)
            if result:
                print(f'Товара с данными параметрами был успешно добавлен. ID({result})\n')
            else:
                print('Добавить товар не удалось')
        else:
            print('Добавлена товара отменено!')

    elif n == 0:
        print('--- Работа приложения завершена ---\n')
        running = False
    else:
        print(False)