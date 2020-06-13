import pymysql

# 使用 connect 方法，传入数据库地址，账号，密码，数据库名就可以得到你的数据库对象
db = pymysql.connect("localhost",'root','root','studypython')

# 接着我们获取 cursor 来操作我们的 studypython 这个数据库
cursor = db.cursor()

# 比如我们来创建一张数据表
sql = """create table beautyGirls (
        name char(20) not null,
        age int )"""
cursor.execute(sql)

#  插入数据
sql = "insert into beautyGrils(name,age) values ('Mrs.cang',18)"

try:
    cursor.execute(sql)
    db.commit()
except:
    # 回滚
    db.rollback()

# 最后我们关闭这个数据库的连接
db.close()