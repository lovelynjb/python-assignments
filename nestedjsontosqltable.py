#Read from a nested json file and flatten into a csv file
import json
import mysql.connector

cn = mysql.connector.connect(user='meeluann', password='meeluann',
                             host='127.0.0.1', database='python_demo')
cursor = cn.cursor()


def getphonenumber(param):
    for field in param:
        if field['type']== 'home':
            return field['number'];


def getaddress(param):
    return str(param.get('streetAddress'))+' '+str(param.get('city'))+' '+str(param.get('state'))+' '+str(param.get('postcode'));


with open('src/customer-data.json', 'r') as json_file:
    json_content = json.load(json_file)
    for field in json_content:
        rows=tuple((field["firstName"], field["lastName"],field["age"],getphonenumber(field["phoneNumber"]),getaddress(field["address"])))
        print(rows)
        cursor.execute("insert into jsontable" "(firstName,lastName,age,phoneNumber,address)""values(%s,%s,%s,%s,%s)",rows)
        cn.commit()

cursor.close()
cn.close()

