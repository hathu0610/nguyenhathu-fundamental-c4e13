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
while playing:
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
    
    if 0<= player['x'] + dx < map['size_x'] and  0<= player['y'] + dy < map['size_y']:
        player['x'] += dx
        player['y'] += dy
    for newbox in boxes:
        if newbox['x'] == player['x'] and newbox['y'] == player['y'] and  0<= newbox['x'] + dx < map['size_x'] and  0<= newbox['y'] + dy < map['size_y']:
            newbox['x'] +=dx
            newbox['y'] +=dy 
    
