""" Brandon Goucher
    IT 140
    Dragon Text Adventure Game"""

playerAlive = True


def showInstructions():
    # prints the instructions to the game
    print("____________________________________________________")
    print("Dragon Text Adventure Game")
    print("Collect all 6 items to win the game or be eaten by the dragon.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: 'get item'")
    print("To check your inventory and room Type 'status'")
    print("____________________________________________________\n")


def showStatus(current_room, inventory):
    # shows your current room as well as what Items you have in your inventory
    print("____________________________________________________")
    print(current_room)
    print(f"Items: {inventory}")
    print("____________________________________________________\n")


rooms = {
    'Great Hall': {'North': 'Dungeon', 'South': 'Library', 'East': 'Gallery', 'West': 'Bedroom', 'item': 'Shield'},
    'Bedroom': {'North': 'Cellar', 'East': 'Great Hall', 'item': 'Armor'},
    'Cellar': {'South': 'Bedroom', 'item': 'Potion'},
    'Dungeon': {'South': 'Great Hall', 'item': 'Sword'},
    'Gallery': {'North': 'Kitchen', 'West': 'Great Hall', 'item': 'Boots'},
    'Kitchen': {'South': 'Gallery'},
    'Library': {'North': 'Great Hall', 'West': 'Dining Room', 'item': 'Book'},
    'Dining Room': {'East': 'Library'}
}
# items get stored into the "inventory here
items = []
# Starting room
room1 = 'Dungeon'
# To call the instructions to pop up only 1 time at the beginning
showInstructions()


def next_room():
    # takes in the string of what room you are in and prints the directions that you can go
    if room1 == 'Great Hall':
        print('You can travel, East, West, North, and South. \n')
    elif room1 == 'Bedroom':
        print('You can travel, North, and East. \n')
    elif room1 == 'Cellar':
        print('You can travel, South. \n')
    elif room1 == 'Dungeon':
        print('You can travel, South. \n')
    elif room1 == 'Gallery':
        print('You can travel, North, and West. \n')
    elif room1 == 'Kitchen':
        print('You can travel, South. \n')
    elif room1 == 'Library':
        print('You can travel, North and West. \n')
    elif room1 == 'Dining Room':
        print('You can travel, East. \n')


def move(direction, room='Dungeon'):
    # Move south
    if direction == 'South':
        if room1 == 'Dining Room' or room1 == 'Library' or room1 == 'Bedroom'\
                or room1 == 'Gallery':
            print('Invalid Direction. Please try again. \n')
            return room1
        else:
            print('I just moved.')
            print(f"You entered into the: {rooms[room]['South']} \n")
            showStatus(rooms[room]['South'], items)
            return rooms[room]['South']
    # Move East
    if direction == 'East':
        if room1 == 'Dungeon' or room1 == 'Kitchen' or room1 == 'Cellar'\
                or room1 == 'Library' or room1 == 'Gallery':
            print('Invalid Direction. Please try again. \n')
            return room1
        else:
            print('I just moved.')
            print(f"You entered into the: {rooms[room]['East']} \n")
            showStatus(rooms[room]['East'], items)
            return rooms[room]['East']
    # Move North
    if direction == 'North':
        if room1 == 'Cellar' or room1 == 'Dungeon' or room1 == 'Kitchen'\
                or room1 == 'Dining Room':
            print('Invalid Direction. Please try again. \n')
            return room1
        else:
            print('I just moved.')
            print(f"You entered into the: {rooms[room]['North']} \n")
            showStatus(rooms[room]['North'], items)

            return rooms[room]['North']
    # Move West
    if direction == 'West':
        if room1 == 'Dining Room' or room1 == 'Bedroom' or room1 == 'Dungeon'\
                or room1 == 'Cellar' or room1 == 'Kitchen':
            print('Invalid Direction. Please try again. \n')
            return room1
        else:
            print('I just moved.')
            print(f"You entered into the: {rooms[room]['West']} \n")
            showStatus(rooms[room]['West'], items)
            return rooms[room]['West']
    # gets the item
    if direction == 'GotItem':
        if room1 == 'Kitchen' or room1 == 'Dining Room':
            print('There is no item here. \n')
            return room1
        if rooms[room]['item'] in items:
            items.remove(rooms[room]['item'])
            items.append(rooms[room]['item'])
            print("You already have that item. \n")
        else:
            print(f"You got {rooms[room]['item']} \n")
            items.append(rooms[room]['item'])


# Main game loop.
# As long as the player is alive it will continue
while playerAlive is True:
    # Checks room
    if room1 == 'Dining Room':
        print('You entered into the Dragons Layer...')
        print(f'{items}\n')
        fight = input("Choose to Fight or Run! \n")  # Given the option to fight or run
        # if user chooses fight, it checks the items list and counts.
        # if item list is 6 or more, then they win
        if fight == 'Fight':
            if len(items) >= 6:
                print('You found all 6 items and were able to kill the dragon!')
                print("You won! Great job!")
                break
                # if items count is less than 6, then player loses
            else:
                print('You did not have enough items to fight him...')
                print('You lose.')
                playerAlive = False
                break
            # if they do not want to fight yet, they are given the option to run
            # using pass wil continue the game loop
        if fight == 'Run':
            pass

    user_input = input('Choose a Command: \n')

    if user_input == 'status':
        showStatus(room1, items)

    if user_input == 'get item':
        move('GotItem', room1)

    if user_input == 'quit':
        break
    if user_input == 'go South':
        room1 = move('South', room1)
        next_room()

    if user_input == 'go East':
        room1 = move('East', room1)
        next_room()

    if user_input == 'go North':
        room1 = move('North', room1)
        next_room()

    if user_input == 'go West':
        room1 = move('West', room1)
        next_room()
