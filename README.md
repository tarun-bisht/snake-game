# Snake-Game
Snake-Game module in python, Can be used for Re-enforcement Learning.
<h1> Documentation </h1>
<ul>
<li><h3>Module Name: game.snake</h3><li>
  <ul>
    <li><h3>Importing Module</h3>
      <p> <code>from game.snake import Snake</code></p>
    </li>
    <li><h3> Class: Snake</h3>
      <p><code>Snake(title, bgcolor, boundary_color, snake_color, snake_shape, food_color, food_shape, on_gameover)</code>
      <h5>Parameters</h5>
      <ul>
        <li>title: Title shown in titlebar of game</li>
        <li>bgcolor: Background color of window</li>
        <li>boundary_color: Wall color which snake has to avoid</li>
        <li>snake_color: color of Snake in game</li>
        <li>snake_shape: shape of Snake and its segment</li>
        <li>food_color: Color of food which snake has to eat</li>
        <li>food_shape: Shape of food which snake has to eat</li>
        <li>on_restart: Function which will be called when gameover occurs</li>
      </ul>
      <p><h6>Example</h6><code>snake=Snake(title="Snake Game By Tarun Bisht", bgcolor="black", boundary_color="red", snake_color="white", snake_shape="square", food_color="yellow", food_shape="circle", on_gameover=on_gameover_function)
      </code></p>
      </p>
    </li>
    <li><h3> Function: play_game</h3>
      <p>Start Game
      <p><h6>Example</h6><code>snake.play_game()</code></p>
      </p>
    </li>
  </ul>
</ul>
<h1> Code Example: </h1>
<p><h6>Example</h6>
 <code>#AUTHOR TARUN BISHT</code><br>
<code>import random</code><br>
<code>from game.snake import Snake</code><br>
<code>def on_gameover():</code><br>
    <code>index=random.randint(0,len(snake_colors)-1)</code><br>
    <code>snake.change_background(bg_colors[index])</code><br>
    <code>snake.change_snake_color(snake_colors[index])</code><br>
    <code>snake.change_food_color(food_colors[index])</code><br>
<code>snake_colors=["white","blue","black","grey","yellow","green"]</code><br>
<code>bg_colors=["black","green","white","blue","grey","yell</code><br>
<code>food_colors=["blue","yellow","grey","green","white","black"]</code><br>
<code>index=random.randint(0,len(snake_colors)-1)</code><br>
<code>snake=Snake(title="Snake Game By Tarun Bisht",bgcolor=bg_colors[index],boundary_color="red",snake_color=snake_colors[index],snake_shape="square",food_color=food_colors[index],food_shape="circle",on_gameover=on_gameover)</code><br>
<code>snake.play_game()</code><br>
</p>
