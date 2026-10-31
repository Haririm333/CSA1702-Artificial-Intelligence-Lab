sum_to_n(0, 0).
sum_to_n(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_to_n(N1, PartialSum),
    Sum is N + PartialSum.

test :-
    sum_to_n(5, S),
    write('Sum from 1 to 5 is: '), write(S), nl,
    sum_to_n(10, S2),
    write('Sum from 1 to 10 is: '), write(S2), nl.
