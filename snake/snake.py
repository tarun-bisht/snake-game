# AUTHOR TARUN BISHT
import time
import random
from .myturtle import create_turtle, set_screen, create_pen


class Snake:
    def __init__(self, title="Snake Game", width=600, height=600, bgcolor="white", boundary_color="black",
                 snake_speed=20, snake_color="white", snake_shape="square", food_color="red", food_shape="circle",
                 difficulty=True, on_gameover=None):
        # scores and highscores
        self.score = 0
        self.highscore = 0
        # set difficulty or not
        self.difficulty = difficulty
        # for storing records of snake body inserted
        self.body_segments = []
        # multiplier to make game not to run every frame of program used to make game slow
        self.deltaTime = 0.1
        # snake movement speed
        self.speed = snake_speed
        # boundary of screen
        self.boundaryx = (width / 2) - 40
        self.boundaryy = (height / 2) - 40
        # snake properties
        self.snake_color = snake_color
        self.snake_shape = snake_shape
        # on restart function
        self.on_gameover = on_gameover
        # setting up screen
        self.window = set_screen(title=title, width=width, height=height, bgcolor=bgcolor)
        # setting up snake
        self.head = create_turtle(color=self.snake_color, shape=snake_shape)
        # setting up food
        points = self.random_point()
        self.food = create_turtle(color=food_color, shape=food_shape, pos=(points[0], points[1]))
        # setting up pen
        self.pen = create_pen(color=snake_color, shape=snake_shape, pos=(0, self.boundaryy - 30))
        # boundary making
        self.make_boundary(width, height, boundary_color)

    # play game function
    def start(self):
        # keyboard movement binding
        self.window.listen()
        self.window.onkeypress(self.dir_up, "w")
        self.window.onkeypress(self.dir_down, "s")
        self.window.onkeypress(self.dir_left, "a")
        self.window.onkeypress(self.dir_right, "d")
        self.update()
        self.window.mainloop()

    # UPDATE FUNCTION
    def update(self):
        # loops every frame of game
        while True:
            # write on screen
            self.write_score(f"SCORE: {self.score}  |   HIGHSCORE: {self.highscore}")
            # check if snake collide border or collide its own body segments if so then game over
            if self.collide_border() or self.collide_body():
                self.game_over()
            # check if snake collides food if so then eat the food and generates new food
            if self.collide_food():
                self.eat_food()
            # updates and arranges new body segments of snake
            self.generated_body_setter()
            # move the snake
            self.move()
            # update window every frame
            self.window.update()
            # to stop moving the snake every frame of loop beacuse its too fast so moving it every 0.1 sec
            time.sleep(self.deltaTime)

    # CHECK COLLISION WITH FOOD
    def collide_food(self):
        return self.head.distance(self.food) < 20

    # CHECK IF SNAKE EAT FOOD
    def eat_food(self):
        self.score += 1
        if self.difficulty:
            self.deltaTime -= 0.001
        points = self.random_point()
        self.food.goto(points[0], points[1])
        # new segment of body created and attached to snake body
        new_segment = create_turtle(color=self.snake_color, shape=self.snake_shape)
        self.body_segments.append(new_segment)

    # RANDOM POINT INSIDE BOUNDARY
    def random_point(self):
        return (random.randint(-self.boundaryx, self.boundaryx), random.randint(-self.boundaryy, self.boundaryy))

    # CHECK IF SNAKE COLLIDE THE BORDER
    def collide_border(self):
        return self.head.xcor() > self.boundaryx or self.head.xcor() < -self.boundaryx or self.head.ycor() > self.boundaryy or self.head.ycor() < -self.boundaryy

    # CHECK COLLISON WITH SNAKE BODY
    def collide_body(self):
        for s in self.body_segments:
            if s.distance(self.head) < 15:
                return True
        return False

    # SNAKE DEATH GAME OVER
    def game_over(self):
        self.deltaTime = 0.1
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        time.sleep(2)
        self.restart_game()

    # SNAKE BODY GENERATION
    def generated_body_setter(self):
        for i in range(len(self.body_segments) - 1, 0, -1):
            x = self.body_segments[i - 1].xcor()
            y = self.body_segments[i - 1].ycor()
            self.body_segments[i].goto(x, y)
        if len(self.body_segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.body_segments[0].goto(x, y)

    # RESTART GAME
    def restart_game(self):
        if not self.on_gameover == None:
            self.on_gameover()
        self.head.goto(0, 0)
        self.head.direction = "stop"
        for s in self.body_segments:
            s.goto(10000, 10000)
        self.body_segments = []

    # MOVEMENT CODE
    # directions up,down,left,right
    def dir_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def dir_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def dir_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def dir_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    # movement
    def move(self):
        if self.head.direction == "up":
            self.head.sety(self.head.ycor() + self.speed)
        if self.head.direction == "down":
            self.head.sety(self.head.ycor() - self.speed)
        if self.head.direction == "left":
            self.head.setx(self.head.xcor() - self.speed)
        if self.head.direction == "right":
            self.head.setx(self.head.xcor() + self.speed)

    # WRITE ON SCREEN
    def write_score(self, text, align="center", font=("Arial", 14, "normal")):
        self.pen.color(self.snake_color)
        self.pen.shape(self.snake_shape)
        self.pen.clear()
        self.pen.write(text, align=align, font=font)

    # CHANGE PARAMETERS COLOR AND SHAPE
    # change bgcolor
    def change_background(self, color="white"):
        self.window.bgcolor(color)

    # change food color
    def change_food_color(self, color="white"):
        self.food.color(color)

    # change snake color
    def change_snake_color(self, color="white"):
        self.head.color(color)
        self.snake_color = color

    # change food shape
    def change_food_shape(self, shape="circle"):
        self.food.shape(shape)

    # change snake shape
    def change_snake_shape(self, shape="square"):
        self.head.shape(shape)
        self.snake_shape = shape

    # MAKE BOUNDARY
    def make_boundary(self, width, height, boundary_color):
        h = height / 2
        w = width / 2
        boundary = create_turtle(color=boundary_color, shape="square", pos=(-w, -h))
        boundary.pendown()
        boundary.pensize(30)
        for i in range(4):
            if i % 2 == 0:
                boundary.forward(width)
            else:
                boundary.forward(height)
            boundary.left(90)
        boundary.penup()
        boundary.hideturtle()


if __name__ == "__main__":
    snake = Snake(title="Snake Game", bgcolor="black", snake_shape="circle", food_shape="square")
    snake.start()
