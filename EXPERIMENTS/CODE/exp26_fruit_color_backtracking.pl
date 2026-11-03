fruit_color(apple, red).
fruit_color(apple, green).
fruit_color(banana, yellow).
fruit_color(orange, orange).
fruit_color(grape, purple).
fruit_color(grape, green).
fruit_color(strawberry, red).
fruit_color(mango, yellow).

fruits_by_color(Color) :-
    fruit_color(Fruit, Color),
    write(Fruit), write(' is '), write(Color), nl,
    fail.
fruits_by_color(_).

colors_of_fruit(Fruit) :-
    fruit_color(Fruit, Color),
    write(Fruit), write(' can be '), write(Color), nl,
    fail.
colors_of_fruit(_).
