import proj1.member.mem_service as ms
import proj1.board.board_service as bs

class Board_Menu:
    def __init__(self, id, pwd, addr, enc):
        self.service = bs.Service(id, pwd, addr, enc)

    def run(self):
        if ms.Service.login_id == None:
            print('로그인 먼저 하시오')
            return

        print('게시판 메뉴')
        while True:
            mm = int(input('1.글작성 2.번호검색 3.작성자검색 4.제목검색 5.수정 6.삭제 7.전체목록 8.종료'))
            if mm==1:
                self.service.addBoard()
            elif mm==2:
                self.service.getByNum()
            elif mm==3:
                self.service.getByWriter()
            elif mm==4:
                self.service.getByTitle()
            elif mm==5:
                self.service.editBoard()
            elif mm==6:
                self.service.delBoard()
            elif mm == 7:
                self.service.getAll()
            elif mm == 8:
                break