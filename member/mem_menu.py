import mem_service as Service

class Menu():
    def __init__(self):
        self.service = Service.Service('hr', 'hr', 'localhost:1521/xe', 'utf-8')

    def run(self):
        while True:
            mm = input('1.가입 2.로그인 3.정보수정 4.로그아웃 5.탈퇴 6.종료')
            if mm = '1':
                self.service.join()
            if mm = '2':
                self.service.login()
            if mm = '3':
                self.service.editMyInfo()
            if mm = '4':
                self.service.logout()
            if mm = '5':
                self.service.out()
            if mm = '6':
                break
