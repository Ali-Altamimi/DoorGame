from door_game import DoorGame


def main():
    LOOP = 100_000
    DOORS = 5
    wins = 0

    for i in range(LOOP):
        game = DoorGame(DOORS)
        if game.play():
            wins = wins + 1
    percentage = (wins / LOOP) * 100
    print(f'{percentage:.2f}%')


if __name__ == '__main__':
    main()
