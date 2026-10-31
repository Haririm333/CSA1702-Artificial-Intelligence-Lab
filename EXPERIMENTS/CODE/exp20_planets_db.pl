planet(mercury, 57.9, 0, terrestrial).
planet(venus, 108.2, 0, terrestrial).
planet(earth, 149.6, 1, terrestrial).
planet(mars, 227.9, 2, terrestrial).
planet(jupiter, 778.6, 79, gas_giant).
planet(saturn, 1433.5, 82, gas_giant).
planet(uranus, 2872.5, 27, ice_giant).
planet(neptune, 4495.1, 14, ice_giant).

has_moons(Planet) :-
    planet(Planet, _, Moons, _),
    Moons > 0.

closer_than(Planet, ThresholdKm) :-
    planet(Planet, Distance, _, _),
    Distance < ThresholdKm.

planet_type(Planet, Type) :-
    planet(Planet, _, _, Type).
