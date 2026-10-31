hanoi(1, Source, Target, _) :-
    write('Move disk from '), write(Source), write(' to '), write(Target), nl.

hanoi(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Auxiliary, Target),
    hanoi(1, Source, Target, Auxiliary),
    hanoi(M, Auxiliary, Target, Source).

solve :-
    hanoi(3, 'Pole A', 'Pole C', 'Pole B').
