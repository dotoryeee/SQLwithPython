class Board:
    def __init__(self, num=None, writer=None, w_date=None, title=None, content=None):
        self.num = num
        self.writer = writer
        self.w_date = w_date
        self.title = title
        self.content = content

    def __str__(self):
        return 'num : ' + self.num + '/writer : ' + self.writer + '/w_date : ' + self.w_date + '/title : ' + self.title + '/content : ' + self.content
