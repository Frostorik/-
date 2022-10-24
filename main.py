field = list(range(1, 10))  # Массив игрового поля
win = [(1, 2, 3),
       (4, 5, 6),
       (7, 8, 9),
       (1, 4, 7),
       (2, 5, 8),  # Храним выигрышные позиции
       (3, 6, 9),
       (1, 5, 9),
       (3, 5, 7)
       ]


# Встречающее сообщение и инструкция по игре
def greet():
    print("Добро пожаловать в игру крестики нолики:")
    print("________________________________________")
    print("Для хода вы вводите значение ячейки, далее ставится ваш игровой знак.")


# Создание игрового поля
def draw():
    print("_______________")
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3])
    print("_______________")


# Ввод данных от пользователя и проверки ввода
def enter(player):
    while True:
        value = input(f"Укажите значение ячейки куда вы хотите сходить. Ходит игрок {player}. \n")

        # Проверка ввёл ли пользователь число или нет.
        if not (value.isdigit()):
            print("Вы ввели не число, повторите ввод.")
            continue
        value = int(value)

        # Проверка ввёл ли пользователь число находящееся в диапазоне.
        if not 1 <= value <= 9:
            print("Значение вне диапазона!")
            continue

        # Проверка занята ли ячейка на поле.
        if str(field[value - 1]) in "X0":
            print("Эта ячейка уже занята, выберите другую.")
            continue
        field[value - 1] = player
        break


# Проверка выигрыша.
def check_win():
    for i in win:
        if (field[i[0] - 1]) == (field[i[1] - 1]) == (field[i[2] - 1]):
            return field[i[1] - 1]
    else:
        return False


# Запуск функции
def start():
    greet()
    count = 0
    while True:
        draw()
        # Определяем порядок хода
        if count % 2 == 0:
            enter("X")
        else:
            enter("0")
        # После 3 хода начинаем проверять выигрышные позиции
        if count > 3:
            winner = check_win()
            if winner:
                draw()
                print(f"Выиграл {winner}!")
                break
        count += 1
        # Условие если поле заполнено
        if count > 8:
            draw()
            print("Ничья!")
            break


start()
