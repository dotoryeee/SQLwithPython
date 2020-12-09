import board.board_service as service

class board_Menu:
    def __init__(self, id, pwd, address, enc, login_id=None):
        self.service = service.Service(id, pwd, address, enc, login_id)
        self.login_id = login_id

    def run(self):
        if self.login_id is None:
            print('로그인이 필요합니다')
            return
        print('Welcome to Board')
        while True:
            sel = input('1.newPost 2.EditPost 3.DelPost 4. MyPost 5.Exit')
            if sel == '1':
                self.service.newPost()
            if sel == '2':
                pass
            if sel == '3':
                self.service.deletePost()
            if sel == '4':
                self.service.showMemberPost()
            if sel == '5':
                break
