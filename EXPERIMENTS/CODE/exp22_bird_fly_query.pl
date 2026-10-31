bird(sparrow).
bird(eagle).
bird(pigeon).
bird(crow).
bird(penguin).
bird(ostrich).
bird(kiwi).

flightless(penguin).
flightless(ostrich).
flightless(kiwi).

can_fly(X) :-
    bird(X),
    \+ flightless(X).

cannot_fly(X) :-
    bird(X),
    flightless(X).

check_bird(X) :-
    can_fly(X),
    write(X), write(' can fly.'), nl.

check_bird(X) :-
    cannot_fly(X),
    write(X), write(' cannot fly.'), nl.

check_bird(X) :-
    \+ bird(X),
    write(X), write(' is not in the bird database.'), nl.
