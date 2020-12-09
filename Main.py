import member.mem_menu as mem_menu
import board.board_menu as board_menu
#import proj1.board.board_menu as board_menu
def main():
    m_menu = mem_menu.Mem_Menu('hr', 'hr', 'localhost:1521/xe', 'utf-8')
    b_menu = board_menu.board_Menu('hr', 'hr', 'localhost:1521/xe', 'utf-8')
    #b_menu = board_menu.Board_Menu('hr', 'hr', 'localhost:1521/xe', 'utf-8')
    while True:
        m = int(input('1.회원관리 2.게시판 3.종료'))
        if m==1:
            m_menu.run()
        elif m==2:
            b_menu.run()
        elif m==3:
            break
main()