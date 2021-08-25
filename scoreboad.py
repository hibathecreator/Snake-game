
from turtle import Turtle
import os
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            if os.path.getsize('data.txt') > 0:
                self.high_score = int(file.read())
            else:
                self.high_score = 0
                file.write(str(self.high_score))
        self.color('white')
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_scoreboad()

    def update_scoreboad(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboad()

    def increment_score(self):
        self.score += 1
        self.update_scoreboad()

