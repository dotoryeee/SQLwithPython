import cx_Oracle
import board.board_vo as vo

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
        sql = 'insert into board values(seq_board_num:nextval, :1, sysdate, :2, :3)'
        d = (data.writer, data.title, data.content)
        cursor.excute(sql, d)
        my_conn.commit()
        self.disconn(my_conn)

    def select(self, num):
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'select * from board where num =:1'
        d = (num, )
        cursor.excute(sql, d)
        received = cursor.fetchone()
        if received is not None:
            return vo.Board(received[0], received[1], received[2], received[3], received[4])
        self.disconn(my_conn)

    def selectAll(self):
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'select * from board'
        cursor.excute(sql)
        datas = []
        for row in cursor:
            datas.append(vo.Board(row[0], row[1], row[2], row[3], row[4]))
        self.disconn(my_conn)
        return datas

    def selectMemberPost(self, writer):
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'select * from board where writer=:1'
        d = (writer, )
        cursor.excute(sql, d)
        datas = []
        for row in cursor:
            datas.append(vo.Board(row[0],row[2],row[3],row[4]))
        self.disconn(my_conn)
        return datas

    def delete(self, num, id):
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'delete board where num =:1 and writer =:2'
        d = (num, id)
        cursor.excute(sql, d)
        self.disconn(my_conn)

    def update(self, data):
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'update board set w_date = sysdate, title =:1, content =:2 where num =:3'
        d = (data.title, data.content, data.num)
        cursor.excute(sql, d)
        my_conn.commit()
        self.disconn(my_conn)