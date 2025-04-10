### Technical Description of the Task

#### Step 1

Implement your SQLAlchemy models for the following tables:

- Students table
- Groups table
- Teachers table
- Subjects table with the teacher who teaches the subject
- A table where each student has grades for subjects with the date when the grade was assigned

#### Step 2

Use Alembic to create migrations in the database.

#### Step 3

Write a `seed.py` script to populate the database with random data (~30-50 students, 3 groups, 5-8 subjects, 3-5 teachers, up to 20 grades for each student in all subjects). Use the Faker package for generating the data. When filling in the data, use the SQLAlchemy session mechanism.

#### Step 4

Make the following queries from the generated database:

1. Find the top 5 students with the highest average grade across all subjects.
2. Find the student with the highest average grade in a particular subject.
3. Find the average grade in groups for a specific subject.
4. Find the average grade for the entire batch (from the entire grades table).
5. Find the courses taught by a specific teacher.
6. Find the list of students in a specific group.
7. Find the grades of students in a specific group for a particular subject.
8. Find the average grade a teacher gives in their subjects.
9. Find the list of courses attended by a particular student.
10. Find the list of courses taught by a particular teacher to a specific student.

Create a separate file `my_select.py` to handle the 10 queries, from `select_1` to `select_10`. For the queries, use the SQLAlchemy session mechanism.
