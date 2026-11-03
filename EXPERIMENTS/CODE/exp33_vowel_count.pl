vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).
vowel('A').
vowel('E').
vowel('I').
vowel('O').
vowel('U').

count_vowels([], 0).
count_vowels([H | T], Count) :-
    vowel(H),
    !,
    count_vowels(T, RestCount),
    Count is RestCount + 1.
count_vowels([_ | T], Count) :-
    count_vowels(T, Count).

count_vowels_in_atom(Atom, Count) :-
    atom_chars(Atom, CharList),
    count_vowels(CharList, Count).

test :-
    count_vowels_in_atom(artificial_intelligence, Count),
    write('Number of vowels in "artificial_intelligence": '), write(Count), nl.
