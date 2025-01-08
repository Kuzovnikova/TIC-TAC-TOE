# Функция для инициализации игрового поля
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]


# Функция для вывода игрового поля
def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("-" * 9)
    print()  # Пустая строка для разделения


# Функция для проверки победителя
def check_winner(board):
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


# Функция для проверки, заполнено ли поле
def is_full(board):
    return all(cell != " " for row in board for cell in row)


# Основной игровой цикл
def play_game():
    board = initialize_board()  # Инициализация доски
    current_player = "X"

    while True:
        print_board(board)  # Передаем доску в функцию
        while True:
            try:
                row = int(input(f"Игрок {current_player}, введите номер строки (1-3): ")) - 1

                # Проверка на корректность ввода строки
                if row not in range(3):
                    print("Неверный ввод. Пожалуйста, введите число от 1 до 3.")
                    continue

                col = int(input(f"Игрок {current_player}, введите номер столбца (1-3): ")) - 1

                # Проверка на корректность ввода столбца
                if col not in range(3):
                    print("Неверный ввод. Пожалуйста, введите число от 1 до 3.")
                    continue

                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Эта клетка уже занята, попробуйте снова.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите целое число.")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Игрок {winner} выиграл!")
            break
        if is_full(board):
            print_board(board)
            print("Игра закончилась вничью!")
            break

        # Переключение игроков
        current_player = "O" if current_player == "X" else "X"


play_game()
