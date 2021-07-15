# Project Two
# By Rosario Robinson
# December 13, 2020
# Class: IT 140 - Introduction to Scripting
# Southern New Hampshire University

# A dictionary linking a room to other rooms
# and linking one item for each room except the Start room (Great Hall) and the room containing the Monster
rooms = {
    'Great Hall': {'North': 'Bedroom', 'South': 'Dining Room', 'East': 'Office', 'West': 'Kitchen', 'Item': ''},
    'Bedroom': {'South': 'Great Hall', 'East': 'Library', 'Item': 'Silver Sword'},  # item: silver sword
    'Library': {'West': 'Bedroom', 'Item': 'Monster'},  # monster!
    'Kitchen': {'East': 'Great Hall', 'Item': 'Shiny Medallion'},  # item: shiny medallion
    'Dining Room': {'North': 'Great Hall', 'East': 'Cellar', 'Item': 'Ruby Ring'},  # item: ruby ring
    'Cellar': {'West': 'Dining Room', 'Item': 'Ancient Book'},  # item: ancient book
    'Office': {'West': 'Great Hall', 'North': 'Living Room', 'Item': 'Magical Compass'},  # item: magical compass
    'Living Room': {'South': 'Office', 'Item': 'Gold Necklace'}  # item: gold necklace
}


# Function showing the instructions of the game and move commands
def show_instructions():
    # prints a main menu and the commands at the beginning of the game
    print("Welcome to the treasure hunt adventure game!")
    print("Collect all 6 treasure items to win the game.")
    print("Beware the monster in the Library; make the wrong turn and you'll lose the game!")
    print("Move commands: South, North, East, West")
    print("Add to Inventory: get 'item'")
    print("Start in the Great Hall. Which way do you want to go?")


# This function looks up the current room in the rooms dictionary and sees if it contains the direction.
def is_valid_direction(current_room, current_direction):
    # Check if the direction is valid in the dictionary for the current room
    if current_direction in rooms[current_room]:
        current_room = rooms[current_room][current_direction]
        print('You are in the ' + current_room + '.')
        return True
    elif current_direction == '':
        print('Please enter a move or type Exit to exit the game.')
    # Else statement for error for wrong direction
    else:
        print('You can’t go that way! Please enter another move.')
        return False


# This function prints the items for the inventory
def print_inventory(current_room, room_item):
    # Assigns current room item
    new_item = rooms[current_room]['Item']

    # Checks to see if there is an item in the treasure array
    if current_room == 'Great Hall':
        new_item = 'room with no treasure'
    else:
        if new_item in room_item:
            print('You see a ' + new_item + '. You already have this treasure.')
        else:
            # Appends item to the array in the room
            room_item.append(rooms[current_room]['Item'])

    # Print Inventory and Items
    print('Inventory:', end=' ')
    print(room_item)
    print('You see a ' + new_item + '.')
    print('-------------------------')
    print('Enter a move.')


# Displays instructions to begin the game
show_instructions()

if __name__ == '__main__':

    # User starts in the Great Hall
    startRoom = 'Great Hall'

    # Player direction input
    direction = input()

    # Variable to hold the current room
    room = startRoom

    # Treasure array
    treasure = []

    # Initializing number of Treasure items picked up
    num_of_items = 0

    # Main while loop for treasure hunt adventure game
    while True:

        # Player moving from Great Hall room
        if room == 'Great Hall':
            # Moving North, South, East, West from Great Hall
            if is_valid_direction(room, direction):
                if direction == 'North':
                    room = 'Bedroom'
                    print_inventory(room, treasure)
                elif direction == 'South':
                    room = 'Dining Room'
                    print_inventory(room, treasure)
                elif direction == 'East':
                    room = 'Office'
                    print_inventory(room, treasure)
                elif direction == 'West':
                    room = 'Kitchen'
                    print_inventory(room, treasure)

        # Player moving from Bedroom Room
        elif room == 'Bedroom':
            # Moving South and East from Bedroom
            if is_valid_direction(room, direction):
                if direction == 'South':
                    room = 'Great Hall'
                    print_inventory(room, treasure)
                elif direction == 'East':
                    room = 'Library'
                    print('You found the Monster! Sorry, Game Over!')
                    break

        # Player moving from Library Room
        elif room == 'Library':
            # Monster is located in this room, therefore the game ends when you enter
            print('You found the Monster! Sorry, Game Over!')
            break

        # Player moving from Kitchen Room
        elif room == 'Kitchen':
            # Moving East from Kitchen
            if is_valid_direction(room, direction):
                if direction == 'East':
                    room = 'Great Hall'
                    print_inventory(room, treasure)

        # Player moving from Dining Room
        elif room == 'Dining Room':
            # Moving North and East from Dining Room
            if is_valid_direction(room, direction):
                if direction == 'North':
                    room = 'Great Hall'
                    print_inventory(room, treasure)
                elif direction == 'East':
                    room = 'Cellar'
                    print_inventory(room, treasure)

        # Player moving from Cellar Room
        elif room == 'Cellar':
            # Moving West from Cellar
            if is_valid_direction(room, direction):
                if direction == 'West':
                    room = 'Dining Room'
                    print_inventory(room, treasure)

        # Player moving from Office Room
        elif room == 'Office':
            # Moving West and North from Office
            if is_valid_direction(room, direction):
                if direction == 'West':
                    room = 'Great Hall'
                    print_inventory(room, treasure)
                elif direction == 'North':
                    room = 'Living Room'
                    print_inventory(room, treasure)

        # Player moving from Living Room
        elif room == 'Living Room':
            # Moving South from Living Room
            if is_valid_direction(room, direction):
                if direction == 'South':
                    room = 'Office'
                    print_inventory(room, treasure)

        # Error to capture invalid commands.
        else:
            print('You entered an invalid direction. Type exit to exit the game, or Enter a direction to continue.')

        # If you found all 6 treasures, the game ends and you win
        if len(treasure) == 6:
            print('Wow, you found all the treasures! Congratulations! Thanks for playing!')
            break

        # Ask user input for direction
        direction = input()

        # Statement to exit the game
        if direction == 'Exit':
            print('Thanks for playing the game. Hope you enjoyed it.')
            break
