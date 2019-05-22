"""
    pymysql , liucheng yanshi


"""


import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'debian-sys-maint',
    password ='Asd123',
    database = 'stu',
    charset = 'utf8'
)


# get cursor
cur = db.cursor()



# data operate
# cur.execute()
try:
    cur.execute("insert into myclass value(12,'pEligp',15,'w',89.5);")
    db.commit()
except Exception as e :
    print(e)
    db.rollback()
#cursor close
cur.close()
db.close()