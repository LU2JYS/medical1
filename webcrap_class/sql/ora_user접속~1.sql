select * from employees;
-- ȸ������ ���̺� ����
create table member (
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);
-- ������ �Է�
insert into member (id,pw,name,phone) values (
'aaa','1111','ȫ�浿','010-1111-1111'
);
insert into member values (
'bbb','1111','������','010-2222-2222'
);
insert into member (id,name,phone) values(
'ccc','�̼���','010-3333-3333'
);
-- �÷��� ���� ����
/*
insert into member values (
'ddd','������','010-4444-4444'
);
*/
select id,pw,name,phone from member;
commit;
rollback;
select id,name from member;
select * from member;
insert into member values(
'ddd','1111','������','010-4444-4444'
);
select * from member;
rollback;
commit;
select * from member;
update member set pw='2222' where id='ccc' ;
select * from member;
rollback;
-- ��� ���̺� Ȯ��
select * from tab;
-- ���̺��� Ÿ�� Ȯ��
desc member;
-- ����Ŭ Ÿ��
-- number-����,date-��¥,char-��������,varchar2-��������,clob-��뷮����
-- number : ����,�Ǽ�
-- number(4) : -9999~9999
create table mem (
no number, -- ���� �������� ����.
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
 mdate2 timestamp --date : ��,��,��,��,��,�ʱ��� ���尡�� / timestamp �и��ʱ��� ���尡����.
);
insert into mem2 (mdate) values ('2024-04-19' );
insert into mem2 (mdate) values (sysdate); --sysdate:����ð�
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
-- char : ��������
insert into mem3 (tel) values ('11112222');
insert into mem3 (tel) values ('22223333');
insert into mem3 (tel) values ('111');
insert into mem3 (tel) values ('123456789');
insert into mem3(tel) values ('ȫ');
-- varchar2 : ��������
insert into mem3 (name) values ('11112222');
insert into mem3 (name) values ('ȫ�浿'); --�ѱ� :3ũ��
insert into mem3 (name) values ('�Ż��Ӵ�'); -- 12�ڸ� �ʿ�
INSERT INTO MEM3 (NAME) VALUES ('AAA');
insert into mem3 (name) values ('aaa');
commit;
select * from mem3 where name='aaa'; -- sql������ ��ҹ��� ���о���, �����ʹ� ��ҹ��� ������.
select * from mem3 where name='AAA';
select * from mem3 where lower(name)='aaa';
-- select,from 2���� Ű����� ���� ��.
-- * ��� �÷��� ���
-- ��ҹ��ڸ� �������� ����.
select * from mem;
SELECT * FROM MEM;
select emp_name,department_id from employees;
-- distinct ���� ���� 1���� ���
select distinct department_id from employees;
select * from departments;
select * from employees;
select * from mem3;
select no,mdate2,tel,name,mdate from mem3;
select * from employees;
-- �����ȣ(e id), ����̸�(e name),�޿�(salary), �Ի�����(hire_date)
select employee_id,emp_name,salary,hire_date from employees;
desc employees;
select * from stu_score;
-- ���̺� ����
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
1,'ȫ�浿',100,100,100,300,100,1
);
insert into stu_score values (
5,'�豸',100,100,100,300,100,1
);
commit;
select * from stu_score;



--��������� numberŸ���� ���

select  * from stu_score;
insert into stu_score values(
6,'������',100,95,96,(100+95+96),(100+95+96)/3,1
);

select  * from stu_score;

insert into stu_score values(
7,'ȫ����',100,100,99,(100+100+99),(100+100+99)/3,1
);

select  * from stu_score;

--��ȣ, �̸�,��������,����������-20,���,���-20�� ��,����������-20�� ���
select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score;

select  * from employees;
 --�޷� ��ȭ ȯ�� - 1381.79��=1�޷�


select employee_id,emp_name,salary*1381.79 from employees;

--���� *12 = ����
select * from employees;
select employee_id,emp_name,salary*12,salary*1381.79*12 from employees; --����(�޷�����),--����(������)


--Ŀ�̼��� �������� = ���� + ����*Ŀ�̼�
--commission_pct
select * from employees;

select employee_id,emp_name,salary+(salary*commission_pct) from employees;

--nvl(�÷�,0)���� ���������
select employee_id,emp_name,nvl(commission_pct,0),salary+(salary*nvl(commission_pct,0)) from employees;

commit;









-------------------------------------------------------------------------------
--24.04.22

select * from employees;

select employee_id,emp_name from employees;

select salary from employees;

-- Ÿ�� : number +,-,*,/ ����
select salary, salary * 1400 k_sal,salary*1400*12 as y_sal from employees;

select * from stu_score;

select no,name,kor,eng,math,total,avg,rank from stu_score;

-- ���̽�.

select department_id from employees;

select nvl(department_id,0) from employees;

select * from employees;

-- ��Ī : as���, "" : Ű���带 �ִ� �״�� ���
select salary, salary + (salary*nvl(commission_pct,0)) as "real_sal*" from employees;

-- �ѱ� ��밡��
select salary as "���" from employees;

-- 

select * from departments;

-- �μ���ȣ, �μ��̸��� ����Ͻÿ�.
select department_id,department_name from departments;

-- �������� �����͸� 1���� ���ļ� �Ѱܾ� �� ��� concat
-- concat : ȫ�浿,������,�̼���,������,�豸 -> split(",") : �и� 

select * from stu_score;

-- concat ||
select kor||','||eng||','||math stu from stu_score;

select kor+eng+math as total,(kor+eng+math)/3 from stu_score;

-- �ߺ����� : distinct
-- where : ������ not �����ϰ� �˻��Ϸ��� is not null
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

-- department_id 10,30,50�� �ش�Ǵ� ����� ����Ͻÿ�.
select employee_id,department_id,salary from employees
where department_id = 10 or department_id = 30 or department_id = 50;

-- ���� 6000 ~ 9000 ������ ����� ����Ͻÿ�.
-- ���� order by �÷� asc : ��������,desc : ��������
select salary from employees where salary>=6000 and salary<=9000
order by salary desc
;
-- ���� 6000,7000,8000 �� ����� ����Ͻÿ�.
select salary from employees
where salary =6000 or salary=7000 or salary = 8000;

-- �μ���ȣ�� 50���̸鼭, ������ 8000 �̻��� ����� ����Ͻÿ�.
select department_id,salary from employees
where department_id=50 and salary >= 8000;

-- stu_score ȫ�浿 ����Ͻÿ�.
select * from stu_score
where name = 'ȫ�浿';

-- ��������
select hire_date from employees
order by hire_date asc
;
-- ��������
select hire_date from employees
order by hire_date desc
;

select emp_name,hire_date from employees
where hire_date >= '02/01/01'
order by hire_date asc
;

select hire_date,hire_date+100 from employees;
-- �ݿø� round
select round(sysdate-hire_date,2) from employees;

select * from employees;

-- ������ġ��� +������ �Ұ���, ||��ɾ� ���
select emp_name||email from employees;

-- �Ի��� 05�� �̻� 06�� �����̸鼭 ������ 6000 �޷� �̻��� ����� �Ի��� �������ķ� ����Ͻÿ�.
select emp_name,hire_date,salary from employees
where hire_date >= '05/01/01' and hire_date <= '06/12/31' and salary >=6000
order by hire_date desc
;

-- !=, <>,^=, not
select department_id from employees
where department_id != 10 and not department_id = 50
order by department_id
;

-- salary 5000 �̻� 9000 ����
select emp_name,salary from employees
where salary >= 5000 and salary <= 9000
order by salary
;

-- ����� 99�� �̻��� �л��� �˻��Ͻÿ�.
select * from stu_score
where avg>=99
;

select * from students;

update students set name='������' 
where no = 10
;

commit;

select * from students;

-- students
-- ��� 70, ��� 75�� �̻��� �л��� ����Ͻÿ�.
select name,kor,avg from students
where kor>=70 and avg>=75
;

-- �������� 80, �������� 70, �������� 90 �� �л��� ����Ͻÿ�.
select name,kor from students
where kor=80 or kor = 70 or kor = 90;

-- in ���� ������ �ʵ尡 �������� �� �߿� �ϳ��� �˻��� ���
select name,kor from students
where kor in(80,70,90);

select name,kor from students
where kor not in(80,70,90);


update students set kor=100 
where no=1;

rollback;

select * from students
where no = 1;

-- ����
update students set kor=100, total = 100+eng+math, avg = (100+eng+math)/3
where no=1;


-- �������� 70 ~ 90 �̻� �л��� ����Ͻÿ�.
select kor from students
where kor > 70 and kor <= 90
;

-- 100��
select * from students;

-- 27�� between a and b : a���� ũ�ų� ���� b���� �۰ų� ���� �� �˻�
select kor from students
where kor between 70 and 90
;

-- 73�� not between a and b : a���� ũ�ų� , b���� ������ �˻�
select kor from students
where kor not between 70 and 90
;

-- ��¥�� between a and b

select hire_date from employees
order by hire_date;

-- �Ի��� 99�⺸�� ũ�ų� ����, 01�� ���� �۰ų� ���� ��� �˻�
select hire_date from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date asc
;

-- �̸��˻�
select * from students
where name='ȫ�浿'
;

-- like �˻� : Ư���ܾ ���ԵǾ� �ִ� ���� �˻�
-- ȫ% : ȫ���� ���۵Ǵ� �ܾ� �˻�
select * from students
where name like 'ȫ%'
;

-- %�� : ������ ������ �ܾ� �˻� 
select * from students
where name like '%��'
;

-- %��% : Ư���ܾ ���ԵǾ� �ִ� �ܾ� �˻�
select * from students
where name like '%��%'
;

-- _ : �� ĭ ������ ���, �� �տ� 1���� �ܾ �����鼭 ���� ���ԵǾ� �ִ� �ܾ� �˻�
select * from students
where name like '_��%'
;


select * from students;

-- 3��°�� t�� �� �ִ� �̸� �˻�
-- __t
select * from students
where name like '__t%'
;

-- �̸��� 4�ڸ���, 3��° r�� �� �ִ� �̸� �˻�
select * from students
where name like '__r_'
;

select * from students
where name like '__r%' and length(name) = 4
;

-- �̸� ���̰� 4�ڸ� �ΰ� �˻�
select name from students
where length(name) = 4
;

-- �̸��� A�� ���۵Ǵ� �л� �˻�
select no,name from students
where name like 'A%'
;

-- �̸��� a�� �� �ִ� �л� �˻�
select no,name from students
where name like '%a%'
;

-- ��ҹ��� ���о��� a�� �� �ִ� �л� �˻�
-- �ҹ��� ��ȯ(lower), �빮�� ��ȯ (upper), ù���� �빮�� (initcap)
select no,name from students
where lower(name) like '%a%'
;

-- a�� ���Ե��� ���� �̸��� �˻�
select no,name from students
where lower(name) not like '%a%'
;


select manager_id from employees;

-- manager_id 100�� ��� �˻�
select employee_id,emp_name,manager_id from employees
where manager_id = 100
;

-- null �� ��񱳰� �ȵ�.
select employee_id,emp_name,managaer_id from employees
where manager_id = null
;

-- null���� is null ��ɾ� ���
select employee_id,emp_name,manager_id from employees
where manager_id is null
;

select * from employees
where manager_id is not null
;

select * from stu_score;

-- �ѱ� ���� ����
select * from stu_score
order by name asc
;


select * from students;


-- 1�� ���������� �������� �� ����, ���� ������ ���, ���������� �������� ����
select * from students
order by kor desc, eng asc
;

-- total�� ��������

select * from students
order by total desc
;

-- �÷��߰�
alter table students add rank number(3);

-- �÷�Ÿ��
desc students;

select * from students;

update students set rank=0;

commit;

-- ���
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




-- ����
update students set rank = 13
where no = 1
;

select * from students
where kor>=70;


select * from (���̺�);


select * from (select * from students where avg>=80)
where kor>=70
;

-------------------------------------------------------------------------------
--24.04.23

--select * from students;
--���̺� �÷��߰�
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

--1.update����
update students a set rank= (rank);

--2. no,rank()����
(select no,rank() over (oeder by total desc) ranks from students) b;

--3.update���� rank()������ no�÷����� ��, rank�÷��� �˻�
update students a set rank= (
 select ranks from (students) b
  where a.no = b.no
  );

update students a set rank= ( 
 select ranks from (select no,rank() over (oeder by total desc) ranks from students) b
 where a.no = b.no);
 
 --��������
 select no,total,rank from students
 order by total desc;
 
 --no��������
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
  
--����1
--�Ի����� ������������!!,
--�÷��� �����ȣ,�����,job_id-����,�Ի���,���� �÷��� ����Ͻÿ�.
select employee_id,emp_name,job_id,hire_date,salary  
from employees
order by hire_date desc;

--����2
--�޿��� ���Թ޴� ��������� ����ϵ� ������ ������, ��������� ���������Ͻÿ�
select emp_name,salary  
from employees
order by  emp_name,salary desc;


--�����Լ�
--abs(������ ����� ���´�)
--round(�ݿø�)
--floor(�Ҽ��� ������)

select -10, abs(-10) from dual;

select 34.789, floor(34.789) as f,round(34.789)as r from dual;

select 34.178, round(34.178), round(34.178,2) from dual; --����� �Ҽ����ݿø� ��ġ�� ��������

--------------------------------�߿�---------------------------------------
select avg from students;
select round(avg,2) avg from students; --�Ҽ��� 2°�ڸ�������!!

select 34.5678, round(34.5678,-1) from dual;

--trunc ���� �ڸ��� ���� ������
select trunc(34.5678,2) trunc from dual;
select trunc(34.5678) trunc from dual;

--������ �ø� �Ҽ�������
select ceil (34.1278) from dual;

--�������� �ϴ��� �����ؼ� ����Ͻÿ�(�ʴ����� ���)
select trunc(kor,-1) from students
order by kor;

--����,����,���� �ϴ��������ؼ� ���� ����Ͻÿ�
SELECT trunc(kor, -1) AS ����, 
       trunc(eng, -1) AS ����, 
       trunc(math, -1) AS ����, 
       trunc(kor, -1)+trunc(eng, -1)+trunc(math, -1) as �հ�
FROM students;

--mod ������
select round(100/7,2) from dual;
select mod(10,7) as ������ from dual;

--������
select 10/7 as ������ from dual;

--����. �����ȣ�� ¦���ΰ��� ����Ͻÿ�!!
SELECT employee_id  from employees WHERE mod(employee_id,2) = 0;

--��
select floor(10/7) from dual;

--�������� 0�̸� ¦��,3�̸� Ȧ��
select mod(10,7) from dual;

--���� �й� 3�� ����ΰ͸� ã������ students���̺�
select no from students
where mod(no,3)=0;

----6��(������)----

create sequence seq_no
increment by 1 --������ 1������
start with 1 --������ 1���� ����
minvalue 1 --�ּҰ� 1
maxvalue 9999 --�ִ밪 9999
nocycle --��ȯ���� ����
nocache; --ĳ���� ������� ����

--nextval ������ ��ȣ 1�� ����
select seq_no.nextval from dual;

--currval ������ ��ȣ Ȯ��
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
seq_mno.nextval,'ccc','1111','�̼���','010-3333-3333'

);

select * from member;

--�ѱ����б� ko�� �ϰ� 24�й��� ko20240001������ ���


select sysdate from dual;
select to_char(sysdate,'yyyy') from dual;

select 's0001' || to_char(seq_mno.currval) from dual; 

--�ѱ����б� ko�� �ϰ� 24�й��� ko20240001������ ���

create sequence seq_ko
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache
;

--trim() �������� �ڵ����� ��ȣ ����
select 'ko' || to_char(sysdate,'yyyy')||trim(to_char(seq_ko.nextval,'00000'))as stu_no from dual;

--�Խ��� 
create table board(
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10)
);

commit;

--����
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


--���ο� ������ ����--
create sequence emp_seq
    increment by 1
    start with 1
    minvalue 1
    maxvalue 9999
    nocycle
    nocache
    ;
    
    --������ ����--
    alter sequence emp_seq
    increment by 1001;
    
insert into emp01 values(
emp_seq.nextval, '�̼���',sysdate
);

select * from emp01;

commit;

--������� �Ի��� �ϼ��� ����Ͻÿ�. �ݿø��ϼ���

select employee_id,emp_name,job_id,hire_date,ceil(sysdate-hire_date)||'��'  
from employees
order by hire_date desc;

select emp_name from employees;

--����
--���ް� ����� ���ļ� ����Ͻÿ�.
select employee_id||job_id 
from employees;

select substr(job_id,0,2) from employees;
select emp_name ,substr(emp_name,1,3) from employees;

-- substr�� ���ڿ� �ڸ���(2��°���� 3���� ©��Ͷ�) substr(���,������ġ,����)
select substr('abcde',2,3) from dual;

--����
select substr(job_id,0,2)|| trim(to_char(employee_id,'00000')) as ���̷� from employees;


--��¥�Լ�
select sysdate from dual;

select to_char(sysdate,'yyyy-mm--dd hh24:mm:ss')from dual;

--�γ�¥ ������ ������ Ȯ��
select MONTHS_BETWEEN(SYSDATE,hire_date),sysdate-hire_date from employees;

--�������� �߰�
select sysdate, add_months(sysdate,2) from dual;

--���ñ������� ������ ���� ��¥�� �˷��ش�.
select next_day(sysdate,'������') from dual;

--�Է��� �������� ������ ���� �˷���
select last_day(sysdate) from dual;
select last_day('2024-02-01') from dual;





-------------------------------------------------------------------------------
--24.04.24

--trunc ����, round �ݿø�
select sysdate,hire_date,trunc(sysdate-hire_date,3) from employees;
select sysdate,hire_date,3,round(sysdate-hire_date) from employees;

---
select sysdate-1 ����,  sysdate+1 ����,sysdate ���� from dual;

--m_no�������� ���� 1-9999������
--����m_yesterday,m_today,m_tomorrow,m_year ��¥�÷��� ���� ���̺��� ����� m_date
--���� ���� ���� 1���� ��¥�� �����Ͻÿ�

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

--abs���밪 ceil,round,floor, trunc
select abs(hire_date-sysdate) from employees;

--��¥�� month�������� �ݿø��Ѵ�.
select hire_date,round(hire_date,'month') from employees;

--��¥�� month�������� �����Ѵ�.
select hire_date,trunc(hire_date,'month'),round(hire_date,'month') from employees;

select trunc(hire_date,'month')������ ,hire_date from employees
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

--��¥�� month�������� �����Ѵ�.
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

update stu_score set name='������'
where no=10;

select * from stu_score
order by no;

update stu_score set avg=(total/3)
;


--2���� ��¥���� �� ������ Ȯ��
select hire_date,floor(months_between(sysdate,hire_date)),trunc(sysdate-hire_date,2) from employees;

--���� �߰�
select hire_date,add_months(hire_date,6) from employees;

--�̴��� ��������
select hire_date,last_day(hire_date),round(hire_date,'d') from employees;

--�ѿ����� 12�� �������� 
select sysdate,round(sysdate,'d') from employees;
select sysdate,trunc(sysdate,'j') from employees;
select sysdate,trunc(sysdate,'month') from employees;

-------------------------�߿�----------------------------------------

select sysdate ������,trunc(sysdate,'month') ó����, last_day(sysdate) �������� from dual;

--Ư�� ������ ��¥�� Ȯ��
select sysdate,next_day(sysdate,'�����') from dual;

--������ ó����
  select sysdate,trunc(sysdate,'d'),next_day(sysdate,'�����') from dual;  
  
  --board�Խ��� ���̺� default�� �Է½� ������ ������ ������ �ڵ� �Էµ�
  create table board(
    bno number(4) primary key,--�ߺ��� �ȵ� �⺻Ű�� ����
    id varchar2(30),
    btitle varchar2(1000),
    bcontent clob, --bcontent varchar2(3000)-������ �� ����
    bdate date default sysdate,
    bhit number default 0,
    bgroup number,
    bstep number default 0,
    bindent number default 0,
    bfile varchar2(100) --����÷��
  );
  
insert into board values(
board_seq.nextval,'aaa','�����Դϴ�','�����Դϴ�',sysdate,0,board_seq.currval,0,0,'1.jpg');


insert into board (bno,id,btitle,bcontent,bgroup,bfile) values(
board_seq.nextval,'bbb','�̺�Ʈ ��û','�̺�Ʈ�� ��û�մϴ�',board_seq.currval,'2.jpg'
);

select * from board;



--����ȯ -numberŸ�� -characterŸ�� -dateŸ��

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

--hire_date, ��,��,��
select hire_date, to_char(hire_date,'yyyy-mm-dd mon day'
)from dual;

--am,pm �������� 24�ð����� ǥ��
select to_char(sysdate,'pm hh24:mm:ss') from dual;

select * from stu_score;

select to_char(c_date,'yyyy-mm-dd hh:mm:ss day') from stu_score
order by c_date;

--��¥���� ��� �����Ͱ� ���ִ��� ����Ͻÿ�

select c_date,count(c_date) from stu_score
group by c_date
order by c_date;

--�������� ���� �Լ�
select length('�ȳ��ϼ���') from dual;
select length(1234000) from dual;

--������ ��Ģ����ȵ�, �ڸ���ǥ��,��ǥǥ��,��¥���� ǥ��
--������ �������� ���� �ķ��� ��Ģ����, �ڸ���ǥ��(0001>�ȵ�),��ǥ ǥ�� �ȵ�.
--��¥�� +,- �����ɰ���,months-between 2����¥ �� ���, ��¥������ �����ؼ� ����� �ȵ�.


--�������ȿ� �ִ� �����Ͱ� �����̸� �ڵ����� ����ȭ�ؼ� �������
--������ �ȿ� ���ڰ� ������ �ڵ���ȯ �Ұ�
 select 10 a, 100 b,(10+100) ab,to_char(100),10+to_char(300) from dual;
 select 10 a, 100 b,(10+100) ab,to_char(100),10+'100��' from dual;

--'0000'���ڸ��� 0���� ä��, '9999' ���ڸ��� ���ڸ��� ��
select 12340000,to_char(12340000),length(to_char(12340000,'999,999,999')) from dual;

select length(12340000),to_char(12340000),length(to_char(12340000,'999,999,999')) from dual;

--L�� ��ȭǥ��
select 12340000,to_char(12340000,'L999,999,999') from dual;
--$�� $�޷�ǥ��
select 12340000,to_char(12340000,'$999,999,999') from dual;
--�Ҽ��� �ڸ� ǥ��
select 1234.1234,to_char(1234.1234,'000,999.99') from dual;

--10���ڸ��� ǥ��
--���������ؼ� �ڸ��� Ȯ�� >>>>>>>>>> trim�����
select length(trim(to_char(12345,'0000000000'))),length(trim(to_char(12345,'999,999'))) from dual;


--����
--123,456,789 + 100,000 =���� ��� õ������
--123,556,789
SELECT TO_CHAR(
           TO_NUMBER(REPLACE('123,456,789', ',', '')) + 
           TO_NUMBER(REPLACE('100,000', ',', ''))
           , 'L999,999,999') AS result
FROM dual;

select to_number('0000123') from dual;


--��¥ ���̰� �����
select '2024-04-24'-'2024-04-01' from dual;
select to_date('2024-04-24')-to_date('2024-04-01') from dual;

select to_date('20240424') from dual;
select to_char(to_date('20240424'),'yyyy-mm-dd hh:mm:ss') as ��¥ from dual;

select hire_date from employees;
where hire_date = '2008/01/01';
select * from stu_score;
select c_date from stu_score
where c_date ='2024/04/05';


select sysdate-hire_date from employees;

--����
SELECT TO_CHAR(
           TO_NUMBER('20,000','99,999') - TO_NUMBER('10,000','99,999')
           ,'99,999') AS result
FROM dual;

--����
select commission_pct from employees;

--��������=����+(����*Ŀ�̼�) ���������ؼ� ����Ͻÿ�
select salary,salary+(salary*nvl(commission_pct,0)) from employees;

select emp_name,commission_pct from employees
where commission_pct is null  ;


--���� manager_id null�̸� 0 nvl(������,0)
select nvl(manager_id,0) from employees
order by manager_id desc;

--null���� ceo�� ��ü�ؼ� �־��
--�������� to_char�� ����
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;




-------------------------------------------------------------------------------
--24.04.25

-----------------�߿� �߿�-----------------------------------------
--���� ���� ����
select sysdate-1, sysdate, sysdate+1 from dual;

--�޿� �ִ� ù��° ��
select sysdate, trunc(sysdate,'month'),last_day(sysdate) from dual;

--�γ�¥�� �ϼ�
select round(sysdate-hire_date,3),trunc(months_between(sysdate,hire_date),2) from employees;

--trunc �ϴ��� ����(�ʴ����� ���)
select trunc(kor,-1) kor,count(trunc(kor,-1))  from stu_score
group by trunc(kor,-1)
order by kor;

--hire_date����  ���� ����Ͻÿ�

select to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(hire_date,'mm') from employees;

select to_char(hire_date,'mm') hire_date,count(to_char(hire_date,'mm')) from employees
group by to_char(hire_date,'mm')
order by hire_date;

--����, hire_date yyyy�⵵ �⵵�� �ο����� ����Ͻÿ�

select to_char(hire_date,'yyyy') hire_date,count(to_char(hire_date,'yyyy')) from employees
group by to_char(hire_date,'yyyy')
order by hire_date;



--  ����ȯ -number, character, date
--  number ��Ģ���� ���� ,��ǥǥ�þȵ�,��ȭǥ��
--  char ��������(+,-)�ȵ�, ��ǥ ǥ�ð���, ��ȭǥ�ð���
--  date +,- ���� ��¥������´� ���� �Ұ�


-------------------------------�߿� �߿�-----------------------------------------
--������,��¥�� �⵵�� ������ �й��� �ο��Ͻÿ�.
--stu_seq�������� ������ 5�� �й��� ���
--ko+2024+0001
create sequence stu_seq
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache
;

--trim() �������� �ڵ����� ��ȣ ����
select 'ko' || to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000'))as stu_no from dual;

SELECT TO_CHAR(
           TO_NUMBER(REPLACE('123,456,789', ',','')) + 
           TO_NUMBER(REPLACE('100,000', ',',''))
           , '999,999,999') AS result
FROM dual;

--�������¸� ��¥Ÿ������ ����
select 20240425+3 from dual;
select to_char(20240425+3) from dual;
select to_date(20240425+3) from dual;


--����Ÿ���� ��¥ Ÿ������ ����
select emp_name,hire_date from employees
where hire_date > to_date(20070101)
order by hire_date;


--����
--8������ �Ի���,����̸� 2��° a �� �� ��� ���
select hire_date from employees
where to_char(hire_date,'mm')='01'or to_char(hire_date,'mm')='05' or to_char(hire_date,'mm')='08'
order by  hire_date ;




--����̸� 2���翡 a�� ����ִ� ����� ����Ͻÿ� 2017�� ���ķ� ���
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

--�Է½� ��¥Ÿ�Կ� ���ڸ� �Է��ص� �����
--��¥�� ���ڸ� ����� �Ұ���, �׷��� ���ڸ� ��¥Ÿ������ �����ؾ��� 
insert into eventDate values(
seq_mno.nextval,sysdate,'2024-04-01',sysdate-to_date('2024-04-01')
);

select * from eventDate;

select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

select salary,salary+(salary*nvl(commission_pct,0)) from employees;

select manager_id from employees
order by manager_id desc;

--����Ÿ���� ����Ÿ������ ����
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;


--�׷��Լ� : sum,avg,count(),count(*),min,max


--�׷��Լ� count
select count * from employees;

select count(emp_name) from employees;

select count(manager_id) from employees;

select emp_name,manager_id from employees;


--sum :����
select sum(salary) from employees;

--avg : ���
select avg(salary) avg_sal from employees;

--min : �ּҰ�
select min(salary) from employees;

--max : �ִ밪
select max(salary) from employees;



--���� 6461�޷����� ��������� ����Ͻÿ� <<��������>>
select * from employees
where salary > (select avg(salary) avg_sal from employees);

select min (salary) from employees;

--�ּҿ��� �޴»���� ���,�̸��� ����Ͻÿ�
select employee_id ,emp_name,salary from employees
where salary=(select min (salary) from employees);

--�ִ���� �޴»���� ���,�̸��� ����Ͻÿ�
select employee_id ,emp_name,salary from employees
where salary=(select max (salary) from employees);

--�μ� ��ȣ�� 50���� ����� ��ü ����
select department_id,salary from employees;

select sum(salary) from employees
where department_id= 50;

select count (*) from stu_score;

--���� kor������ 80���̻��� ����� ����Ͻÿ�
select kor from stu_score
where kor >= 80;

--�������� ����̻�, �������� ��� �̻� ����Ͻÿ�
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

--����
--������ �ִ��� ����� �ּ��� ��� ���

select  emp_name,salary from employees
where salary=(select min (salary) from employees)
or salary=(select max (salary) from employees)
or salary=(select avg (salary) from employees);


--�ִ밪
select emp_name,salary from employees
where salary=(select max(salary) from employees);


--�̰� �ϳ��� ���̺�� �����Ѵ�
--��պ��� ������
select emp_name,salary from employees
where salary >= (select avg(salary) from employees)
order by salary;


--��պ��� ���� ����߿� �ִ밪�� ����� ����Ͻÿ�
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

--�����Լ�
--lpad,rpad�� ���� ä���
select emp_name,lpad(emp_name,15,'#')from employees;
select emp_name,rpad(emp_name,50,'@')from employees;


-- ltrim,rtrim Ư�� ���� ���ڸ� �߶󳻰� ���
select emp_name,ltrim(emp_name,'Do') from employees;



--ko20240001
select 'ko20240001', ltrim('ko20240001','ko2024') from dual;

--substr(������,����,����)
select emp_name,substr(emp_name,3,4) from employees;

select job_id from employees;

--����.  job_id�� �ִ� �տ� sh�� �����ȣ�� �����ؼ� ��½�Ű�ÿ�
select  substr(job_id,0,2)|| employee_id  from employees;

--length
select emp_name,length(emp_name) from employees
where length(emp_name)>15;

--��¥���� ���°� �ȴ�.
select sysdate-hire_date from employees;

--��¥���� ���ϴ°� �ȵȴ�.
select sysdate+hire_date from employees;

--�������� ù°��
select round(sysdate,'month') from dual;

select round(sysdate,'year') from dual;

--���ϴ� �޷� �̵�
select sysdate,add_months(sysdate,-2) from dual;


--ceil������ floor���� mod������ power����
select ceil(-4.2),floor(-4.2),mod(8,3),power(2,10) from dual;

select emp_name || to_char(hire_date,' yyyy "��" mm "��"dd "��"') from employees;

----------------------------���� ����� ����*1400�� �տ� ��ȭ ǥ�ÿ� ��ǥ�� �־� ���
select salary,to_char(salary*1400,'L000,000,000') from employees;

--�ڽ��� ���ϰ� �ڽ��� ������ ���� ���� ��������¥

select trunc(to_date('2010-10-10'),'month'),'2010-10-10' ,last_day('2010-10-01') from dual;



select  * from member;

desc member;

alter table member drop column phone;


--ddl(data) �÷� �߰����ֱ�
--�����ִ� ddl�� Ŀ��,�ѹ��� ����
alter table member add gender varchar2(6) default 'Female' not null;
select  * from member;

update member set gender='male';

commit;

--�÷����� : �̸�����
alter table member rename column name to stu_name
;

--�÷����� : Ÿ�Ժ���
alter table member modify(stu_name varchar2(50));

--������ �����Ͱ� �����Ϸ��� ũ�⺸�� �������� ����
update member set stu_name='';
alter table member modify(stu_name varchar2(6));

alter table member modify(stu_name varchar2(4));
desc member;
select stu_name from member;

--�ڸ��� �ʰ� ����
alter table member modify(stu_name number(100));
desc member;

select  * from member;
































 
 




 

































