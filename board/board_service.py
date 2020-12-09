import board.board_vo as vo
import board.board_dao as dao

class Service():

    def __init__(self, id, pwd, address, enc, login_id):
        self.dao = dao.Dao(id, pwd, address, enc)
        self.login_id = login_id

    def newPost(self):
        p = vo.Board()
        if self.login_id is None:
            print('로그인이 필요합니다')
            return
        print('새로운 게시글')
        p.writer = Service.login_id
        p.title = input('제 목 : ')
        p.content = input('내용 입력 : ')
        self.dao.insert(p)

    def showMemberPost(self):
        targetID = self.login_id
        print(self.dao.selectMemberPost(targetID))

    def deletePost(self):
        self.showMemberPost()
        int(input('삭제할 게시글 번호 : '))
