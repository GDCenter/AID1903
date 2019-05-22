"""

    add ,delete update

"""

import  pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'debian-sys-maint',
    password ='Asd123',
    database = 'stu',
    charset = 'utf8'
)
cur = db.cursor()
while True:

    name = input(">>>Name:")
    age = input(">>>Age:")
    sex = input(">>>m or w :")
    score = input(">>>Score:")

    sql = "insert into myclass (name, age, sex, score) values (%s,%d,%s,%s);"
    try:
        cur.execute(sql)
        db.commit()
    except Exception as e :
        db.rollback()
        print("faild :",e)

cur.close()
db.close()


