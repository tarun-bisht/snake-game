# Snake-Game
Snake-Game module in python, Can be used for Re-enforcement Learning.

# Documentation

### Module
- `snake`

  Importing Module

  `import snake as sn`

### Class
- `Snake`

  `sn.Snake(title, bgcolor, boundary_color, snake_color, snake_shape, food_color, food_shape, on_gameover)`

  - Parameters
    - title: Title shown in titlebar of game
    - bgcolor: Background color of window
    - boundary_color: Wall color which snake has to avoid
    - snake_color: color of Snake in game
    - snake_shape: shape of Snake and its segment
    - food_color: Color of food which snake has to eat
    - food_shape: Shape of food which snake has to eat
    - on_restart: Function which will be called when gameover occurs

  - Example

    ```python
      snake=Snake(title="Snake Game By Tarun Bisht", bgcolor="black", boundary_color="red", snake_color="white", snake_shape="square", food_color="yellow", food_shape="circle", on_gameover=on_gameover_function)
    ```

### Functions
- `start`

  Start Game
  - Example

  `snake.start()`

- `change_background`

  Change game background color
  - Example

  `snake.change_background("yellow")`

- `change_snake_color`

  Change snake color
  - Example

  `snake.change_snake_color("green")`

- `change_food_color`

  Change snake food color
  - Example

  `snake.change_food_color("red")`

- `change_background`

  Change game background
  - Example

  `snake.change_background("yellow")`
  `

## Code Example
```python
import random
import snake as sn

def on_gameover():
    index = random.randint(0, len(snake_colors) - 1)
    snake.change_background(bg_colors[index])
    snake.change_snake_color(snake_colors[index])
    snake.change_food_color(food_colors[index])


snake_colors = ["white", "blue", "black", "grey", "yellow", "green"]
bg_colors = ["black", "green", "white", "blue", "grey", "yellow"]
food_colors = ["blue", "yellow", "grey", "green", "white", "black"]
index = random.randint(0, len(snake_colors) - 1)

snake = sn.Snake(title="Snake Game", bgcolor=bg_colors[index], boundary_color="red",
              snake_color=snake_colors[index], snake_shape="square", food_color=food_colors[index], food_shape="circle",
              on_gameover=on_gameover)
snake.start()
```
