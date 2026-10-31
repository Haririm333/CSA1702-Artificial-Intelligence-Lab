student(arun, 101, cse).
student(priya, 102, ai).
student(rahul, 103, cse).
student(sneha, 104, it).

teacher(dr_sharma, csa17).
teacher(prof_kumar, cs102).
teacher(dr_anita, ai201).

subject(csa17, artificial_intelligence).
subject(cs102, data_structures).
subject(ai201, machine_learning).

enrolled(arun, csa17).
enrolled(arun, cs102).
enrolled(priya, csa17).
enrolled(priya, ai201).
enrolled(rahul, cs102).
enrolled(sneha, ai201).

teacher_of_student(Teacher, Student) :-
    enrolled(Student, SubCode),
    teacher(Teacher, SubCode).

students_in_subject(SubCode, Student) :-
    enrolled(Student, SubCode).

student_subject_name(Student, SubName) :-
    enrolled(Student, SubCode),
    subject(SubCode, SubName).
