import pygame as pg
import copy 
#white pieces
white_elephant=pg.image.load("./images/white_elephant.png")
white_bishop=pg.image.load("./images/white_bishop.png")
white_horse=pg.image.load("./images/white_horse.png")
white_king=pg.image.load("./images/white_king.png")
white_pawn= pg.image.load("./images/white_pawn.png")
white_queen=pg.image.load("./images/white_queen.png")
#black pieces
black_elephant=pg.image.load("./images/black_elephant.png")
black_bishop=pg.image.load("./images/black_bishop.png")
black_horse=pg.image.load("./images/black_horse.png")
black_king=pg.image.load("./images/black_king.png")
black_pawn= pg.image.load("./images/black_pawn.png")
black_queen=pg.image.load("./images/black_queen.png")
class Piece:
    def __init__(self,row,col,color) -> None:
        self.row=row
        self.col=col
        self.color=color
        self.selected=False
        self.king=False
        self.moves=[]
    def update_moves(self,board):
        self.moves=self.possible_moves(board,self.row,self.col)
        self.moves=self.valid_move(self.moves,board,self.row,self.col)
        return len(self.moves)
    def isSelected(self):
        return self.selected
    def dangerous_moves(self,color,board):
        opponents_moves=[]
        for i in range(8):
            for j in range(8):
                if board[i][j]!=0 and board[i][j].color!=color:
                    opponents_moves.extend(board[i][j].possible_moves(board,i,j))
        
        return opponents_moves
    def is_check(self,color,board):
        opponents_moves=self.dangerous_moves(color,board.copy())
        # print("danger moves")
        # for i in opponents_moves:
        #     print(i)
        # print("dangermoves done")
        king_pos=(-1,-1)
        for i in range(8):
            for j in range(8):
                if board[i][j]!=0 and board[i][j].king and board[i][j].color==color:
                    # print("king pos ",end="")
                    # print((i,j))
                    if (i,j) in opponents_moves:
                        return True
                    else:
                        return False
    
    def valid_move(self,moves,board,i_x,i_y):
        final_ans=[]
        for final_pos in moves:
            dummy_board=copy.deepcopy(board)
            dummy_board[final_pos[0]][final_pos[1]]=dummy_board[i_x][i_y]
            dummy_board[i_x][i_y]=0
            if not self.is_check(self.color,dummy_board):
                final_ans.append(final_pos)
        
        # print("valid moves")
        # for i in final_ans:
        #     print(i)
        return final_ans

    def move(self):
        pass


class Bishop(Piece):
    
    def check_move(self,x,y,board):
        # moves=self.possible_moves(board,self.row,self.col)
        moves=self.moves
        if (x,y) in moves:
            board[x][y]=board[self.row][self.col]
            board[self.row][self.col]=0
            self.row=x
            self.col=y
            self.selected=False
            return True
        return False
    def draw(self,screen,board,current_color):
        if self.color=='w':
            image=white_bishop
        else:
            image=black_bishop
        
        x=70+self.col*70
        y=70+self.row*70
        if self.selected and current_color==self.color:
            pg.draw.rect(screen,(255,0,0),(x,y,70,70),2)
            # moves=self.possible_moves(board,self.row,self.col)
            # for i in moves:
            #     print(i)
            # moves=self.valid_move(moves,board.copy(),self.row,self.col)
            moves=self.moves
            # print("final_moves are here")
            # for i in moves:
            #     print(i)
            # if len(moves)==0:
            #     print("something is wrong")
            for pos in moves:
                x1=70+pos[1]*70
                y1=70+pos[0]*70
                pg.draw.rect(screen,(0,255,0),(x1,y1,70,70),2)
        screen.blit(image,(x,y))
    
    def possible_moves(self,board,i,j):
        moves=[]
        # i=self.row
        # j=self.col
        
        #bottom right
        for t in range(1,8):
            curr_row=i+t
            curr_col=j+t
            if curr_row>7 or curr_col>7:
                break
            if board[curr_row][curr_col]!=0 and ((self.color=='w' and board[curr_row][curr_col].color=='w') or (self.color!='w' and board[curr_row][curr_col].color!='w')):
                break
            if board[curr_row][curr_col]!=0:
                moves.append((curr_row,curr_col))
                break
            # if self.valid_move(i,j,curr_row,curr_col,board):
            moves.append((curr_row,curr_col))
        #bottom left
        for t in range(1,8):
            curr_row=i+t
            curr_col=j-t
            if curr_row>7 or curr_col<0:
                break
            if board[curr_row][curr_col]!=0 and ((self.color=='w' and board[curr_row][curr_col].color=='w') or (self.color!='w' and board[curr_row][curr_col].color!='w')):
                break
            if board[curr_row][curr_col]!=0:
                moves.append((curr_row,curr_col))
                break
            # if self.valid_move(i,j,curr_row,curr_col,board):
            moves.append((curr_row,curr_col))
        #top right
        for t in range(1,8):
            curr_row=i-t
            curr_col=j+t
            if curr_row<0 or curr_col>7:
                break
            if board[curr_row][curr_col]!=0 and ((self.color=='w' and board[curr_row][curr_col].color=='w') or (self.color!='w' and board[curr_row][curr_col].color!='w')):
                break
            if board[curr_row][curr_col]!=0:
                moves.append((curr_row,curr_col))
                break
            # if self.valid_move(i,j,curr_row,curr_col,board):
            moves.append((curr_row,curr_col))
        #top left
        for t in range(1,8):
            curr_row=i-t
            curr_col=j-t
            if curr_row<0 or curr_col<0:
                break
            if board[curr_row][curr_col]!=0 and ((self.color=='w' and board[curr_row][curr_col].color=='w') or (self.color!='w' and board[curr_row][curr_col].color!='w')):
                break
            if board[curr_row][curr_col]!=0:
                moves.append((curr_row,curr_col))
                break
            # if self.valid_move(i,j,curr_row,curr_col,board):
            moves.append((curr_row,curr_col))
        return moves

class Elephant(Piece):
    def check_move(self,x,y,board):
        # moves=self.possible_moves(board,self.row,self.col)
        moves=self.moves
        if (x,y) in moves:
            board[x][y]=board[self.row][self.col]
            board[self.row][self.col]=0
            self.row=x
            self.col=y
            self.selected=False
            return True
        return False
    def draw(self,screen,board,current_color):
        if self.color=='w':
            image=white_elephant
        else:
            image=black_elephant
        x=70+self.col*70
        y=70+self.row*70
        if self.selected and self.color==current_color:
            pg.draw.rect(screen,(255,0,0),(x,y,70,70),2)
            # moves=self.possible_moves(board,self.row,self.col)
            moves=self.moves
            for pos in moves:
                x1=70+pos[1]*70
                y1=70+pos[0]*70
                pg.draw.rect(screen,(0,255,0),(x1,y1,70,70),2)
        screen.blit(image,(x,y))
    
    def possible_moves(self,board,i,j):
        moves=[]
        # i=self.row
        # j=self.col
        #moving up
        for t in range(1,8):
            curr_row=i-t
            if curr_row<0:
                break
            if board[curr_row][j]!=0 and ((self.color=='w' and board[curr_row][j].color=='w') or (self.color!='w' and board[curr_row][j].color!='w')):
                break
            if board[curr_row][j]!=0:
                moves.append((curr_row,j))
                break
            moves.append((curr_row,j))
        
        #moving down
        for t in range(1,8):
            curr_row=i+t
            if curr_row>7:
                break
            if board[curr_row][j]!=0 and ((self.color=='w' and board[curr_row][j].color=='w') or (self.color!='w' and board[curr_row][j].color!='w')):
                break
            if board[curr_row][j]!=0:
                moves.append((curr_row,j))
                break
            moves.append((curr_row,j))
        #moving left
        for t in range(1,8):
            curr_col=j-t
            if curr_col<0:
                break
            if board[i][curr_col]!=0 and ((self.color=='w' and board[i][curr_col].color=='w') or (self.color!='w' and board[i][curr_col].color!='w')):
                break
            if board[i][curr_col]!=0:
                moves.append((i,curr_col))
                break
            moves.append((i,curr_col))
        #moving right
        for t in range(1,8):
            curr_col=j+t
            if curr_col>7:
                break
            if board[i][curr_col]!=0 and ((self.color=='w' and board[i][curr_col].color=='w') or (self.color!='w' and board[i][curr_col].color!='w')):
                break
            if board[i][curr_col]!=0:
                moves.append((i,curr_col))
                break
            moves.append((i,curr_col))
        return moves
class Horse(Piece):
    def check_move(self,x,y,board):
        # moves=self.possible_moves(board,self.row,self.col)
        moves=self.moves
        if (x,y) in moves:
            board[x][y]=board[self.row][self.col]
            board[self.row][self.col]=0
            self.row=x
            self.col=y
            self.selected=False
            return True
        return False
    def draw(self,screen,board,current_color):
        if self.color=='w':
            image=white_horse
        else:
            image=black_horse
        x=70+self.col*70
        y=70+self.row*70
        if self.selected and current_color==self.color:
            pg.draw.rect(screen,(255,0,0),(x,y,70,70),2)
            # moves=self.possible_moves(board,self.row,self.col)
            moves=self.moves
            for pos in moves:
                x1=70+pos[1]*70
                y1=70+pos[0]*70
                # print(x1,y1)
                pg.draw.rect(screen,(0,255,0),(x1,y1,70,70),2)
        screen.blit(image,(x,y))
    
    def possible_moves(self,board,i,j):
        directions=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
        moves=[]
        # i=self.row
        # j=self.col
        for dir in directions:
            curr_row=i+dir[0]
            curr_col=j+dir[1]
            if( curr_row<0 or curr_col<0 or curr_row>7 or curr_col>7 or (board[curr_row][curr_col]!=0 and self.color=='w' and board[curr_row][curr_col].color=='w') or (board[curr_row][curr_col]!=0 and self.color!='w' and board[curr_row][curr_col].color!='w')):
                continue
            moves.append((curr_row,curr_col))
        
        return moves

class Pawn(Piece):
    def __init__(self, row, col, color) -> None:
        super().__init__(row, col, color)
        self.first=True
        self.queen=False
    def check_move(self,x,y,board):
        # moves=self.possible_moves(board,self.row,self.col)
        moves=self.moves
        if (x,y) in moves:
            board[x][y]=board[self.row][self.col]
            board[self.row][self.col]=0
            self.row=x
            self.col=y
            self.first=False
            self.selected=False
            return True
        return False
    def draw(self,screen,board,current_color):
        if self.color=='w':
            image=white_pawn
        else:
            image=black_pawn
        x=70+self.col*70
        y=70+self.row*70
        if self.selected and current_color==self.color:
            pg.draw.rect(screen,(255,0,0),(x,y,70,70),2)
            # moves=self.possible_moves(board,self.row,self.col)
            moves=self.moves
            # print("pawn selected")
            # for i in moves:
                # print(i)
            for pos in moves:
                x1=70+pos[1]*70
                y1=70+pos[0]*70
                pg.draw.rect(screen,(0,255,0),(x1,y1,70,70),2)
        screen.blit(image,(x,y))
    
    def possible_moves(self,board,i,j):
        moves=[]
        # i=self.row
        # j=self.col
        if(self.color=='w'):
            if self.first and board[i-2][j]==0 and board[i-1][j]==0:
                moves.append((i-2,j))
            if i-1>=0 and board[i-1][j]==0:
                moves.append((i-1,j))
            if i-1>=0 and j-1>=0 and board[i-1][j-1]!=0 and board[i-1][j-1].color!='w':
                moves.append((i-1,j-1))
            if i-1>=0 and j+1<8 and board[i-1][j+1]!=0 and board[i-1][j+1].color!='w':
                moves.append((i-1,j+1))
        else:
            if self.first and board[i+2][j]==0 and board[i+1][j]==0:
                moves.append((i+2,j))
            if i+1<8 and board[i+1][j]==0:
                moves.append((i+1,j))
            if i+1<8 and j-1>=0 and board[i+1][j-1]!=0 and board[i+1][j-1].color=='w':
                moves.append((i+1,j-1))
            if i+1<8 and j+1<8 and board[i+1][j+1]!=0 and board[i+1][j+1].color=='w':
                moves.append((i+1,j+1))
        return moves

class King(Piece):
    def __init__(self, row, col, color) -> None:
        super().__init__(row, col, color)
        self.king=True
    def check_move(self,x,y,board):
        # moves=self.possible_moves(board,self.row,self.col)
        moves=self.moves
        if (x,y) in moves:
            board[x][y]=board[self.row][self.col]
            board[self.row][self.col]=0
            self.row=x
            self.col=y
            self.selected=False
            return True
        return False
    def draw(self,screen,board,current_color):
        if self.color=='w':
            image=white_king
        else:
            image=black_king
        x=70+self.col*70
        y=70+self.row*70
        if self.selected and current_color:
            pg.draw.rect(screen,(255,0,0),(x,y,70,70),2)
            # moves=self.possible_moves(board,self.row,self.col)
            moves=self.moves
            for pos in moves:
                x1=70+pos[1]*70
                y1=70+pos[0]*70
                pg.draw.rect(screen,(0,255,0),(x1,y1,70,70),2)
        screen.blit(image,(x,y))
    
    def possible_moves(self,board,i,j):
        moves=[]
        directions=[(-1,0),(1,0),(0,-1),(0,1),(1,-1),(1,1),(-1,1),(-1,-1)]
        for dir in directions:
            curr_row=i+dir[0]
            curr_col=j+dir[1]
            if(curr_row<0 or curr_col<0 or curr_col>7 or curr_row>7 or (self.color=='w' and board[curr_row][curr_col]!=0 and board[curr_row][curr_col].color=='w') or (self.color!='w' and board[curr_row][curr_col]!=0 and board[curr_row][curr_col].color!='w')):
                continue
            moves.append((curr_row,curr_col))
        return moves
class Queen(Piece):
    def check_move(self,x,y,board):
        # moves=self.possible_moves(board,self.row,self.col)
        moves=self.moves
        if (x,y) in moves:
            board[x][y]=board[self.row][self.col]
            board[self.row][self.col]=0
            self.row=x
            self.col=y
            self.selected=False
            return True
        return False
    def draw(self,screen,board,current_color):
        if self.color=='w':
            image=white_queen
        else:
            image=black_queen
        x=70+self.col*70
        y=70+self.row*70
        if self.selected and current_color==self.color:
            pg.draw.rect(screen,(255,0,0),(x,y,70,70),2)
            # moves=self.possible_moves(board,self.row,self.col)
            moves=self.moves
            for pos in moves:
                x1=70+pos[1]*70
                y1=70+pos[0]*70
                pg.draw.rect(screen,(0,255,0),(x1,y1,70,70),2)
        screen.blit(image,(x,y))
    
    def possible_moves(self,board,i,j):
        moves=[]
        # i=self.row
        # j=self.col
        #moving up
        for t in range(1,8):
            curr_row=i-t
            if curr_row<0:
                break
            if board[curr_row][j]!=0 and ((self.color=='w' and board[curr_row][j].color=='w') or (self.color!='w' and board[curr_row][j].color!='w')):
                break
            if board[curr_row][j]!=0:
                moves.append((curr_row,j))
                break
            moves.append((curr_row,j))
        
        #moving down
        for t in range(1,8):
            curr_row=i+t
            if curr_row>7:
                break
            if board[curr_row][j]!=0 and ((self.color=='w' and board[curr_row][j].color=='w') or (self.color!='w' and board[curr_row][j].color!='w')):
                break
            if board[curr_row][j]!=0:
                moves.append((curr_row,j))
                break
            moves.append((curr_row,j))
        #moving left
        for t in range(1,8):
            curr_col=j-t
            if curr_col<0:
                break
            if board[i][curr_col]!=0 and ((self.color=='w' and board[i][curr_col].color=='w') or (self.color!='w' and board[i][curr_col].color!='w')):
                break
            if board[i][curr_col]!=0:
                moves.append((i,curr_col))
                break
            moves.append((i,curr_col))
        #moving right
        for t in range(1,8):
            curr_col=j+t
            if curr_col>7:
                break
            if board[i][curr_col]!=0 and ((self.color=='w' and board[i][curr_col].color=='w') or (self.color!='w' and board[i][curr_col].color!='w')):
                break
            if board[i][curr_col]!=0:
                moves.append((i,curr_col))
                break
            moves.append((i,curr_col))
        
        #bottom right
        for t in range(1,8):
            curr_row=i+t
            curr_col=j+t
            if curr_row>7 or curr_col>7:
                break
            if board[curr_row][curr_col]!=0 and ((self.color=='w' and board[curr_row][curr_col].color=='w') or (self.color!='w' and board[curr_row][curr_col].color!='w')):
                break
            if board[curr_row][curr_col]!=0:
                moves.append((curr_row,curr_col))
                break
            moves.append((curr_row,curr_col))
        #bottom left
        for t in range(1,8):
            curr_row=i+t
            curr_col=j-t
            if curr_row>7 or curr_col<0:
                break
            if board[curr_row][curr_col]!=0 and ((self.color=='w' and board[curr_row][curr_col].color=='w') or (self.color!='w' and board[curr_row][curr_col].color!='w')):
                break
            if board[curr_row][curr_col]!=0:
                moves.append((curr_row,curr_col))
                break
            moves.append((curr_row,curr_col))
        #top right
        for t in range(1,8):
            curr_row=i-t
            curr_col=j+t
            if curr_row<0 or curr_col>7:
                break
            if board[curr_row][curr_col]!=0 and ((self.color=='w' and board[curr_row][curr_col].color=='w') or (self.color!='w' and board[curr_row][curr_col].color!='w')):
                break
            if board[curr_row][curr_col]!=0:
                moves.append((curr_row,curr_col))
                break
            moves.append((curr_row,curr_col))
        #top left
        for t in range(1,8):
            curr_row=i-t
            curr_col=j-t
            if curr_row<0 or curr_col<0:
                break
            if board[curr_row][curr_col]!=0 and ((self.color=='w' and board[curr_row][curr_col].color=='w') or (self.color!='w' and board[curr_row][curr_col].color!='w')):
                break
            if board[curr_row][curr_col]!=0:
                moves.append((curr_row,curr_col))
                break
            moves.append((curr_row,curr_col))
        return moves