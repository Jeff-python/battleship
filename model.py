from random import randint

lst_grid = []

for x in range(5):
    lst_grid.append(["O"] * 5)

def print_board(lst_grid):
    for row in lst_grid:
        print((" ").join(row))

print("Welcome to Simplified Battleship!")
print_board(lst_grid)


class ships:

    def __init__(self, position_x, position_y):

        self.position_x = position_x
        self.position_y = position_y

ship1 =ships(randint(0,4),randint(0,4))


ship_row = ship1.position_x
ship_col = ship1.position_y
count = 1
guess_remaining = 4
for turn in range(5):
    guess_row = int(input("Guess Row # from 0-4:"))
    guess_col = int(input("Guess Column # from 0-4:"))
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk the battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print(f"Guess:# {count},that is not on the Board, {guess_remaining} guess left")
            count+=1
            guess_remaining -=1
        elif(lst_grid[guess_row][guess_col] == "X"):
            print(f"Guess:# {count},you guessed that # already, {guess_remaining} guess left")
            count+=1
            guess_remaining -=1
        else:   
            print(f"Guess:# {count},you missed the battleship, {guess_remaining} guess left")
            lst_grid[guess_row][guess_col] = "X"
            count+=1
            guess_remaining -=1
    if turn == 4:
        print("Game Over")
    turn =+ 1
    print_board(lst_grid)

# 1) What data structures are you using to store the board? The ships?
# I am using 5 rows of lists to create the board. The ship is a tuple and an instance of the class, it takes the parameters of
# x and y positions.

# 2) What performance tradeoffs did you consider when considering which data structures to use?

# Since the size of the ship on the board in a simplified battleship is 1 and I only have 1 ship, the 
# searching time for storing the data in a tuple is o(n) or o(1) in this case. A better data structure to store many
# ships would be with a dictionary with a faster searching time, o(1) consistently. 

# 3)How are you modularizing your code? Why is a given code in Model versus View versus Controller?
# Not applied as my implementation of MVC is buggy.

# 4)Will there be a visual component? If so, how will you dislpay information to the user?

# 5)If you were to expand this with multiple ships of different dimensions, how would this be done? Be as specific as possible without writing code
# I would add a class parameter called something like size - this will allow ships to be distinguished by how many adjacent coordinates make up 
# the ship. (Example a destroyer can be a size 2 and an aircraft carrier can be a size 4)

# 6)If you were to expand this to be multiple players, how would this be done? Be as specific as possible without writing code   
# Add the following implementations:  
# Step 1, get ship(s) positions from the user and store row and column positions as the key, and ship name as the value of a dictionary. 
# example: {00:destroyer,01:destroyer}.
# Step 2, use the randint function from the library random to guess user's ship position by the computer.
# Step 3, create a function for turn alternation between user and computer.
# Step 4, create a function to print You Win or Game Over when one side of ship(s) is/are all destroyed.