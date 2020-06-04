from door_game import DoorGame
loop = 1_000_000

wins = 0
for i in range(loop):
    game = DoorGame()
    if game.play():
        wins = wins+1

print((wins/loop)*100)