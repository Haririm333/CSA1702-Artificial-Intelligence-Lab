fact(has_feathers).
fact(lays_eggs).
fact(can_swim).
fact(black_and_white).

is_true(Goal) :-
    fact(Goal).

is_true(bird) :-
    is_true(has_feathers),
    is_true(lays_eggs).

is_true(penguin) :-
    is_true(bird),
    is_true(can_swim),
    is_true(black_and_white).

backward_chain(Hypothesis) :-
    write('Testing hypothesis: '), write(Hypothesis), nl,
    (   is_true(Hypothesis)
    ->  write('Hypothesis confirmed: '), write(Hypothesis), nl
    ;   write('Hypothesis rejected: '), write(Hypothesis), nl
    ).
