import cx_Oracle
import board_vo as vo

class Dao():
    def __init__(self, id, pwd, addr, enc):
        self.id = id
        self.pwd = pwd
        self.addr = addr
        self.enc = enc

    def conn(self):#db 연결
        return cx_Oracle.connect(self.id, self.pwd, self.addr, encoding=self.enc)

    def disconn(self, conn):
        conn.close()

    def insert(self, data):
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'insert into board values(:1, :2, :3, :4, :5)'
        d = (data.num, data.writer, data.w_date, data.title, data.content)
        cursor.excute(sql, d)
        my_conn.commit()
        self.disconn(my_conn)

    def select(self, num):
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'select * from board where num =:1'
        d = (num, )
        cursor(sql, d)
        received = cursor.fetchone()
        if received is not None:
            return vo.Board(received[0], received[1], received[2], received[3], received[4])
        self.disconn(my_conn)

    def selectAll(self):
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'select * from board'
        datas = []
        for row in cursor:
            datas.append(vo.Board(row[0], row[1], row[2], row[3], row[4]))
        self.disconn(my_conn)
        return datas

    def delete(self, num):
        my_conn = self.conn()
        cursor = my_conn.cursor()


    def update(self, num):
        pass