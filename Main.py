import member.mem_menu as mem_menu
#import proj1.board.board_menu as board_menu
def main():
    m_menu = mem_menu.Mem_Menu('hr', 'hr', 'localhost:1521/xe', 'utf-8')
    #b_menu = board_menu.Board_Menu('hr', 'hr', 'localhost:1521/xe', 'utf-8')
    while True:
        m = int(input('1.회원관리 2.게시판 3.종료'))
        if m==1:
            m_menu.run()
        elif m==2:
            pass #b_menu.run()
        elif m==3:
            break
main()
'''
게시판 기능-로그인 해야 가능
1. 글쓰기
2. 글 번호로 검색(1개)
3. 글 작성자로 검색(여러개)
4. 글 제목으로 검색(여러개)
5. 글수정(로그인한 사람 자기것만 수정가능. 제목, 내용 수정)
6. 글삭제(로그인한 사람 자기것만 번호로 찾아서 삭제. )
7. 글 목록출력
8. 종료
'''