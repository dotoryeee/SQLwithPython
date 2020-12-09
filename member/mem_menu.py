import member.mem_service as service

class Mem_Menu:
    def __init__(self, id, pwd, addr, enc):
        self.service = service.Service(id, pwd, addr, enc)

    def run(self):
        print('회원관리 메뉴')
        while True:
            mm = int(input('1.가입 2.로그인 3.내정보수정 4.로그아웃 5.탈퇴 6.종료'))
            if mm==1:
                self.service.join()
            elif mm==2:
                self.service.login()
            elif mm==3:
                self.service.editMyInfo()
            elif mm==4:
                self.service.logout()
            elif mm==5:
                self.service.out()
            elif mm==6:
                break