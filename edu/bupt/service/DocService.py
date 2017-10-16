import edu.bupt.db.mysql as mysql

class DocService:
    def __init__(self):
        self.mysql = mysql.MySQL('127.0.0.1', 'root', '123456', 3306)
        self.mysql.selectDb('nlp')


    def fetch(self, sql):
        self.mysql.query(sql)
        result = self.mysql.fetchAll()
        return result

    def insertBatch(self, table_name, datas):
        self.mysql.insetBatch(table_name, datas)
        self.mysql.commit()

    def insert(self, data, table_name):
        self.mysql.insert(table_name=table_name, data=data)
        self.mysql.commit()