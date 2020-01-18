from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "empty"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Dictionary of all items that can be added to rooms

items = {
    "candle": Item("candle", "Sets the ground in front of you on fire. The fire can be used to burn away bushes or even light up dark areas."),
    "ring": Item("ring", "This ring mitigates damage taken by half and changes the color of Links tights."),
    "bomb": Item("bomb", "Used primarily to blow up weakened walls and also a winning component to beating certain enemies."),
    "boomerang": Item("boomerang", "A long-ranged weapon that can kill weaker enemies and stun some larger ones, such as Like-likes."),
    "clock": Item("clock", "Enemies sometimes drop this power-up. When picked up, it holds all enemies still, thus allowing you to kill things at your own pace."),
    "compass": Item("compass", "Obtaining the compass allows you to see where the piece of the triforce is in the current dungeon.")
}

# Added items to each room
room["outside"].add_item(items["ring"])
room["foyer"].add_item(items["candle"])
room["overlook"].add_item(items["bomb"])
room["narrow"].add_item(items["boomerang"])
room["treasure"].add_item(items["clock"])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print('Prepare to defend yourself player in Links Dream 🔥')
new_player = Player('Link', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    # Winning condition
    if len(new_player.get_inventory()) == 6:
        print(
            f"You've collected all items and escaped Links dream {new_player.name} 🔥!")
        break

    # Game description
    print("\n")
    print(
        f"Hi {new_player.name}! Your current location: {new_player.current_room.name}\n")
    print(
        f"Items in the room: {[item.name for item in new_player.current_room.get_items()]}")
    print(
        f"Your current inventory is: {[item.name for item in new_player.get_inventory()]}")
    print(f"Your current rupees is: {new_player.rupees}\n")
    print("Enter a direction: \nNorth: n\nSouth: s\nEast: e\nWest: w\nTo quit: q\n")
    print("To pick up an item, type take/get <item-name>")
    print("To drop an item: drop <item-name>\n")

    direction = input("Enter the direction you want to go: ")
    user_input = direction.strip().lower().split(" ")

    room_items = {
        item.name: item for item in new_player.current_room.get_items()}

    # To quit the game
    if len(user_input) == 1:
        if direction not in ["n", "s", "e", "w", "q", "i", "inventory"]:
            print("Please enter a valid direction\n")
            continue
        if direction == "q":
            print(
                "You have been consumed by darkness and trapped in this dream forever !")
            break

        # Picking a direction
        current_room = new_player.current_room
        if direction == "n":
            if current_room.n_to is None:
                print("You discover a dead end 🔒")
                continue
            else:
                new_player.current_room = current_room.n_to

        elif direction == "s":
            if current_room.s_to is None:
                print("You discover a dead end 🔒")
                continue
            else:
                new_player.current_room = current_room.s_to

        elif direction == "e":
            if current_room.e_to is None:
                print("You discover a dead end 🔒")
                continue
            else:
                new_player.current_room = current_room.e_to

        elif direction == "w":
            if current_room.w_to is None:
                print("You discover a dead end 🔒")
                continue
            else:
                new_player.current_room = current_room.w_to
        elif direction == 'i' or direction == 'inventory':
            print(f"\nYour inventory: {new_player.get_inventory()}")

    # Pick up or drop items
    elif len(user_input) == 2:
        action = user_input[0]
        item_str = user_input[1]

        if action == "take" or action == 'get':
            if item_str not in room_items:
                print("This object cannot be found in this room. You must be mistaken for something else. You will be trapped here forever")
                continue
            else:
                item = room_items[item_str]

                new_player.current_room.delete_item(item)
                new_player.add_item(item)
                item.on_take()

        elif action == "drop":
            if item_str not in room_items:
                print("You don't have " + item_str +
                      ", you cannot drop it. Stop making mistakes, or you'll regret it")
                continue
            else:
                item = room_items[item_str]

                new_player.delete_item(item)
                new_player.current_room.add_item(item)
                item.on_drop()
        else:
            print("Invalid command! WHAT ARE YOU DOING! Take this SERIOUS")
            continue
