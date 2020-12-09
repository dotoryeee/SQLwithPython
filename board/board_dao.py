import cx_Oracle
import proj1.board.board_vo as bv

class Dao:
    def __init__(self, id, pwd, addr, enc):
        self.id = id
        self.pwd = pwd
        self.addr = addr
        self.enc = enc

    def conn(self):#db 연결
        return cx_Oracle.connect(self.id, self.pwd, self.addr, encoding=self.enc)

    def disconn(self, conn):#db 끊기
        conn.close()

    def insert(self, b):
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'insert into board values(seq_board_num.nextval, :1, sysdate, :2, :3)'
        t = (b.writer, b.title, b.content)
        cursor.execute(sql, t)
        my_conn.commit()
        self.disconn(my_conn)

    def selectByNum(self, num):#번호로 검색
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'select * from board where num=:1'
        t = (num,)
        cursor.execute(sql, t)
        row = cursor.fetchone()
        self.disconn(my_conn)
        if row is not None:
            return bv.Board(row[0], row[1], row[2], row[3], row[4])

    def selectByWriter(self, writer):#작성자로 검색
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'select * from board where writer=:1 order by num'
        t = (writer,)
        cursor.execute(sql, t)
        bb = []
        for row in cursor:
            bb.append(bv.Board(row[0], row[1], row[2], row[3], row[4]))

        self.disconn(my_conn)
        return bb

    def selectByTitle(self, title):#제목으로 검색
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = "select * from board where title like '%"+title+"%' order by num"
        cursor.execute(sql)
        bb = []
        for row in cursor:
            bb.append(bv.Board(row[0], row[1], row[2], row[3], row[4]))

        self.disconn(my_conn)
        return bb

    def selectAll(self):#전체검색
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'select * from board order by num'
        cursor.execute(sql)
        bb = []
        for row in cursor:
            bb.append(bv.Board(row[0], row[1], row[2], row[3], row[4]))

        self.disconn(my_conn)
        return bb

    def update(self, b):
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'update board set title=:1, content=:2 where num=:3'
        t = (b.title, b.content, b.num)
        cursor.execute(sql, t)
        my_conn.commit()
        self.disconn(my_conn)

    def delete(self, num):
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'delete board where num=:1'
        t = (num,)
        cursor.execute(sql, t)
        my_conn.commit()
        self.disconn(my_conn)