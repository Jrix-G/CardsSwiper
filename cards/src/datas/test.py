import turtle
turtle.speed(0)

"""
def carre(cote) :
    # trace un carre de taille 100
    i = 1 # compteur du nb de cotes
    while i <= 4 :
        turtle.forward(cote)
        turtle.right(90)
        i = i + 1

def triangles(cote):
    for i in range(3):
        turtle.forward(cote)
        turtle.right(120)

def triangle(cote, x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    for i in range(3):
        turtle.forward(cote)
        turtle.right(120)

cote = 50
turtle.up()
turtle.goto(-300, -100)
turtle.down()
for i in range(3):
    carre(cote)
    turtle.up()
    turtle.forward(cote*2)
    turtle.down()
    triangles(cote)
    turtle.up()
    turtle.forward(cote*2)
    turtle.down()
    cote += 30

def rosace(x, y, nb, r):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    angle = 360 / nb
    for _ in range(nb):
        turtle.circle(r)
        turtle.right(angle)

def rosacelignes(x, y, nbRosaces, nbLignes, nb, r):
    for i in range(nbLignes):
        for j in range(nbRosaces):
            rosace(x + j * 100, y - i * 100, nb, r)

rosacelignes(-200, 0, 5, 5, 5, 10)

def carre(cote):
    for _ in range(4):
        turtle.forward(cote)
        turtle.right(90)

def carres_imbriques(cote_debut, nb_carres, x, y):
    cote = cote_debut
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    for _ in range(nb_carres):
        carre(cote)
        cote *= 2/3
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

carres_imbriques(50, 30, -100, 0)

def aller_sans_tracer(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

def descendre_sans_tracer(longueur):
    turtle.up()
    turtle.right(90)
    turtle.forward(longueur)
    turtle.left(90)
    turtle.down()

import math

def polygone(nb_cotes, cote):
    angle = 360 / nb_cotes
    for _ in range(nb_cotes):
        turtle.forward(cote)
        turtle.right(angle)

def diametre_polygone(nb_cotes, cote):
    return(cote/math.sin(math.pi/nb_cotes))

def colonne_polygone(nb_poly, cote):
    for i in range(3, 3 + nb_poly):
        polygone(i, cote)
        d = diametre_polygone(i, cote)
        descendre_sans_tracer(d + 5)

def pavage(nb_poly, nb_col, cote):
    aller_sans_tracer(-270, 330)
    for i in range(nb_col):
        turtle.down()
        colonne_polygone(nb_poly, cote)
        d = diametre_polygone(nb_poly + 2, cote)
        aller_sans_tracer(-270 + (d + 10) * (i + 1), 330)
        cote += 10

pavage(6, 4, 20)

"""

#Code bonus trouvé sur internet
import random 

def draw_black_rectangle(width, height):
    turtle.up()
    turtle.goto(-width // 2, height // 2)
    turtle.down()
    turtle.color("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_white_rectangle(x, y, width, height):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def move_turtle_randomly(steps, step_size, width, height):
    directions = [0, 90, 180, 270]
    for _ in range(steps):
        direction = random.choice(directions)
        turtle.setheading(direction)
        new_x = turtle.xcor() + step_size * (1 if direction == 0 else -1 if direction == 180 else 0)
        new_y = turtle.ycor() + step_size * (1 if direction == 90 else -1 if direction == 270 else 0)
        if -width // 2 < new_x < width // 2 and -height // 2 < new_y < height // 2:
            draw_white_rectangle(turtle.xcor(), turtle.ycor(), step_size, step_size)
            turtle.forward(step_size)

def create_maze(width, height, steps, step_size):
    draw_black_rectangle(width, height)
    turtle.color("white")
    turtle.up()
    turtle.goto(-width // 2 + step_size, height // 2 - step_size)
    turtle.down()
    move_turtle_randomly(steps, step_size, width, height)
    draw_white_rectangle(width // 2 - step_size, -height // 2 + step_size, step_size, step_size)  # Ensure exit

create_maze(600, 600, 100, 20)

turtle.mainloop()



