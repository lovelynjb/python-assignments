#11.Write a python code to join 2 tables emp,dept and write into EMP_DEPT table
import mysql.connector

cn = mysql.connector.connect(user='meeluann', password='meeluann',
                                 host='127.0.0.1', database='python_demo')
cs = cn.cursor()

query = "Select emp.empno, emp.ename, emp.job, emp.sal, emp.deptno, dept.dname, dept.loc from emp,dept where emp.deptno = dept.deptno"

cs.execute(query)
result_set = cs.fetchall()

def writefile(param):
    cn = mysql.connector.connect(user='meeluann', password='meeluann',
                                 host='127.0.0.1', database='python_demo')
    cursor = cn.cursor()
    add_demo = ("INSERT INTO emp_dept"
                "(empno,ename,job,sal,deptno,dname,loc) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s)")
    cursor.execute(add_demo,param)
    cn.commit()
    print ("added")
    cursor.close()
    cn.close()

for x in result_set:
    print(x)
    writefile(x)
