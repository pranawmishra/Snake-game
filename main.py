from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

snake = Snake()
food = Food()
food.refresh()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# snake.create_snake()
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
# segment = []
# for position in starting_position:
#     new_segment = Turtle(shape='square')
#     new_segment.color('white')
#     new_segment.penup()
#     new_segment.goto(position)
#     segment.append(new_segment)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collison with wall

    if snake.segment[0].xcor() > 290 or snake.segment[0].xcor() < -290 or snake.segment[0].ycor() > 290 or \
            snake.segment[0].ycor() < -290:
        scoreboard.reset_score()
        snake.reset()
        #  game_on = False
        #  scoreboard.game_over()

    # detect collision with tail
    for block in snake.segment[1:]:
        if snake.segment[0].distance(block) < 10:
            scoreboard.reset_score()

            snake.reset()
            # game_on = False
            # scoreboard.game_over()

    # for seg_num in range(len(segment)-1,0,-1):
    #     new_x=segment[seg_num-1].xcor()
    #     new_y=segment[seg_num-1].ycor()
    #     segment[seg_num].goto(new_x,new_y)
    # segment[0].forward(20)
    # segment[0].left(90)

# segment2=Turtle(shape='square')
# segment2.color('white')
# segment2.goto(-20,0)
#
# segment3=Turtle(shape='square')
# segment3.color('white')
# segment3.goto(-40,0)


screen.exitonclick()
