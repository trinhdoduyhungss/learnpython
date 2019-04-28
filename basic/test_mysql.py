import mysql.connector
class MySQL_AST:
    def __init__(self):
        self.connect_str = mysql.connector.connect(user='root', password='01669853766',
                                        host='localhost',
                                        database='test_mysql')
        self.cursor = self.connect_str.cursor()
    def __del__(self):
        self.connect_str.close()

if __name__== 'main':
    my_db = MySQL_AST()
