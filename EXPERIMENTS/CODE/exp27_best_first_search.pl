edge(a, b, 2).
edge(a, c, 1).
edge(b, d, 5).
edge(b, e, 3).
edge(c, f, 4).
edge(c, g, 2).
edge(e, goal, 1).
edge(g, goal, 3).

h(a, 6).
h(b, 4).
h(c, 4).
h(d, 5).
h(e, 2).
h(f, 4).
h(g, 2).
h(goal, 0).

best_first_search(Start, Goal, Path) :-
    h(Start, H),
    bfs_queue([[node(Start, H)]], Goal, RevPath),
    reverse(RevPath, Path).

bfs_queue([[node(Goal, _) | Rest] | _], Goal, [Goal | RestNames]) :-
    extract_names(Rest, RestNames).

bfs_queue([CurrentPath | OtherPaths], Goal, FinalPath) :-
    CurrentPath = [node(CurrentNode, _) | _],
    findall([node(Next, HNext) | CurrentPath],
            (edge(CurrentNode, Next, _), \+ member(node(Next, _), CurrentPath), h(Next, HNext)),
            NewPaths),
    append(OtherPaths, NewPaths, AllPaths),
    sort_paths(AllPaths, SortedPaths),
    bfs_queue(SortedPaths, Goal, FinalPath).

extract_names([], []).
extract_names([node(N, _) | T], [N | Rest]) :-
    extract_names(T, Rest).

sort_paths(Paths, Sorted) :-
    map_list_to_pairs(path_h, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

path_h([node(_, H) | _], H).

test :-
    best_first_search(a, goal, Path),
    write('Best First Search Path: '), write(Path), nl.
