map = {
    "size_x" : 5,
    "size_y" :5
}
player = {
    "x" : 3,
    "y" : 4
}
boxes = [
    { "x": 1, "y": 1},
    { "x": 2, "y": 2},
    { "x": 3, "y": 3}
]

destination=[
    {"x":2, "y": 1},
    {"x":3, "y": 2},
    {"x":4, "y": 3},
]

playing = True
while playing == True :
    
    for y in range(map['size_y']):    
        for x in range(map['size_x']):
            box_is_here = False
            player_is_here = False
            destination_is_here = False
            if x == player['x'] and y == player['y']:
                player_is_here = True

            for box in boxes:
                if box['x']== x and box['y'] == y:
                    box_is_here = True
        
            for dest in destination:
                if dest['x']== x and dest['y'] == y:
                    destination_is_here = True
            
            if player_is_here == True:
                print("P", end= " ")
            elif box_is_here == True:
                print("B", end=" ")
            elif destination_is_here == True:
                print("D", end=" ")
            else:
                print("-", end=" ")
        print()

    move = input("Your move: ").upper()

    dx = 0
    dy = 0
    if move == "W":
       dy = -1
    elif move == "S":
       dy = 1
    elif move == "A":
       dx = -1
    elif move == "D":
        dx = 1
    else:
        print("Buzz")
        playing = False
    count = 0
    detectbox = True
    if 0<= player['x'] + dx < map['size_x'] and  0<= player['y'] + dy < map['size_y']:
        player['x'] += dx
        player['y'] += dy

    
    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player['y'] and detectbox == True:
            if 0<= box['x'] + dx < map['size_x'] and  0<= box['y'] + dy < map['size_y']:
                box['x'] +=dx
                box['y'] +=dy 
            else:
                player['x'] -= dx
                player['y'] -= dy

            for other_box in boxes:
                if box['x']  == other_box['x'] and box['y']  == other_box['y']:
                    detectbox = False

               
        for checkdest in destination:
            if checkdest['x'] == box['x'] and checkdest['y'] == box['y']:
                count+=1
            if count == 3:
                print("You win!")
                playing = False
    
