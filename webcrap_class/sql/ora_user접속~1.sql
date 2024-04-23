select * from employees;
-- 회원정보 테이블 생성
create table member (
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);
-- 데이터 입력
insert into member (id,pw,name,phone) values (
'aaa','1111','홍길동','010-1111-1111'
);
insert into member values (
'bbb','1111','유관순','010-2222-2222'
);
insert into member (id,name,phone) values(
'ccc','이순신','010-3333-3333'
);
-- 컬럼수 부족 에러
/*
insert into member values (
'ddd','강감찬','010-4444-4444'
);
*/
select id,pw,name,phone from member;
commit;
rollback;
select id,name from member;
select * from member;
insert into member values(
'ddd','1111','강감찬','010-4444-4444'
);
select * from member;
rollback;
commit;
select * from member;
update member set pw='2222' where id='ccc' ;
select * from member;
rollback;
-- 모든 테이블 확인
select * from tab;
-- 테이블의 타입 확인
desc member;
-- 오라클 타입
-- number-숫자,date-날짜,char-고정문자,varchar2-가변문자,clob-대용량문자
-- number : 정수,실수
-- number(4) : -9999~9999
create table mem (
no number, -- 길이 지정하지 않음.
no2 number(4),
no3 number(4,2)
);
insert into mem (no) values ( 1234567890 );
insert into mem (no2) values (9999);
insert into mem (no2) values (1.11);
insert into mem (no2) values (-9999);
insert into mem (no2) values (-10000);
insert into mem (no3) values(11.11);
insert into mem (no3) values(111 ); --111.00
select * from mem;
commit;
create table mem2 (
 no number(4,2),
 mdate date,
 mdate2 timestamp --date : 년,월,일,시,분,초까지 저장가능 / timestamp 밀리초까지 저장가능함.
);
insert into mem2 (mdate) values ('2024-04-19' );
insert into mem2 (mdate) values (sysdate); --sysdate:현재시간
insert into mem2 (mdate2) values (sysdate);
insert into mem2 (mdate,mdate2) values (sysdate,sysdate+30);
select * from mem2;
select to_char(mdate,'yyyy/mm/dd hh:mi:ss:ff') from mem2;
select to_char(mdate2,'yyyy/mm/dd hh:mi:ss:ff') from mem2;
select mdate,mdate+30 from mem2;
select * from employees;
select sysdate-hire_date from employees;
create table mem3 (
no number(4,2),
tel char(8),
name varchar2(9),
mdate date,
mdate2 timestamp
);
-- char,varchar2
-- char : 고정문자
insert into mem3 (tel) values ('11112222');
insert into mem3 (tel) values ('22223333');
insert into mem3 (tel) values ('111');
insert into mem3 (tel) values ('123456789');
insert into mem3(tel) values ('홍');
-- varchar2 : 가변문자
insert into mem3 (name) values ('11112222');
insert into mem3 (name) values ('홍길동'); --한글 :3크기
insert into mem3 (name) values ('신사임당'); -- 12자리 필요
INSERT INTO MEM3 (NAME) VALUES ('AAA');
insert into mem3 (name) values ('aaa');
commit;
select * from mem3 where name='aaa'; -- sql구문은 대소문자 구분없음, 데이터는 대소문자 구분함.
select * from mem3 where name='AAA';
select * from mem3 where lower(name)='aaa';
-- select,from 2개의 키워드로 구성 됨.
-- * 모든 컬럼을 출력
-- 대소문자를 구분하지 않음.
select * from mem;
SELECT * FROM MEM;
select emp_name,department_id from employees;
-- distinct 같은 것은 1번만 출력
select distinct department_id from employees;
select * from departments;
select * from employees;
select * from mem3;
select no,mdate2,tel,name,mdate from mem3;
select * from employees;
-- 사원번호(e id), 사원이름(e name),급여(salary), 입사일자(hire_date)
select employee_id,emp_name,salary,hire_date from employees;
desc employees;
select * from stu_score;
-- 테이블 삭제
drop table stu_score;
create table stu_score (
 no number,
 name varchar2(30),
 kor number(3),
 eng number(3),
 math number(3),
 total number(3),
 avg number(5,2),
 rank number
);
insert into stu_score values (
1,'홍길동',100,100,100,300,100,1
);
insert into stu_score values (
5,'김구',100,100,100,300,100,1
);
commit;
select * from stu_score;



--산술연산자 number타입인 경우

select  * from stu_score;
insert into stu_score values(
6,'김유신',100,95,96,(100+95+96),(100+95+96)/3,1
);

select  * from stu_score;

insert into stu_score values(
7,'홍길자',100,100,99,(100+100+99),(100+100+99)/3,1
);

select  * from stu_score;

--번호, 이름,국어점수,국어점수의-20,평균,평균-20을 뺀,국어점수를-20한 평균
select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score;

select  * from employees;
 --달러 원화 환산 - 1381.79원=1달러


select employee_id,emp_name,salary*1381.79 from employees;

--월급 *12 = 연봉
select * from employees;
select employee_id,emp_name,salary*12,salary*1381.79*12 from employees; --연봉(달러단위),--연봉(원단위)


--커미션은 실제월급 = 월급 + 월급*커미션
--commission_pct
select * from employees;

select employee_id,emp_name,salary+(salary*commission_pct) from employees;

--nvl(컬럼,0)으로 정의해줘라
select employee_id,emp_name,nvl(commission_pct,0),salary+(salary*nvl(commission_pct,0)) from employees;

commit;









-------------------------------------------------------------------------------
--24.04.22

select * from employees;

select employee_id,emp_name from employees;

select salary from employees;

-- 타입 : number +,-,*,/ 가능
select salary, salary * 1400 k_sal,salary*1400*12 as y_sal from employees;

select * from stu_score;

select no,name,kor,eng,math,total,avg,rank from stu_score;

-- 파이썬.

select department_id from employees;

select nvl(department_id,0) from employees;

select * from employees;

-- 별칭 : as사용, "" : 키워드를 있는 그대로 사용
select salary, salary + (salary*nvl(commission_pct,0)) as "real_sal*" from employees;

-- 한글 사용가능
select salary as "년봉" from employees;

-- 

select * from departments;

-- 부서번호, 부서이름을 출력하시오.
select department_id,department_name from departments;

-- 여러개의 데이터를 1개라 합쳐서 넘겨야 할 경우 concat
-- concat : 홍길동,유관순,이순신,강감찬,김구 -> split(",") : 분리 

select * from stu_score;

-- concat ||
select kor||','||eng||','||math stu from stu_score;

select kor+eng+math as total,(kor+eng+math)/3 from stu_score;

-- 중복제거 : distinct
-- where : 조건절 not 제거하고 검색하려면 is not null
select distinct department_id from employees where department_id is not null;

-- manager_id

select manager_id from employees;

select distinct manager_id from employees;
select distinct manager_id from employees where manager_id is not null;


select * from employees;

select employee_id,salary from employees
where employee_id = 200 or employee_id = 201 or employee_id=202;

select * from employees
where employee_id >= 200 and employee_id <=203;

select * from employees
where employee_id <= 150 or employee_id>=200;

-- department_id 10,30,50에 해당되는 사원을 출력하시오.
select employee_id,department_id,salary from employees
where department_id = 10 or department_id = 30 or department_id = 50;

-- 월급 6000 ~ 9000 이하인 사원을 출력하시오.
-- 정렬 order by 컬럼 asc : 순차정렬,desc : 역순정렬
select salary from employees where salary>=6000 and salary<=9000
order by salary desc
;
-- 월급 6000,7000,8000 인 사원을 출력하시오.
select salary from employees
where salary =6000 or salary=7000 or salary = 8000;

-- 부서번호가 50번이면서, 월급이 8000 이상인 사원을 출력하시오.
select department_id,salary from employees
where department_id=50 and salary >= 8000;

-- stu_score 홍길동 출력하시오.
select * from stu_score
where name = '홍길동';

-- 순차정렬
select hire_date from employees
order by hire_date asc
;
-- 역순정렬
select hire_date from employees
order by hire_date desc
;

select emp_name,hire_date from employees
where hire_date >= '02/01/01'
order by hire_date asc
;

select hire_date,hire_date+100 from employees;
-- 반올림 round
select round(sysdate-hire_date,2) from employees;

select * from employees;

-- 문자합치기는 +연산자 불가능, ||명령어 사용
select emp_name||email from employees;

-- 입사일 05년 이상 06년 이하이면서 월급이 6000 달러 이상인 사원을 입사일 역순정렬로 출력하시오.
select emp_name,hire_date,salary from employees
where hire_date >= '05/01/01' and hire_date <= '06/12/31' and salary >=6000
order by hire_date desc
;

-- !=, <>,^=, not
select department_id from employees
where department_id != 10 and not department_id = 50
order by department_id
;

-- salary 5000 이상 9000 이하
select emp_name,salary from employees
where salary >= 5000 and salary <= 9000
order by salary
;

-- 평균이 99점 이상인 학생을 검색하시오.
select * from stu_score
where avg>=99
;

select * from students;

update students set name='관순스' 
where no = 10
;

commit;

select * from students;

-- students
-- 국어가 70, 평균 75점 이상인 학생을 출력하시오.
select name,kor,avg from students
where kor>=70 and avg>=75
;

-- 국어점수 80, 국어점수 70, 국어점수 90 인 학생을 출력하시오.
select name,kor from students
where kor=80 or kor = 70 or kor = 90;

-- in 연산 동일한 필드가 여러개의 값 중에 하나를 검색할 경우
select name,kor from students
where kor in(80,70,90);

select name,kor from students
where kor not in(80,70,90);


update students set kor=100 
where no=1;

rollback;

select * from students
where no = 1;

-- 수정
update students set kor=100, total = 100+eng+math, avg = (100+eng+math)/3
where no=1;


-- 국어점수 70 ~ 90 이상 학생을 출력하시오.
select kor from students
where kor > 70 and kor <= 90
;

-- 100명
select * from students;

-- 27명 between a and b : a보다 크거나 같고 b보다 작거나 같은 것 검색
select kor from students
where kor between 70 and 90
;

-- 73명 not between a and b : a보다 크거나 , b보다 작은것 검색
select kor from students
where kor not between 70 and 90
;

-- 날짜도 between a and b

select hire_date from employees
order by hire_date;

-- 입사일 99년보다 크거나 같고, 01년 보다 작거나 같은 사원 검색
select hire_date from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date asc
;

-- 이름검색
select * from students
where name='홍길동'
;

-- like 검색 : 특정단어가 포함되어 있는 것을 검색
-- 홍% : 홍으로 시작되는 단어 검색
select * from students
where name like '홍%'
;

-- %순 : 순으로 끝나는 단어 검색 
select * from students
where name like '%순'
;

-- %길% : 특정단어가 포함되어 있는 단어 검색
select * from students
where name like '%길%'
;

-- _ : 한 칸 공간을 사용, 길 앞에 1개의 단어가 있으면서 길이 포함되어 있는 단어 검색
select * from students
where name like '_길%'
;


select * from students;

-- 3번째에 t가 들어가 있는 이름 검색
-- __t
select * from students
where name like '__t%'
;

-- 이름이 4자리인, 3번째 r이 들어가 있는 이름 검색
select * from students
where name like '__r_'
;

select * from students
where name like '__r%' and length(name) = 4
;

-- 이름 길이가 4자리 인것 검색
select name from students
where length(name) = 4
;

-- 이름이 A로 시작되는 학생 검색
select no,name from students
where name like 'A%'
;

-- 이름에 a가 들어가 있는 학생 검색
select no,name from students
where name like '%a%'
;

-- 대소문자 구분없이 a가 들어가 있는 학생 검색
-- 소문자 취환(lower), 대문자 취환 (upper), 첫글자 대문자 (initcap)
select no,name from students
where lower(name) like '%a%'
;

-- a가 포함되지 않은 이름을 검색
select no,name from students
where lower(name) not like '%a%'
;


select manager_id from employees;

-- manager_id 100인 사원 검색
select employee_id,emp_name,manager_id from employees
where manager_id = 100
;

-- null 은 등가비교가 안됨.
select employee_id,emp_name,managaer_id from employees
where manager_id = null
;

-- null값은 is null 명령어 사용
select employee_id,emp_name,manager_id from employees
where manager_id is null
;

select * from employees
where manager_id is not null
;

select * from stu_score;

-- 한글 정렬 가능
select * from stu_score
order by name asc
;


select * from students;


-- 1차 국어점수로 역순정렬 한 다음, 같은 점수인 경우, 영문점수로 순차정렬 진행
select * from students
order by kor desc, eng asc
;

-- total로 역순정렬

select * from students
order by total desc
;

-- 컬럼추가
alter table students add rank number(3);

-- 컬럼타입
desc students;

select * from students;

update students set rank=0;

commit;

-- 등수
select no,rank() over(order by total desc) as rank from students
;

select no,rank() over(order by total desc ) as ranks from students
;

update students s1 set rank = (select ranks 
from (select no, rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no )
;

update students s1 set rank = 13
where no = 1
;

update students set rank=0;
select no,rank from students;




-- 수정
update students set rank = 13
where no = 1
;

select * from students
where kor>=70;


select * from (테이블);


select * from (select * from students where avg>=80)
where kor>=70
;

-------------------------------------------------------------------------------
--24.04.23

--select * from students;
--테이블 컬럼추가
alter table students add rank number(3);

select * from students;

update students set rank=0;

commit;

select * from students;

select rank() over(order by total desc) rank 
from students;

update students set total=0;

select total,rank from students
order by total desc;



update students set total=(kor+eng+math);

update students a set rank=  (select ranks
from (select no,rank() over(order by total desc) ranks
from students) b where a.no = b.no);

--1.update구문
update students a set rank= (rank);

--2. no,rank()구문
(select no,rank() over (oeder by total desc) ranks from students) b;

--3.update구문 rank()구문을 no컬럼으로 비교, rank컬럼을 검색
update students a set rank= (
 select ranks from (students) b
  where a.no = b.no
  );

update students a set rank= ( 
 select ranks from (select no,rank() over (oeder by total desc) ranks from students) b
 where a.no = b.no);
 
 --역순정렬
 select no,total,rank from students
 order by total desc;
 
 --no순차정렬
 select no,total,rank from students
 order by no;
 
 select no,kor,eng,math,total,rank from students
 order by kor desc, eng asc;
 
 select manager_id from employees
 order by manager_id desc;
 
 select hire_date from employees
 order by hire_date desc;
 
 select max(hire_date)-min(hire_date) from employees
 order by hire_date desc;
 
  select max(kor)-min(kor) from students;
  select max(kor),max(eng),max(kor) from students;
  
--퀴즈1
--입사일은 오름차순으로!!,
--컬럼은 사원번호,사원명,job_id-직급,입사일,월급 컬럼을 출력하시요.
select employee_id,emp_name,job_id,hire_date,salary  
from employees
order by hire_date desc;

--퀴즈2
--급여를 적게받는 사람순으로 출력하되 월급이 같으면, 사원명으로 순차정렬하시요
select emp_name,salary  
from employees
order by  emp_name,salary desc;


--숫자함수
--abs(무조건 양수가 나온다)
--round(반올림)
--floor(소수점 버리기)

select -10, abs(-10) from dual;

select 34.789, floor(34.789) as f,round(34.789)as r from dual;

select 34.178, round(34.178), round(34.178,2) from dual; --라운드는 소수점반올림 위치를 지정가능

--------------------------------중요---------------------------------------
select avg from students;
select round(avg,2) avg from students; --소수점 2째자리까지만!!

select 34.5678, round(34.5678,-1) from dual;

--trunc 지정 자리수 이하 버리기
select trunc(34.5678,2) trunc from dual;
select trunc(34.5678) trunc from dual;

--무조건 올림 소수점없음
select ceil (34.1278) from dual;

--국어점수 일단위 절사해서 출력하시요(십단위로 출력)
select trunc(kor,-1) from students
order by kor;

--국어,영어,수학 일단위절사해서 합을 출력하시요
SELECT trunc(kor, -1) AS 국어, 
       trunc(eng, -1) AS 영어, 
       trunc(math, -1) AS 수학, 
       trunc(kor, -1)+trunc(eng, -1)+trunc(math, -1) as 합계
FROM students;

--mod 나머지
select round(100/7,2) from dual;
select mod(10,7) as 나머지 from dual;

--나누기
select 10/7 as 나누기 from dual;

--퀴즈. 사원번호가 짝수인것을 출력하시요!!
SELECT employee_id  from employees WHERE mod(employee_id,2) = 0;

--몫
select floor(10/7) from dual;

--나머지가 0이면 짝수,3이면 홀수
select mod(10,7) from dual;

--퀴즈 학번 3의 배수인것만 찾으세요 students테이블
select no from students
where mod(no,3)=0;

----6장(시퀀스)----

create sequence seq_no
increment by 1 --증감이 1씩증가
start with 1 --시작이 1부터 진행
minvalue 1 --최소값 1
maxvalue 9999 --최대값 9999
nocycle --순환하지 않음
nocache; --캐쉬를 사용하지 않음

--nextval 시퀀스 번호 1씩 증가
select seq_no.nextval from dual;

--currval 시퀀스 번호 확인
select seq_no.currval from dual;

--drop table member;

--drop table mem3;

create table member(
mno number(4),
id varchar2(30),
pw varchar2(20),
name varchar(30),
phone varchar(15));

create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

select seq_mno.nextval from dual;

insert into member values(
seq_mno.nextval,'ccc','1111','이순신','010-3333-3333'

);

select * from member;

--한국대학교 ko라 하고 24학번의 ko20240001번으로 출력


select sysdate from dual;
select to_char(sysdate,'yyyy') from dual;

select 's0001' || to_char(seq_mno.currval) from dual; 

--한국대학교 ko라 하고 24학번의 ko20240001번으로 출력

create sequence seq_ko
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache
;

--trim() 공백제거 자동으로 번호 생성
select 'ko' || to_char(sysdate,'yyyy')||trim(to_char(seq_ko.nextval,'00000'))as stu_no from dual;

--게시판 
create table board(
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10)
);

commit;

--퀴즈
create sequence seq_deptno
increment by 10
start with 1001
minvalue 1
maxvalue 99999
cycle
nocache
;


create table emp01(
 empno number(4) primary key,
 ename varchar(30),
 hire_date date
);


--새로운 시퀀스 생성--
create sequence emp_seq
    increment by 1
    start with 1
    minvalue 1
    maxvalue 9999
    nocycle
    nocache
    ;
    
    --시퀀스 수정--
    alter sequence emp_seq
    increment by 1001;
    
insert into emp01 values(
emp_seq.nextval, '이순신',sysdate
);

select * from emp01;

commit;

--현재까지 입사한 일수를 출력하시요. 반올림하세요

select employee_id,emp_name,job_id,hire_date,ceil(sysdate-hire_date)||'일'  
from employees
order by hire_date desc;

select emp_name from employees;

--퀴즈
--직급과 사번을 합쳐서 출력하시요.
select employee_id||job_id 
from employees;

select substr(job_id,0,2) from employees;
select emp_name ,substr(emp_name,1,3) from employees;

-- substr은 문자열 자르기(2번째부터 3개만 짤라와라) substr(대상,시작위치,개수)
select substr('abcde',2,3) from dual;

--퀴즈
select substr(job_id,0,2)|| trim(to_char(employee_id,'00000')) as 하이루 from employees;


--날짜함수
select sysdate from dual;

select to_char(sysdate,'yyyy-mm--dd hh24:mm:ss')from dual;

--두날짜 사이의 개월수 확인
select MONTHS_BETWEEN(SYSDATE,hire_date),sysdate-hire_date from employees;

--개월수를 추가
select sysdate, add_months(sysdate,2) from dual;

--오늘기준으로 다음주 요일 날짜를 알려준다.
select next_day(sysdate,'월요일') from dual;

--입력한 기준으로 마지막 일을 알려줌
select last_day(sysdate) from dual;
select last_day('2024-02-01') from dual;



















 
 




 

































