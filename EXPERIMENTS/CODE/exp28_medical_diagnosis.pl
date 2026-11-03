symptom(john, fever).
symptom(john, cough).
symptom(john, headache).

symptom(mary, chills).
symptom(mary, fever).
symptom(mary, sweating).

symptom(alice, sneezing).
symptom(alice, runny_nose).
symptom(alice, sore_throat).

disease(flu) :-
    symptom(Patient, fever),
    symptom(Patient, headache),
    symptom(Patient, cough),
    write(Patient), write(' is diagnosed with Flu.'), nl.

disease(malaria) :-
    symptom(Patient, fever),
    symptom(Patient, chills),
    symptom(Patient, sweating),
    write(Patient), write(' is diagnosed with Malaria.'), nl.

disease(common_cold) :-
    symptom(Patient, sneezing),
    symptom(Patient, runny_nose),
    symptom(Patient, sore_throat),
    write(Patient), write(' is diagnosed with Common Cold.'), nl.

diagnose(Patient, flu) :-
    symptom(Patient, fever),
    symptom(Patient, headache),
    symptom(Patient, cough).

diagnose(Patient, malaria) :-
    symptom(Patient, fever),
    symptom(Patient, chills),
    symptom(Patient, sweating).

diagnose(Patient, common_cold) :-
    symptom(Patient, sneezing),
    symptom(Patient, runny_nose),
    symptom(Patient, sore_throat).
