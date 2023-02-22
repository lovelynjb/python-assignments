# Read from a csv file and write to a table in my sql table
import mysql.connector


def writefile(csv_content):
    cn = mysql.connector.connect(user='meeluann', password='meeluann',
                                 host='127.0.0.1', database='python_demo')
    cursor = cn.cursor()
    add_demo = ("INSERT INTO demo "
                "(col1, col2, col3) "
                "VALUES (%s, %s, %s)")
    
    cursor.execute(add_demo, csv_content)
    cn.commit()

    cursor.close()
    cn.close()


with open('src/FIle_01.dat', 'r') as csv_file:
    csv_content = csv_file.readlines()
    for str1 in csv_content:
        writefile(tuple(str1.split(',')))
