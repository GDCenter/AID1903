import  pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'debian-sys-maint',
    password ='63n1RN2Vs1hh7Xhj',
    database = 'stu',
    charset = 'utf8'
)
cur = db.cursor()
try:
    sql = "insert into interest values " \
          "(7,'bob','draw,sing','a','8888','loser');"
    cur.execute(sql)

    sql = "update interest set price = 6666 where name = 'Abby';"
    cur.execute(sql)

    sql = "delete from myclass where  score < 8888;"
    cur.execute(sql)
    db.commit()

    xiugai = property

except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()
