from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Times New Roman", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Times New Roman", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        # Clear the previous score display
        self.clear()

        # Move to the center at (0, 0) and display the "Game Over" message
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Times New Roman", 50, 'normal'))
