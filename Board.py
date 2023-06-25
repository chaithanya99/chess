from Piece import King
from Piece import Queen
from Piece import Pawn
from Piece import Horse
from Piece import Bishop
from Piece import Elephant

class Board:
    def __init__(self) -> None:
        self.current_color='w'
        self.rows=8
        self.cols=8
        self.board=[[0 for i in range(8)] for _ in range(self.rows)]
        #black
        self.board[0][0]=(Elephant(0,0,'b'))
        self.board[0][1]=(Horse(0,1,'b'))
        self.board[0][2]=(Bishop(0,2,'b'))
        self.board[0][3]=(Queen(0,3,'b'))
        self.board[0][4]=(King(0,4,'b'))
        self.board[0][5]=(Bishop(0,5,'b'))
        self.board[0][6]=(Horse(0,6,'b'))
        self.board[0][7]=(Elephant(0,7,'b'))

        #black pawns
        for i in range(8):
            self.board[1][i]=(Pawn(1,i,'b'))
        
        #white
        self.board[7][0]=(Elephant(7,0,'w'))
        self.board[7][1]=(Horse(7,1,'w'))
        self.board[7][2]=(Bishop(7,2,'w'))
        self.board[7][3]=(Queen(7,3,'w'))
        self.board[7][4]=(King(7,4,'w'))
        self.board[7][5]=(Bishop(7,5,'w'))
        self.board[7][6]=(Horse(7,6,'w'))
        self.board[7][7]=(Elephant(7,7,'w'))
        #white pawns
        for i in range(8):
            self.board[6][i]=(Pawn(6,i,'w'))

    def draw(self,screen):
        for i in range(self.rows):
            for j in range(self.cols):
                if(self.board[i][j]!=0):
                    self.board[i][j].draw(screen,self.board,self.current_color)
    
    def select_piece(self,x,y):
        
        for i in range(8):
            for j in range(8):
                if(self.board[i][j]!=0 and self.board[i][j].selected and self.board[i][j].color==self.current_color):
                    if self.board[i][j].check_move(x,y,self.board):
                        if self.current_color=='w':
                            self.current_color='b'
                        else:
                            self.current_color='w'
                        return 
                if(self.board[i][j]!=0):
                    self.board[i][j].selected=False
        if self.board[x][y]!=0 and self.board[x][y].color==self.current_color:
            self.board[x][y].selected=True
    
    def update_all_moves(self):
        count=0
        for i in range(8):
            for j in range(8):
                if self.board[i][j]!=0 and self.board[i][j].color==self.current_color:
                    count+=self.board[i][j].update_moves(self.board)
        if count==0:
            return self.current_color
        return None
              
    
