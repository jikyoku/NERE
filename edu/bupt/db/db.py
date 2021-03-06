# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# import MySQLdb as mdb
#
# # 连接数据库
# # conn = mdb.connect('localhost', 'root', 'root')
#
# # 也可以使用关键字参数
# # conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test', charset='utf8')
#
# # 也可以使用字典进行连接参数的管理
# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'passwd': '123456',
#     'db': 'nlp',
#     'charset': 'utf8'
# }
# conn = mdb.connect(**config)
#
# # 如果使用事务引擎，可以设置自动提交事务，或者在每次操作完成后手动提交事务conn.commit()
# conn.autocommit(1)  # conn.autocommit(True)
#
# # 使用cursor()方法获取操作游标
# cursor = conn.cursor()
#
#
# # 因该模块底层其实是调用CAPI的，所以，需要先得到当前指向数据库的指针。
#
# def get_connect():
#     return conn
#
#
# def close_connect():
#
#
# try:
#     # 创建数据库
#     DB_NAME = 'nlp'
#     # cursor.execute('DROP DATABASE IF EXISTS %s' %DB_NAME)
#     # cursor.execute('CREATE DATABASE IF NOT EXISTS %s' %DB_NAME)
#     conn.select_db(DB_NAME)
#
#     # 创建表
#     TABLE_NAME = 'users'
#     # cursor.execute('CREATE TABLE %s(id int primary key,name varchar(30))' %TABLE_NAME)
#
#     # 插入单条数据
#     sql = 'INSERT INTO users values("%d","%s")' % (1, "jack")
#
#     # 不建议直接拼接sql，占位符方面可能会出问题，execute提供了直接传值
#
#     # 批量插入数据
#     values = []
#     for i in range(3, 20):
#         values.append((i, 'kk' + str(i)))
#     cursor.executemany('INSERT INTO users values(%s,%s)', values)
#
#     # 查询数据条目
#     count = cursor.execute('SELECT * FROM %s' % TABLE_NAME)
#     print 'total records: %d' % count
#     print 'total records:', cursor.rowcount
#
#     # 获取表名信息
#     desc = cursor.description
#     print "%s %3s" % (desc[0][0], desc[1][0])
#
#     # 查询一条记录
#     print 'fetch one record:'
#     result = cursor.fetchone()
#     print result
#     print 'id: %s,name: %s' % (result[0], result[1])
#
#     # 查询多条记录
#     print 'fetch five record:'
#     results = cursor.fetchmany(5)
#     for r in results:
#         print r
#
#     # 查询所有记录
#     # 重置游标位置，偏移量:大于0向后移动;小于0向前移动，mode默认是relative
#     # relative:表示从当前所在的行开始移动; absolute:表示从第一行开始移动
#     cursor.scroll(0, mode='absolute')
#     results = cursor.fetchall()
#     for r in results:
#         print r
#
#     cursor.scroll(-2)
#     results = cursor.fetchall()
#     for r in results:
#         print r
#
#     # 更新记录
#     cursor.execute('UPDATE %s SET name = "%s" WHERE id = %s' % (TABLE_NAME, 'Jack', 1))
#     # 删除记录
#     cursor.execute('DELETE FROM %s WHERE id = %s' % (TABLE_NAME, 2))
#
#     # 如果没有设置自动提交事务，则这里需要手动提交一次
#     conn.commit()
# except:
#     import traceback
#
#     traceback.print_exc()
#     # 发生错误时会滚
#     conn.rollback()
# finally:
#     # 关闭游标连接
#     cursor.close()
#     # 关闭数据库连接
#     conn.close()
