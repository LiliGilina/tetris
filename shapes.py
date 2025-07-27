from turtle import Turtle
import random
STARTING_POSITION = [(-40,260), (-20,260), (0,260), (20,260), (-40,260)], [(-20,240), (0, 240), (0, 260), (20,240)], [(-40, 240), (-40, 260), (-20, 240),  (0,240), (20,240)], [(-20,240), (0, 240), (0, 260), (20,260)], [(-20,260), (0, 260), (0, 240), (20,240)], [(-20,260), (0, 260), (0, 240), (-20,240)]
COLORS = ["red", "blue", "green", "yellow", "purple", "cyan", "orange", "white"]


class Figurka():
    def __init__(self):
        self.figurka = []
        self.create_shape()
        
    def create_shape(self):
        starting_position = random.choice(STARTING_POSITION)
        shape_color = random.choice(COLORS)
        for posision in starting_position:
            new_shape = Turtle("square")
            new_shape.color(shape_color)
            new_shape.penup()
            new_shape.goto(posision)   
            self.figurka.append(new_shape)
    
    def down(self):
        for block in self.figurka:
            x = block.xcor()
            y = block.ycor()
            block.goto(x, y-20)

    
    def left(self):
        for block in self.figurka:
            x = block.xcor()
            y = block.ycor()
            block.goto(x-20, y)
           


    def right(self):
        for block in self.figurka:
            x = block.xcor()
            y = block.ycor()
            block.goto(x+20, y)

    def turn(self):
        if len(self.figurka) > 1:
            center = self.figurka[1]
            center_x, center_y = center.xcor(), center.ycor()
    
            for block in self.figurka:
                rel_x = block.xcor() - center_x
                rel_y = block.ycor() - center_y
                new_rel_x = rel_y
                new_rel_y = -rel_x
                new_x = center_x + new_rel_x
                new_y = center_y + new_rel_y
                block.goto(new_x, new_y)
        



    
    


                

    
