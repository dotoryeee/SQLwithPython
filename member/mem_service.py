import member.mem_dao as dao
import member.mem_vo as vo

class Service:
    login_id=None   #로그인 한 사람의 id를 저장할 변수

    def __init__(self, id, pwd, addr, enc):
        self.dao = dao.Dao(id, pwd, addr, enc)

    def join(self):
        m = vo.Member()
        print('회원가입')
        while True:
            m.id = input('id:')
            x = self.dao.select(m.id)
            if x==None:
                break
            else:
                print('중복된 아이디. id를 다시 입력하시오')

        m.pwd = input('pwd:')
        m.name = input('name:')
        m.email = input('email:')
        self.dao.insert(m)

    def login(self):
        print('로그인')
        id = input('id:')
        pwd = input('pwd:')
        x = self.dao.select(id)
        if x==None:
            print('없는 아이디')
        else:
            if pwd==x.pwd:
                print('로그인 성공')
                Service.login_id = id #로그인 처리
            else:
                print('패스워드 불일치')

    def editMyInfo(self):
        if Service.login_id==None:
            print('로그인 먼저 하시오')
            return
        print('내 정보')
        print(self.dao.select(Service.login_id))

        print('내정보 수정')
        m = vo.Member(id=Service.login_id)
        m.pwd = input('new pwd:')
        m.email = input('new email:')
        self.dao.update(m)

    def logout(self):
        print('로그아웃')
        if Service.login_id == None:
            print('로그인 먼저 하시오')
        else:
            Service.login_id = None

    def out(self):
        if Service.login_id == None:
            print('로그인 먼저 하시오')
        else:
            self.dao.delete(Service.login_id)
