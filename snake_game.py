#AUTHOR TARUN BISHT
import random
from game.snake import Snake
def on_gameover():
    index=random.randint(0,len(snake_colors)-1)
    snake.change_background(bg_colors[index])
    snake.change_snake_color(snake_colors[index])
    snake.change_food_color(food_colors[index])
snake_colors=["white","blue","black","grey","yellow","green"]
bg_colors=["black","green","white","blue","grey","yellow"]
food_colors=["blue","yellow","grey","green","white","black"]
index=random.randint(0,len(snake_colors)-1)
snake=Snake(title="Snake Game By Tarun Bisht",bgcolor=bg_colors[index],boundary_color="red",snake_color=snake_colors[index],snake_shape="square",food_color=food_colors[index],food_shape="circle",on_gameover=on_gameover)
snake.play_game()
