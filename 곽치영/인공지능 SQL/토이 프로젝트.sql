USE university;
SHOW TABLES;

# 처음에 JOIN으로만 짜다가 SubQuery도 나름 최적화 잘 되는 편 같아서 편하게 SubQuery로 짰습니다.
# 쿼리 앞에 EXPLAIN치면 구체적으로 어떻게 최적화하는지 나오는데 아직 정확한 뜻은 잘 모르겠네요.

# a. Computer Science 학부 과목을 한 과목이라도 수강하고 있는 모든 학생의 ID와 이름을 출력하세요.
# 현재까지 컴공과목을 하나라도 들은 학생 목록

SELECT ID, name
FROM student
WHERE ID IN (
	SELECT ID
    FROM takes
    WHERE course_id IN (
		SELECT course_id
        FROM course
        WHERE dept_name = 'Comp. Sci.'
    )
);

-- SELECT student.ID as ID, student.name as name
-- FROM student
-- LEFT JOIN takes
-- ON student.ID = takes.ID
-- LEFT JOIN course
-- ON takes.course_id = course.course_id
-- WHERE course.dept_name = 'Comp. Sci.'
-- GROUP BY student.ID;


# b. “CS-001”를 id로 가지고, “Weekly Seminar”가 title인 1학점짜리 과목을 새로 신설해보세요.
INSERT IGNORE INTO course
VALUE ('CS-001', 'Weekly Seminar', 'Comp. Sci.', 1);

# c. Computer Science 학부생 전원을 sec_id가 1인 2007년도 가을학기 세션에 등록시켜주세요.

# “Weekly Seminar”의 가을학기 세션1 을 새로 추가합니다.
# 섹션 장소와 시간은 null 이 들어갑니다.
INSERT IGNORE INTO section (course_id, sec_id, semester, year)
VALUE ('CS-001', 1, 'Fall', 2007);

# 컴공 학부생들 모두를 해당 세션에 배정합니다.
INSERT IGNORE INTO takes (ID, course_id, sec_id, semester, year)
SELECT student.ID, 'CS-001', 1, 'Fall', 2007
FROM student
WHERE student.dept_name = 'Comp. Sci.';

# d. 각 학부별로 가장 많은 연봉을 가진 instructor중에서 가장 연봉이 낮은 instructor의 name과 dept_name을 찾아주세요.
# 원래 밑에 주석된 쿼리로 제출했는데 다른분들 풀이 보고 간단하게 수정했습니다.

SELECT name, dept_name, salary
FROM instructor
INNER JOIN (
	SELECT dept_name, MAX(salary) as max_salary
	FROM instructor
	GROUP BY dept_name
    ORDER BY max_salary
    LIMIT 1
	) AS min_max_dept_salary
USING(dept_name)
WHERE salary = max_salary;


-- WITH max_salarys AS (
-- 	SELECT dept_name, MAX(salary) as max_salary
-- 	FROM instructor
-- 	GROUP BY dept_name
-- 	),
--     min_max_dept_salary AS (
-- 		WITH min_max_salarys AS (
-- 			SELECT min(max_salary) as min_max_salary
-- 			FROM max_salarys
--             )
-- 		SELECT dept_name, max_salary
--         FROM max_salarys, min_max_salarys
--         WHERE max_salarys.max_salary = min_max_salarys.min_max_salary
-- 	)
-- SELECT name, dept_name, salary
-- FROM instructor
-- INNER JOIN min_max_dept_salary
-- USING(dept_name)
-- WHERE salary = max_salary;

# e. 2008년도 가을학기에 수업을 진행하는 모든 instructor를 찾아주세요.
SELECT ID, name
FROM instructor
WHERE ID IN (
	SELECT ID
    FROM teaches
    WHERE year = 2008
		AND semester = 'Fall'
	);

-- SELECT ID, name, year, semester
-- FROM instructor
-- INNER JOIN teaches USING(ID)
-- #GROUP BY year, semester ORDER BY year, semester;
-- WHERE year = 2008 AND semester = 'Fall';

# f. 2007년도 기준 물리학부에 재학중인 모든 학생을 찾아주세요.
SELECT ID, name
FROM student
WHERE dept_name = 'Physics'
	AND ID in (
	SELECT ID
    FROM takes
    WHERE year = 2007);
    
-- SELECT ID, name
-- FROM student
-- INNER JOIN takes USING(ID)
-- WHERE dept_name = 'Physics' AND year=2007
-- GROUP BY ID;

# g. 컴퓨터공학 강사 Lee가 담당하고 있는 학생들 중 다른 학부 학생을 모두 찾아주세요.

SELECT ID, name, dept_name
FROM student
WHERE ID in (
	SELECT s_id
    FROM advisor
    WHERE dept_name != 'Comp. Sci.'
		AND ('Lee', 'Comp. Sci.') = (
			SELECT name, dept_name
			FROM instructor
			WHERE ID = i_id
			)
	);

# h. 이 때까지 한번도 과목을 수강한 적이 없는 모든 학생의 ID와 name을 출력해주세요.

SELECT ID, name
FROM student
WHERE ID NOT IN (
	SELECT ID
    FROM takes
    );