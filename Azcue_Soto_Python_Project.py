# Jorge Azcue Soto
# IT - 140 Introduction to Scripting
# Alien Invasion Text Based project

# Introduction to the game w/ instructions
print("\n**Welcome to Jorge's first coding game..... ALIEN INVASION**\n")
print('ALIENS are invading Earth! They have taken over the city you live in, and you realize that one of them is in your house. \n'
          'Knowing this day would come, you have prepared yourself for this but realize that all your items are scattered all over your house. \n'
          'To defeat the aliens, you will need to collect ALL 6 items that are in each room of the house before making your way\n'
          'to the Basement where the alien is in. You will need:\n')
print('FLASHLIGHT from the Kitchen to see around the house\n' # Items to get
          'ALUMINUM HELMET from the Main Bedroom so they can not read your mind\n'
          'EAR PLUGS from the Guest Bedroom to tune out they high pitch noise\n'
          'BODY SUIT from the Guest Closet to protect your body\n'
          'RAY-GUN you built from the Garage to shoot the alien\n'
          'GAS MASK from the Living Room to prevent inhaling any toxic air\n')
print('Your move commands are: go South, go North, go East, go West')
print("To add an item to your Inventory type: get 'ITEM NAME'\n"
      "\nGOOD LUCK!")

# assigning rooms to other rooms w/ items in each room
rooms = {
        'Main Hallway': {'go South': 'Garage', 'go West': 'Main Bedroom', 'go North': 'Living Room', 'go East': 'Guest Bedroom'},
        'Garage': {'go North': 'Main Hallway', 'go East': 'Basement', 'item': 'RAY GUN'},
        'Basement': {'go West': 'Garage', 'item': 'ALIEN!'},
        'Main Bedroom': {'go East': 'Main Hallway', 'item': 'ALUMINUM HELMET'},
        'Guest Bedroom': {'go West': 'Main Hallway', 'go North': 'Guest Closet', 'item': 'EAR PLUGS'},
        'Guest Closet': {'go South': 'Guest Bedroom', 'item': 'BODY SUIT'},
        'Living Room': {'go South': 'Main Hallway', 'go East': 'Kitchen', 'item': 'GAS MASK'},
        'Kitchen': {'go West': 'Living Room', 'item': 'FLASHLIGHT'}
}

# starting point and starting inventory list
current_room = 'Main Hallway'
inventory = []

# Players inventory and which room they are in during the game
def player_status():
    print('-' * 50)
    print('Inventory:', inventory)
    print('You are in the', current_room)



# if, elif, else statement to collect items in rooms. And output if item has already been collected
    if current_room == 'Main Hallway':
        print('There is no item here to collect\n')
    elif current_room in rooms and rooms[current_room]['item'] not in inventory:
        print('You see:', rooms[current_room]['item'], '\n')
        print("To add an item to your Inventory type: get 'ITEM NAME'")
        inp = input('Make a move: ')
        if rooms[current_room]['item'] in inp and 'get' in inp:
            inventory.append(rooms[current_room]['item'])
            print('-' * 50)
            print('YOU GOT THE', rooms[current_room]['item'], '!')
            print('Inventory:', inventory)
        else:
            print()
    else:
        if current_room in rooms and rooms[current_room]['item'] in inventory:
            print('You have already collected the item in this room')
            print()


#Infinte loop for the game, with how to end the if player reaches Basement with all 6 items and without all 6 items
while True:
    if current_room == 'Basement':
        if len(inventory) >= 6:
            print('-' * 50)
            print('Congratulations! You have defeated the Alien!\n'
                  '1 Alien down... 10,000 more to go!\n'
                  '¯\_(ツ)_/¯\n'
                  "Thank you so much for playing, I hope you've enjoyed it\n"
                  'GAME OVER!')
        elif len(inventory) < 6:
            print('-' * 50)
            print('ZAAAAAAPP! You reached the basement before collecting all 6 items\n'
                  'The Alien has turned your brain into mush!\n'
                  'Thank you for playing.\n'
                  'GAME OVER')
        break
    player_status()
    user_input = input('Enter a move: ')

    if user_input in rooms[current_room]:
        current_room = rooms[current_room][user_input]
    else:
        print('-' * 50)
        print('THAT IS AN INVALID MOVE')
