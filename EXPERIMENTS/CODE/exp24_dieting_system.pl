diet(diabetes,
     [oats, leafy_greens, whole_grains, fish, beans],
     [sugar, white_bread, soda, fried_food, sweets]).

diet(hypertension,
     [bananas, spinach, garlic, berries, low_fat_yogurt],
     [salt, canned_soup, pickles, red_meat, alcohol]).

diet(obesity,
     [salads, green_tea, steamed_vegetables, lean_chicken, water],
     [fast_food, sugary_drinks, butter, pastries, pizza]).

diet(anemia,
     [spinach, red_meat, lentils, dates, pomegranate],
     [excessive_tea, coffee, calcium_supplements_with_iron]).

diet(ulcer,
     [oatmeal, apples, carrots, bananas, curd],
     [spicy_food, citrus_fruits, caffeine, alcohol, peppers]).

suggest_diet(Disease) :-
    diet(Disease, Recommended, Avoid),
    write('--- Diet Plan for: '), write(Disease), write(' ---'), nl,
    write('Recommended Foods: '), write(Recommended), nl,
    write('Foods to Avoid: '), write(Avoid), nl.

suggest_diet(Disease) :-
    \+ diet(Disease, _, _),
    write('No diet plan found for: '), write(Disease), nl.
