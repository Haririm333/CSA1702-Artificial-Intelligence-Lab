prefix([], _).
prefix([H | T1], [H | T2]) :-
    prefix(T1, T2).

suffix(S, L) :-
    append(_, S, L).

sublist(Sub, List) :-
    append(_, Rest, List),
    append(Sub, _, Rest).

match_pattern([], []).
match_pattern([any | PT], [_ | LT]) :-
    match_pattern(PT, LT).
match_pattern([H | PT], [H | LT]) :-
    H \= any,
    match_pattern(PT, LT).

test_pattern :-
    write('Testing sublist [2, 3] in [1, 2, 3, 4]: '),
    (sublist([2, 3], [1, 2, 3, 4]) -> write('Matched'); write('Failed')), nl,

    write('Testing wildcard pattern [a, any, c] with [a, b, c]: '),
    (match_pattern([a, any, c], [a, b, c]) -> write('Matched'); write('Failed')), nl.
