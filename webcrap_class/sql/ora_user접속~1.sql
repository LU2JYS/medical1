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





-------------------------------------------------------------------------------
--24.04.24

--trunc 버림, round 반올림
select sysdate,hire_date,trunc(sysdate-hire_date,3) from employees;
select sysdate,hire_date,3,round(sysdate-hire_date) from employees;

---
select sysdate-1 어제,  sysdate+1 내일,sysdate 오늘 from dual;

--m_no시퀀스로 저장 1-9999씩증가
--퀴즈m_yesterday,m_today,m_tomorrow,m_year 날짜컬럼을 가진 테이블을 만들고 m_date
--어제 오늘 내일 1년후 날짜를 저장하시요

CREATE SEQUENCE seq_m_no
    INCREMENT BY 1
    START WITH 1
    MINVALUE 1
    MAXVALUE 9999
    NOCYCLE
    NOCACHE;

-- Create the table
CREATE TABLE m_date (
    m_no number(4),
    m_yesterday date,
    m_today date,
    m_tomorrow date,
    m_year date
    );

insert into m_date (m_no, m_yesterday,m_today,m_tomorrow,m_year) values 
    (seq_m_no.nextval,
     sysdate-1,
     sysdate,
     sysdate+1,
     sysdate+365
    );

select * from m_date;

--abs절대값 ceil,round,floor, trunc
select abs(hire_date-sysdate) from employees;

--날짜의 month기준으로 반올림한다.
select hire_date,round(hire_date,'month') from employees;

--날짜의 month기준으로 버림한다.
select hire_date,trunc(hire_date,'month'),round(hire_date,'month') from employees;

select trunc(hire_date,'month')기준일 ,hire_date from employees
order by hire_date;
select * from channels;

select period,count(period) from kor_loan_status
group by period
order by period;

select period from kor_loan_status
where period='201111';

select trunc(kor,-1)  t_kor,count(trunc(kor,-1)) from students
group by trunc(kor,-1)
order by t_kor;

--날짜의 month기준으로 버림한다.
select trunc(hire_date,'month') m_hire_date,count(trunc(hire_date,'month')) from employees
group by trunc(hire_date,'month')
order by m_hire_date
;

drop table students;
drop table stu_score;
drop table emp01;
drop table board;

select * from stu_score
order by no;

update stu_score set name='관순스'
where no=10;

select * from stu_score
order by no;

update stu_score set avg=(total/3)
;


--2개의 날짜에서 월 간격을 확인
select hire_date,floor(months_between(sysdate,hire_date)),trunc(sysdate-hire_date,2) from employees;

--개월 추가
select hire_date,add_months(hire_date,6) from employees;

--이달의 마지막날
select hire_date,last_day(hire_date),round(hire_date,'d') from employees;

--한요일의 12시 기준으로 
select sysdate,round(sysdate,'d') from employees;
select sysdate,trunc(sysdate,'j') from employees;
select sysdate,trunc(sysdate,'month') from employees;

-------------------------중요----------------------------------------

select sysdate 현재일,trunc(sysdate,'month') 처음일, last_day(sysdate) 마지막날 from dual;

--특정 요일의 날짜를 확인
select sysdate,next_day(sysdate,'토요일') from dual;

--요일의 처음일
  select sysdate,trunc(sysdate,'d'),next_day(sysdate,'토요일') from dual;  
  
  --board게시판 테이블 default는 입력시 없을시 지정한 데이터 자동 입력됨
  create table board(
    bno number(4) primary key,--중복이 안됨 기본키로 사용됨
    id varchar2(30),
    btitle varchar2(1000),
    bcontent clob, --bcontent varchar2(3000)-무제한 랑 같다
    bdate date default sysdate,
    bhit number default 0,
    bgroup number,
    bstep number default 0,
    bindent number default 0,
    bfile varchar2(100) --파일첨부
  );
  
insert into board values(
board_seq.nextval,'aaa','제목입니다','내용입니다',sysdate,0,board_seq.currval,0,0,'1.jpg');


insert into board (bno,id,btitle,bcontent,bgroup,bfile) values(
board_seq.nextval,'bbb','이벤트 시청','이벤트를 신청합니다',board_seq.currval,'2.jpg'
);

select * from board;



--형변환 -number타입 -character타입 -date타입

select sysdate from dual;
select sysdate ,to_char(sysdate,'yyyy-mm-dd') from dual;
select to_char(sysdate,'yyyy-mm-dd') from dual;
select to_char(sysdate,'yyyy') from dual;

--ko2024001
select 'Ko' || to_char(sysdate,'yyyy')||trim(to_char(seq_mno.nextval,'0000')) from dual;

select to_char(sysdate,'dy'
),to_char(sysdate,'day') from dual;

select to_char(sysdate,'yyyy-mm-dd mon day'
),to_char(sysdate,'day') from dual;

--hire_date, 연,월,일
select hire_date, to_char(hire_date,'yyyy-mm-dd mon day'
)from dual;

--am,pm 오전오후 24시간으로 표시
select to_char(sysdate,'pm hh24:mm:ss') from dual;

select * from stu_score;

select to_char(c_date,'yyyy-mm-dd hh:mm:ss day') from stu_score
order by c_date;

--날짜별로 몇개의 데이터가 들어가있는지 출력하시요

select c_date,count(c_date) from stu_score
group by c_date
order by c_date;

--데이터의 길이 함수
select length('안녕하세요') from dual;
select length(1234000) from dual;

--문자형 사칙연산안됨, 자리수표시,쉼표표시,날짜형태 표시
--숫자형 사직연산 가능 컴럼별 사칙연산, 자리수표시(0001>안됨),쉼표 표시 안됨.
--날짜형 +,- 연산기능가능,months-between 2개날짜 달 계산, 날짜유형을 지정해서 출력이 안됨.


--문자형안에 있는 데이터가 숫자이면 자동으로 형변화해서 계산해줌
--문자형 안에 문자가 있으면 자동변환 불가
 select 10 a, 100 b,(10+100) ab,to_char(100),10+to_char(300) from dual;
 select 10 a, 100 b,(10+100) ab,to_char(100),10+'100원' from dual;

--'0000'빈자리는 0으로 채움, '9999' 빈자리를 빈자리로 둠
select 12340000,to_char(12340000),length(to_char(12340000,'999,999,999')) from dual;

select length(12340000),to_char(12340000),length(to_char(12340000,'999,999,999')) from dual;

--L은 원화표시
select 12340000,to_char(12340000,'L999,999,999') from dual;
--$은 $달러표시
select 12340000,to_char(12340000,'$999,999,999') from dual;
--소수점 자리 표시
select 1234.1234,to_char(1234.1234,'000,999.99') from dual;

--10개자리수 표시
--공백제거해서 자리수 확인 >>>>>>>>>> trim적용시
select length(trim(to_char(12345,'0000000000'))),length(trim(to_char(12345,'999,999'))) from dual;


--퀴즈
--123,456,789 + 100,000 =값을 출력 천단위로
--123,556,789
SELECT TO_CHAR(
           TO_NUMBER(REPLACE('123,456,789', ',', '')) + 
           TO_NUMBER(REPLACE('100,000', ',', ''))
           , 'L999,999,999') AS result
FROM dual;

select to_number('0000123') from dual;


--날짜 차이값 만들기
select '2024-04-24'-'2024-04-01' from dual;
select to_date('2024-04-24')-to_date('2024-04-01') from dual;

select to_date('20240424') from dual;
select to_char(to_date('20240424'),'yyyy-mm-dd hh:mm:ss') as 날짜 from dual;

select hire_date from employees;
where hire_date = '2008/01/01';
select * from stu_score;
select c_date from stu_score
where c_date ='2024/04/05';


select sysdate-hire_date from employees;

--퀴즈
SELECT TO_CHAR(
           TO_NUMBER('20,000','99,999') - TO_NUMBER('10,000','99,999')
           ,'99,999') AS result
FROM dual;

--퀴즈
select commission_pct from employees;

--실제월급=월급+(월급*커미션) 실제월급해서 출력하시요
select salary,salary+(salary*nvl(commission_pct,0)) from employees;

select emp_name,commission_pct from employees
where commission_pct is null  ;


--퀴즈 manager_id null이면 0 nvl(데이터,0)
select nvl(manager_id,0) from employees
order by manager_id desc;

--null값을 ceo로 대체해서 넣어라
--문자형은 to_char를 쓴다
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;




-------------------------------------------------------------------------------
--24.04.25

-----------------중요 중요-----------------------------------------
--어제 오늘 내일
select sysdate-1, sysdate, sysdate+1 from dual;

--달에 있는 첫번째 일
select sysdate, trunc(sysdate,'month'),last_day(sysdate) from dual;

--두날짜간 일수
select round(sysdate-hire_date,3),trunc(months_between(sysdate,hire_date),2) from employees;

--trunc 일단위 버림(십단위로 출력)
select trunc(kor,-1) kor,count(trunc(kor,-1))  from stu_score
group by trunc(kor,-1)
order by kor;

--hire_date에서  월만 출력하시요

select to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(hire_date,'mm') from employees;

select to_char(hire_date,'mm') hire_date,count(to_char(hire_date,'mm')) from employees
group by to_char(hire_date,'mm')
order by hire_date;

--퀴즈, hire_date yyyy년도 년도별 인원수를 출력하시요

select to_char(hire_date,'yyyy') hire_date,count(to_char(hire_date,'yyyy')) from employees
group by to_char(hire_date,'yyyy')
order by hire_date;



--  형변환 -number, character, date
--  number 사칙연산 가능 ,쉼표표시안됨,원화표시
--  char 사직연산(+,-)안됨, 쉼표 표시가능, 원화표시가능
--  date +,- 가능 날짜출력형태는 변경 불가


-------------------------------중요 중요-----------------------------------------
--시퀀스,날짜의 년도를 가지고 학번을 부여하시요.
--stu_seq시퀀스를 가지고 5개 학번을 출력
--ko+2024+0001
create sequence stu_seq
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache
;

--trim() 공백제거 자동으로 번호 생성
select 'ko' || to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000'))as stu_no from dual;

SELECT TO_CHAR(
           TO_NUMBER(REPLACE('123,456,789', ',','')) + 
           TO_NUMBER(REPLACE('100,000', ',',''))
           , '999,999,999') AS result
FROM dual;

--숫자형태를 날짜타입으로 변경
select 20240425+3 from dual;
select to_char(20240425+3) from dual;
select to_date(20240425+3) from dual;


--숫자타입을 날짜 타입으로 변경
select emp_name,hire_date from employees
where hire_date > to_date(20070101)
order by hire_date;


--퀴즈
--8월에만 입사한,사원이름 2번째 a 가 들어간 사람 출력
select hire_date from employees
where to_char(hire_date,'mm')='01'or to_char(hire_date,'mm')='05' or to_char(hire_date,'mm')='08'
order by  hire_date ;




--사원이름 2번재에 a가 들어있는 사람을 출력하시요 2017년 이후로 출력
select emp_name,hire_date from employees
where hire_date > to_date(20070101)
and emp_name like '_a%'
order by hire_date;

select sysdate-to_date('20240401') from dual;

select * from m_date;

insert into m_date(m_no,m_yesterday) values(
seq_mno.nextval,'2024-04-01'
);

create table eventDate(
eno number,
e_today date,
e_choice_day date,
e_period number
);

--입력시 날짜타입에 문자를 입력해도 저장됨
--날짜와 문자를 빼기는 불가능, 그래서 문자를 날짜타입으로 변경해야함 
insert into eventDate values(
seq_mno.nextval,sysdate,'2024-04-01',sysdate-to_date('2024-04-01')
);

select * from eventDate;

select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

select salary,salary+(salary*nvl(commission_pct,0)) from employees;

select manager_id from employees
order by manager_id desc;

--숫자타입이 문자타입으로 변경
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;


--그룹함수 : sum,avg,count(),count(*),min,max


--그룹함수 count
select count * from employees;

select count(emp_name) from employees;

select count(manager_id) from employees;

select emp_name,manager_id from employees;


--sum :총합
select sum(salary) from employees;

--avg : 평균
select avg(salary) avg_sal from employees;

--min : 최소값
select min(salary) from employees;

--max : 최대값
select max(salary) from employees;



--퀴즈 6461달러보다 높은사람을 출력하시요 <<이중쿼리>>
select * from employees
where salary > (select avg(salary) avg_sal from employees);

select min (salary) from employees;

--최소월급 받는사람의 사번,이름을 출력하시요
select employee_id ,emp_name,salary from employees
where salary=(select min (salary) from employees);

--최대월급 받는사람의 사번,이름을 출력하시요
select employee_id ,emp_name,salary from employees
where salary=(select max (salary) from employees);

--부서 번호가 50번인 사원만 전체 월급
select department_id,salary from employees;

select sum(salary) from employees
where department_id= 50;

select count (*) from stu_score;

--퀴즈 kor점수가 80점이상인 사람만 출력하시요
select kor from stu_score
where kor >= 80;

--국어점수 평균이상, 영어점수 평균 이상만 출력하시요
select name,kor,eng from stu_score
where kor >= (select avg(kor) avg_kor from stu_score) and
eng >= (select avg(eng) avg_eng from stu_score);


create table s_info(
sno number,
s_count number
);

insert into s_info values(
stu_seq.nextval,1000);

insert into s_info values(
stu_seq.nextval,(select count(*) from stu_score
where kor >= (select avg(kor) avg_kor from stu_score) and
eng >= (select avg(eng) avg_eng from stu_score)));

select * from s_info;

--퀴즈
--월급이 최대인 사람과 최소인 사람 출력

select  emp_name,salary from employees
where salary=(select min (salary) from employees)
or salary=(select max (salary) from employees)
or salary=(select avg (salary) from employees);


--최대값
select emp_name,salary from employees
where salary=(select max(salary) from employees);


--이게 하나의 테이블로 생각한다
--평균보다 작은값
select emp_name,salary from employees
where salary >= (select avg(salary) from employees)
order by salary;


--평균보다 작은 사원중에 최대값인 사원을 출력하시요
select emp_name from employees
where salary = 6400;

SELECT emp_name, salary 
FROM employees 
WHERE salary = (
    SELECT MAX(salary) 
    FROM (
        SELECT emp_name, salary 
        FROM employees 
        WHERE salary >= (SELECT AVG(salary) FROM employees)
        ORDER BY salary DESC
    )
);

--문자함수
--lpad,rpad빈 공백 채우기
select emp_name,lpad(emp_name,15,'#')from employees;
select emp_name,rpad(emp_name,50,'@')from employees;


-- ltrim,rtrim 특정 지정 문자를 잘라내고 출력
select emp_name,ltrim(emp_name,'Do') from employees;



--ko20240001
select 'ko20240001', ltrim('ko20240001','ko2024') from dual;

--substr(데이터,순서,개수)
select emp_name,substr(emp_name,3,4) from employees;

select job_id from employees;

--퀴즈.  job_id에 있는 앞에 sh와 사원번호를 겹합해서 출력시키시요
select  substr(job_id,0,2)|| employee_id  from employees;

--length
select emp_name,length(emp_name) from employees
where length(emp_name)>15;

--날짜끼리 빼는건 된다.
select sysdate-hire_date from employees;

--날짜끼리 더하는건 안된다.
select sysdate+hire_date from employees;

--다음달의 첫째날
select round(sysdate,'month') from dual;

select round(sysdate,'year') from dual;

--원하는 달로 이동
select sysdate,add_months(sysdate,-2) from dual;


--ceil나머지 floor버림 mod나머지 power제곱
select ceil(-4.2),floor(-4.2),mod(8,3),power(2,10) from dual;

select emp_name || to_char(hire_date,' yyyy "년" mm "월"dd "일"') from employees;

----------------------------퀴즈 사원명 월급*1400원 앞에 원화 표시와 쉼표를 넣어 출력
select salary,to_char(salary*1400,'L000,000,000') from employees;

--자신의 생일과 자신의 생일이 속한 달의 마지막날짜

select trunc(to_date('2010-10-10'),'month'),'2010-10-10' ,last_day('2010-10-01') from dual;



select  * from member;

desc member;

alter table member drop column phone;


--ddl(data) 컬럼 추가해주기
--위에있는 ddl은 커밋,롤백이 없다
alter table member add gender varchar2(6) default 'Female' not null;
select  * from member;

update member set gender='male';

commit;

--컬럼수정 : 이름변경
alter table member rename column name to stu_name
;

--컬럼수정 : 타입변경
alter table member modify(stu_name varchar2(50));

--기존의 데이터가 변경하려는 크기보다 작을때만 가능
update member set stu_name='';
alter table member modify(stu_name varchar2(6));

alter table member modify(stu_name varchar2(4));
desc member;
select stu_name from member;

--자리수 초과 오류
alter table member modify(stu_name number(100));
desc member;

select  * from member;
































 
 




 

































