person(john, dob(15, may, 1998)).
person(alice, dob(22, august, 2001)).
person(bob, dob(10, january, 1995)).
person(emma, dob(5, may, 1998)).
person(david, dob(19, december, 2003)).

born_in_year(Name, Year) :-
    person(Name, dob(_, _, Year)).

born_in_month(Name, Month) :-
    person(Name, dob(_, Month, _)).

get_dob(Name, Day, Month, Year) :-
    person(Name, dob(Day, Month, Year)).
