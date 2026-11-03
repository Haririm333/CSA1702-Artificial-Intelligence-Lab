move(state(middle, onbox, middle, hasnot),
     grasp,
     state(middle, onbox, middle, has)).

move(state(P, onfloor, P, H),
     climb,
     state(P, onbox, P, H)).

move(state(P1, onfloor, P1, H),
     push(P1, P2),
     state(P2, onfloor, P2, H)).

move(state(P1, onfloor, B, H),
     walk(P1, P2),
     state(P2, onfloor, B, H)).

canget(state(_, _, _, has), []).
canget(State1, [Action | Rest]) :-
    move(State1, Action, State2),
    canget(State2, Rest).

solve :-
    canget(state(door, onfloor, window, hasnot), Plan),
    write('Plan for monkey to get banana:'), nl,
    print_plan(Plan).

print_plan([]).
print_plan([H | T]) :-
    write(' -> '), write(H), nl,
    print_plan(T).
