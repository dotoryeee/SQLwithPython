import proj1.board.board_vo as bv
import proj1.board.board_dao as bdao
import proj1.member.mem_service as mserv
class Service:

    def __init__(self, id, pwd, addr, enc):
        self.dao = bdao.Dao(id, pwd, addr, enc)

    def addBoard(self):#글 하나 추가. 제목, 내용만 입력받고 나머지 자동입력
        print('글작성')
        b = bv.Board(writer=mserv.Service.login_id)#작성자는 자동을 로그인 아이디 할당
        b.title = input('title:')
        b.content = input('content:')
        self.dao.insert(b)

    def getByNum(self):
        print('글 번호로 검색')
        num = int(input('num:'))
        b = self.dao.selectByNum(num)
        if b==None:
            print('없는 글 번호')
        else:
            print(b)

    def getByWriter(self):
        print('글 작성자로 검색')
        writer = input('writer:')
        self.getByWriter1(writer)

    def getByWriter1(self, writer):
        b_list = self.dao.selectByWriter(writer)
        if len(b_list)==0:
            print('검색결과 없음')
            return
        for b in b_list:
            print(b)

    def getByTitle(self):
        print('글 제목으로 검색')
        title = input('title:')
        b_list = self.dao.selectByTitle(title)
        if len(b_list) == 0:
            print('검색결과 없음')
            return
        for b in b_list:
            print(b)

    def editBoard(self):
        print('글 수정(본인이 작성한 글만 수정함)')
        print('본인 글')
        self.getByWriter1(mserv.Service.login_id)
        b = bv.Board()
        b.num = int(input('수정할 글의 번호:'))
        b.title = input('new title:')
        b.content = input('new content:')
        bb = self.dao.selectByNum(b.num)
        if bb==None:
            print('없는 글. 수정 취소')
        else:
            if bb.writer==mserv.Service.login_id:
                self.dao.update(b)
            else:
                print('본인 글이 아니므로 수정 불가')

    def delBoard(self):
        print('글 삭제')
        num = int(input('삭제할 글의 번호:'))
        bb = self.dao.selectByNum(num)
        if bb == None:
            print('없는 글. 삭제 취소')
        else:
            if bb.writer == mserv.Service.login_id:
                self.dao.delete(num)
            else:
                print('본인 글이 아니므로 삭제 불가')

    def getAll(self):
        b_list = self.dao.selectAll()
        if len(b_list) == 0:
            print('등록된 글이 없음')
            return
        for b in b_list:
            print(b)
