use practice_db;
CREATE TABLE Activity (
    machine_id INT,
    process_id INT,
    activity_type enum('start', 'end'),
    timestamp FLOAT
);

INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES
(0, 0, 'start', 0.712),
(0, 0, 'end', 1.520),
(0, 1, 'start', 3.140),
(0, 1, 'end', 4.120),
(1, 0, 'start', 0.550),
(1, 0, 'end', 1.550),
(1, 1, 'start', 0.430),
(1, 1, 'end', 1.420),
(2, 0, 'start', 4.100),
(2, 0, 'end', 4.512),
(2, 1, 'start', 2.500),
(2, 1, 'end', 5.000);

select * from Activity;

select 
	a1.machine_id,
    round(avg(a2.timestamp - a1.timestamp),3) as processing_time
from 
	Activity a1 join Activity a2 on
    a1.machine_id = a2.machine_id and 
    a1.process_id = a2.process_id and
    a1.activity_type = 'start' and
    a2.activity_type = 'end'
group by a1.machine_id;


########################################################################

CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50)
);

INSERT INTO Students (student_id, student_name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(13, 'John'),
(6, 'Alex');

CREATE TABLE Subjects (
    subject_name VARCHAR(50) PRIMARY KEY
);

INSERT INTO Subjects (subject_name) VALUES
('Math'),
('Physics'),
('Programming');

CREATE TABLE Examinations (
    student_id INT,
    subject_name VARCHAR(50),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_name) REFERENCES Subjects(subject_name)
);

INSERT INTO Examinations (student_id, subject_name) VALUES
(1, 'Math'),
(1, 'Physics'),
(1, 'Programming'),
(2, 'Programming'),
(1, 'Physics'),
(1, 'Math'),
(13, 'Math'),
(13, 'Programming'),
(13, 'Physics'),
(2, 'Math'),
(1, 'Math');

select 
    st.student_id,
    st.student_name,
    sb.subject_name,
    coalesce(count(ex.student_id),0) as attended_exams
from 
    Students as st cross join
    Subjects as sb left join
    Examinations as ex on
    st.student_id = ex.student_id
    and sb.subject_name = ex.subject_name
group by sb.subject_name, st.student_id, st.student_name
order by st.student_id, st.student_name, sb.subject_name;


    








