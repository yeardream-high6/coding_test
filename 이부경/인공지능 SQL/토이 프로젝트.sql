-- a. Computer Science 학부 과목을 한 과목이라도 수강하고 있는 모든 학생의 ID와 이름을 출력하세요. 
-- (단, 중복을 제거하여 출력해주세요)
SELECT DISTINCT C.title, student.ID, student.NAME, student.DEPT_NAME
FROM course AS C
INNER JOIN takes AS T
	ON  C.course_id = T.course_id
INNER JOIN student
	ON T.ID = student.ID   
WHERE C.dept_name ='Comp. Sci.'
	AND T.YEAR = 2010
    AND T.SEMESTER = 'Fall'
ORDER BY student.ID; 
-- 2007년은 303건


-- b. “CS-001”를 id로 가지고, “Weekly Seminar”가 title인 1학점짜리 과목을 새로 신설해보세요.
-- select @@autocommit;
-- set autocommit = 1;
-- start transaction;
-- rollback;
-- COMMIT;
INSERT INTO course(course_id, title, credits)
values('CS-001', 'Weekly Seminar', 1);


-- c. Computer Science 학부생 전원을 sec_id가 1인 2017년도 가을학기 세션에 등록시켜주세요.
-- (HINT. University ERD도 참고해보세요)
INSERT INTO takes(ID, course_id, sec_id, SEMESTER, YEAR) 
SELECT student.ID, T2.course_id, T2.sec_id, T2.SEMESTER, T2.YEAR
FROM student, 
	(SELECT S.course_id, S.sec_id, S.SEMESTER, S.YEAR 
	FROM section S
	where S.sec_id = 1 AND
		S.SEMESTER = 'Fall' AND
		S.YEAR = 2007 ) AS T2
WHERE dept_name = 'Comp. Sci.'
	-- 기 수강 신청된 건들 제외
	AND (student.ID, T2.course_id, T2.sec_id, T2.SEMESTER, T2.YEAR) NOT in     
	(SELECT T.ID, T.course_id, T.sec_id, T.SEMESTER, T.YEAR  
	FROM takes T
	inner join student S
		on T.ID = S.ID
	WHERE S.dept_name = 'Comp. Sci.'
		and T.sec_id = 1
		and T.year = 2007
		and T.semester = 'Fall');

-- 조건에 맞는 과목 ->  5 과목 (SEC_ID = 1, YEAR=2007, SEMESTER='Fall')
-- 'Comp. Sci.' 학생 108명
-- 540 카테젼 곱 (= 5 * 108)

-- 그러나 540건을 다  넣으면 에러남 이미 수강 신청했던 건들의 경우 또 넣으려고 하는 것이 돼서
-- 그래서 기 수강신청된 건들은 제외 후 넣어야 함
-- 기 수강 신청된 수 82건
-- 그래서 540 - 82 = 458건


-- d. 각 학부별로 가장 많은 연봉을 가진 instructor중에서 가장 연봉이 낮은 instructor의 name과 dept_name을 찾아주세요.
SELECT dept_name, name, max(salary) as max_salary 
FROM instructor
GROUP BY dept_name
ORDER BY max_salary
LIMIT 1;
-- 'Psychology', 'DAgostino', '62579.61'


-- e. 2018년도 가을학기에 수업을 진행하는 모든 instructor를 찾아주세요.
SELECT * 
FROM teaches AS T
INNER JOIN instructor AS I
	ON T.ID = I.ID
WHERE T.year = 2008
	AND T.semester = 'Fall';
	
	
-- f. 2017년도 기준 물리학부에 재학중인 모든 학생을 찾아주세요.
SELECT distinct S.ID, S.name
FROM student S
INNER JOIN takes T
	ON S.ID = T.ID
WHERE S.dept_name = 'Physics'
	AND T.year = 2007
group by S.ID
order by name;


-- g. 컴퓨터공학 강사 Lee가 담당하고 있는 학생들 중 다른 학부 학생을 모두 찾아주세요.
SELECT * 
FROM instructor I
INNER JOIN advisor A 
	ON I.ID = A.i_ID
INNER JOIN student S
	ON S.ID = A.s_ID
WHERE 
	I.dept_name = 'Comp. Sci.'
    AND I.name = 'Lee'
    AND I.dept_name != S.dept_name  
order by I.name;


-- h. 이 때까지 한번도 과목을 수강한 적이 없는 모든 학생의 ID와 name을 출력해주세요.
SELECT ID, name
FROM student
where ID NOT IN 
	(SELECT ID FROM takes);