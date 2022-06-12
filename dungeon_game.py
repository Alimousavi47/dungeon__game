import random
import os
# draw grid
# pick a random location for the player
# pick a random location for the exit door
# pick a random location for the monster
# draw the player in the grid
# take input or movement
# move the player, unless invalid move (edges of grid)
# check if the player win/loss
# clear the screen and random grid

CELLS = [
    (0,0),(1,0),(2,0),(3,0),(4,0),
    (0,1),(1,1),(2,1),(3,1),(4,1),
    (0,2),(1,2),(2,2),(3,2),(4,2),
    (0,3),(1,3),(2,3),(3,3),(4,3),
    (0,4),(1,4),(2,4),(3,4),(4,4)
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_location():
    return random.sample(CELLS,3)

def move_player(player, move):
    x, y = player
    
    if move == 'LEFT':
        x -= 1
    if move == 'RIGHT':
        x += 1
    if move == 'UP':
        y -= 1
    if move == 'DOWN':
        y += 1
    return x, y
    # get the player's location
    # if move == LEFT, x-1
    # if move == RIGHT, x+1
    # if move == UP, y-1
    # if move == DOWN, y+1

def get_move(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = player
    
    # if player is x == 0, they can't move Left
    if x == 0:
        moves.remove('LEFT')
    
    # if player is x == 4, they can't move Right
    if x == 4:
        moves.remove('RIGHT')
    # if player is y == 0, they can't move Up    
    if y == 0:
        moves.remove('UP')
    
    # if player is y == 4, they can't move Down
    if y == 4:
        moves.remove('DOWN')
   
    return moves

def draw_map(player):
    print(" _" * 5)
    tile = "|{}"
    
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end = line_end)
            
def game_loop():
    monster, door, player = get_location()
    playing = True
    
    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_move(player)
        print("you currently in room {}".format(player)) #fill with player position
        print("you can move {}".format(", ".join(valid_moves))) #fill with available moves
        print("Enter 'Quit' to quit")
        move = input("> ")
        move = move.upper()
        if move == 'Quit':
            break
        if move in valid_moves:
            player = move_player(player, move)
            if player == monster:
                print("Monster got you!")
                playing = False
            if player == door:
                print("You escaped!")
                playing = False
        else:
            input("\n ** walls are hard!!! don't run into the them ** \n")

    else:
        if input("Play again? [Y/N] ").lower() == 'n':
            game_loop()
    # good move? change player position
    # bad move? don't change player position
    # on the door? they win
    # on the monster? they loss


clear_screen()
print("Welcome to the dungeon!")
input("Press 'return' to start the game!")
clear_screen()
game_loop()