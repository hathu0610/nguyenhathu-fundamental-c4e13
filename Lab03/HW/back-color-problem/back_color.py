from random import *
import ex11
shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    #text:
    list_text = []
    for d in shapes:
        list_text.append(d["text"])
    text = choice(list_text)
    
    list_color = []
    for d in shapes:
        list_color.append(d["color"])
    color = choice(list_color)

    quiz_type = randint(0, 1)
    return [
                text,
                color,
                quiz_type # 0 : meaning, 1: color
            ]



def mouse_press(x, y, text, color, quiz_type):
    boo = True
    for d in shapes:
        if quiz_type == 0:
            if d["text"] == text:
                if ex11.is_inside([x,y], d["rect"]) == True:
                    boo = True
                else:
                    boo = False
        elif quiz_type == 1:
           if d["color"] == color:
                if ex11.is_inside([x,y], d["rect"]) == True:
                    boo = True
                else:
                    boo = False
    return boo

