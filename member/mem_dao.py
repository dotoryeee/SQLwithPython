import cx_Oracle
import proj1.member.mem_vo as vo

class Dao:
    def __init__(self, id, pwd, addr, enc):
        self.id = id
        self.pwd = pwd
        self.addr = addr
        self.enc = enc

    def conn(self):#db 연결
        return cx_Oracle.connect(self.id, self.pwd, self.addr, encoding=self.enc)
        #conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')

    def disconn(self, conn):#db 끊기
        conn.close()

    def insert(self, mem):#mem은 Member 객체로 회원가입한 사람의 id,pwd,name,email이 들어있음. 이 값을 테이블에 insert
        my_conn = self.conn() #db 연결
        cursor = my_conn.cursor() #사용할 커서 객체 생성
        sql = 'insert into member values(:1, :2, :3, :4)' #sql 문장 생성. 바인딩 변수
        t = (mem.id, mem.pwd, mem.name, mem.email)  #바인딩 값으로 튜플 생성
        cursor.execute(sql, t)  #execute()으로 sql 실행. t는 sql의 바인딩 값 튜플
        my_conn.commit()
        self.disconn(my_conn)   #커넥션 닫음

    def select(self, id):#id컬럼값이 파라메터 id와 동일한 한 줄 검색하여 Member 객체로 생성해서 반환
        my_conn = self.conn()  # db 연결
        cursor = my_conn.cursor()  # 사용할 커서 객체 생성
        sql = 'select * from member where id=:1'  # sql 문장 생성. 바인딩 변수
        t = (id,)  # 바인딩 값으로 튜플 생성
        cursor.execute(sql, t)  # execute()으로 sql 실행. t는 sql의 바인딩 값 튜플
        row = cursor.fetchone()
        self.disconn(my_conn)  # 커넥션 닫음
        if row is not None:
            return vo.Member(row[0], row[1], row[2], row[3])

    def selectAll(self):#member 테이블 모든 줄 검색하여 리스트에 담아서 반환
        my_conn = self.conn()
        cursor = my_conn.cursor()
        sql = 'select * from member'
        cursor.execute(sql)
        mems = []
        for row in cursor:
            mems.append(vo.Member(row[0], row[1], row[2], row[3]))
        self.disconn(my_conn)
        return mems

    def update(self, mem):#mem에 Member 객체 전달. 이 객체에는 수정할 사람의 id와 새 pwd, 새 email을 담아전달.이 값으로 수정 완료. 아무값도 반환 안함
        my_conn = self.conn()  # db 연결
        cursor = my_conn.cursor()  # 사용할 커서 객체 생성
        sql = 'update member set pwd=:1, email=:2 where id=:3'  # sql 문장 생성. 바인딩 변수
        t = (mem.pwd, mem.email, mem.id)  # 바인딩 값으로 튜플 생성
        cursor.execute(sql, t)  # execute()으로 sql 실행. t는 sql의 바인딩 값 튜플
        my_conn.commit()
        self.disconn(my_conn)

    def delete(self, id):#id로 찾아서 삭제.
        my_conn = self.conn()  # db 연결
        cursor = my_conn.cursor()  # 사용할 커서 객체 생성
        sql = 'delete member where id=:1'  # sql 문장 생성. 바인딩 변수
        t = (id,)  # 바인딩 값으로 튜플 생성
        cursor.execute(sql, t)  # execute()으로 sql 실행. t는 sql의 바인딩 값 튜플
        my_conn.commit()
        self.disconn(my_conn)