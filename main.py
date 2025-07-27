from turtle import Screen, Turtle
from shapes import Figurka
from ground import Ground
import time


screen = Screen()
screen.setup(height=600, width=370)
screen.bgcolor("black")
screen.title("TETRIS")
screen.tracer(0)

figurka = Figurka()
screen.update()
time.sleep(1)

def move_down():
    can_move = True
    for block in figurka.figurka:
        new_x = block.xcor()
        new_y = block.ycor() - 20
    
        if new_y <= -280:
            can_move = False
            break
    
        for ground_pos in ground.ground:
            if isinstance(ground_pos, tuple):
                ground_x, ground_y = ground_pos
                if new_x == ground_x and new_y == ground_y:
                    can_move = False
                    break
        
        if not can_move:
            break
    
    if can_move:
        figurka.down()
        screen.update()

def move_left():
    can_move = True
    for block in figurka.figurka:
        new_x = block.xcor() - 20
        new_y = block.ycor()
        
        if new_x < -160:
            can_move = False
            break
            
        for ground_pos in ground.ground:
            if isinstance(ground_pos, tuple):
                ground_x, ground_y = ground_pos
                if new_x == ground_x and new_y == ground_y:
                    can_move = False
                    break
        
        if not can_move:
            break
    
    if can_move:
        figurka.left()
        screen.update()

def move_right():
    can_move = True
    for block in figurka.figurka:
        new_x = block.xcor() + 20
        new_y = block.ycor()

        if new_x > 150:
            can_move = False
            break

        for ground_pos in ground.ground:
            if isinstance(ground_pos, tuple):
                ground_x, ground_y = ground_pos
                if new_x == ground_x and new_y == ground_y:
                    can_move = False
                    break
        if not can_move:
            break
    if can_move:
        figurka.right()
        screen.update()

def turn_shape():
    original_positions = [(block.xcor(), block.ycor()) for block in figurka.figurka]
    figurka.turn()
    valid_turn = True
    
    for block in figurka.figurka:
        if block.xcor() < -160 or block.xcor() > 150:
            valid_turn = False
            break

        for ground_pos in ground.ground:
            if isinstance(ground_pos, tuple):
                ground_x, ground_y = ground_pos
                if block.xcor() == ground_x and block.ycor() == ground_y:
                    valid_turn = False
                    break

        if not valid_turn:
            break

    if not valid_turn:
        for i, block in enumerate(figurka.figurka):
            block.goto(original_positions[i])
    
    screen.update()

def gravity():
    global figurka
    
    if check_game_over():
        game_over()
        return
    can_move = True
    for block in figurka.figurka:
        new_x = block.xcor()
        new_y = block.ycor() - 20
        if new_y <= -280:
            can_move = False
            break

        for ground_pos in ground.ground:
            if isinstance(ground_pos, tuple):
                ground_x, ground_y = ground_pos
                if new_x == ground_x and new_y == ground_y:
                    can_move = False
                    break
        
        if not can_move:
            break
    
    if can_move:
        figurka.down()
        screen.update()
        screen.ontimer(gravity, 150)
    else:
        ground.add_shapes(figurka)
        screen.update() 

        figurka = Figurka()
        
        spawn_blocked = False
        for new_block in figurka.figurka:
            for ground_pos in ground.ground:
                if isinstance(ground_pos, tuple):
                    ground_x, ground_y = ground_pos
                    if new_block.xcor() == ground_x and new_block.ycor() == ground_y:
                        spawn_blocked = True
                        break
            if spawn_blocked:
                break
        
        if spawn_blocked:
            game_over()
            return
        
        screen.update()
        screen.ontimer(gravity, 150)

ground = Ground()

def collision():
    for block in figurka.figurka:
        if block.ycor() <= -280:
            return True
        for ground_pos in ground.ground:
            if isinstance(ground_pos, tuple):
                ground_x, ground_y = ground_pos
                if block.xcor() == ground_x and block.ycor() - 20 == ground_y:
                    return True
    return False



def check_game_over():
    for ground_pos in ground.ground:
        if isinstance(ground_pos, tuple):
            ground_x, ground_y = ground_pos
            if ground_y >= 260: 
                return True
    return False

def game_over():
    screen.clear()
    screen.bgcolor("black")
    
    game_over_label = Turtle()
    game_over_label.hideturtle()
    game_over_label.color("white")
    game_over_label.penup()
    game_over_label.goto(0, 0)
    game_over_label.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
    
    
    screen.update()


gravity()

screen.listen()
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(turn_shape, "Up")



screen.mainloop()

