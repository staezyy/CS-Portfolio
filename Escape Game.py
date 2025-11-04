#Room Descriptions
room_list = []
room = ["You are in an empty, dark room. \nThere are passages North and West.", 1, None, None, 2]
room_list.append(room)
room = ["You are in a hospital room with flashing lights and shattered glass everywhere. \nThere are passages to the South and West.", None, None, 0, 3]
room_list.append(room)
room = ["You are in a nearly pitch black room, there are glowing white eyes in the corner. \nThere are doors North, East, and west.", 3, 0, None, 5]
room_list.append(room)
room = ["You are in an empty hall. \nThere are passages to the North, East, and South.", 4, 1, 2, None]
room_list.append(room)
room = ["You are in a waiting room, all the chairs are fallen over and destroyed. \nThere are doors South and West.", None, None, 3, 6]
room_list.append(room)
room = ["You followed the glowing eyes because you're stupid. But lucky for you, you found a room full of cute little cats. \nThere is a door back East.", None, 2, None, None]
room_list.append(room)
room = ["You found the exit! \nThe exit is to the West, but are you really gonna leave the cats...?", None, 4, None, 7]
room_list.append(room)
current_room = 0
done = False

#Loop for next rooms
while not done:
    print()
    print(room_list[current_room][0])
    x = input("What direction do you want to go? ").lower().strip()
    if x == "north" or x == "n":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif x == "east" or x == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif x == "south" or x == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif x == "west" or x == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    else:
        print("I don\'t know what you just typed")
    if x == "quit" or x == "q":
        print("You quit the game.")
        done = True
    if current_room == 7:
        print("You Escaped!")
        done = True
