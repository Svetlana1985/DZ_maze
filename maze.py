
maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', 'E', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '0', '#', '#', '#', '#'],
]
def print_maze(maze):
    for row in maze:
        print(' '.join(row))



def find_exit(maze, x, y):
    moves = 0
    print('Выберите направление хода набрав нужную цифру:\nналево 4; направо 6; вверх 8; вниз 2')
    while True:
        player = input('Введите цифру для хода: ')
        new_x = x
        new_y = y
        if player == '6':
            new_y += 1
        elif player == '4':
            new_y -= 1
        elif player == '8':
            new_x -= 1
        elif player == '2':
            new_x += 1
        else:
            print('Неверный ввод, попробуйте снова')
            continue

        if maze[new_x][new_y] == '0':
            print("Выход найден!")
            break
        elif maze[new_x][new_y] == '#':
            print('Тупик, сделайте шаг в другую сторону')
        else:

            if maze[x][y] == 'E':
                maze[x][y] = '-'
            maze[new_x][new_y] = 'E'
            print_maze(maze)
            x, y = new_x, new_y
            moves += 1
    print(f'Количество ходов: {moves}')

print_maze(maze)
find_exit(maze, 3, 3)




