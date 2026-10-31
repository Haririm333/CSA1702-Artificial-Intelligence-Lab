male(john).
male(bob).
male(mike).
male(david).

female(mary).
female(lisa).
female(emma).

parent(john, bob).
parent(mary, bob).
parent(john, lisa).
parent(mary, lisa).
parent(bob, mike).
parent(emma, mike).
parent(bob, david).
parent(emma, david).

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

brother(X, Y) :-
    male(X),
    sibling(X, Y).

sister(X, Y) :-
    female(X),
    sibling(X, Y).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

grandfather(X, Z) :-
    male(X),
    grandparent(X, Z).

grandmother(X, Z) :-
    female(X),
    grandparent(X, Z).

ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
