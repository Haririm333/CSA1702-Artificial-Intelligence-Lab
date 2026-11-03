:- dynamic fact/1.

fact(has_fur).
fact(gives_milk).
fact(has_stripes).
fact(carnivore_teeth).

rule(mammal) :-
    fact(has_fur),
    fact(gives_milk).

rule(carnivore) :-
    fact(mammal),
    fact(carnivore_teeth).

rule(tiger) :-
    fact(carnivore),
    fact(has_stripes).

forward_chain :-
    rule(NewFact),
    \+ fact(NewFact),
    !,
    assertz(fact(NewFact)),
    write('Derived new fact: '), write(NewFact), nl,
    forward_chain.
forward_chain :-
    write('Forward chaining completed.'), nl.

show_facts :-
    listing(fact).
