from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        with open('data.txt') as data:
            self.highscore=int(data.read())
        # self.highscore=0
        self.color('white')
        self.hideturtle()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'ScoreBoard: {self.score} High score:{self.highscore}', False, align='center', font=('Arial', 15, 'normal'))

    def reset_score(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open('data.txt',mode='w') as data:
                data.write(f'{self.highscore}')
        self.score=0
        self.update_score()
    # def game_over(self):
    #      self.goto(0,0)
    #      self.color('white')
    #      self.write('Game over',align='center',font=('Arial',15,'bold'))

    def increase_score(self):
        self.score+=1
        self.update_score()

