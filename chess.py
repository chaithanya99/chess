import pygame as pg
import Board
pg.init()

board=pg.image.load("./images/board.jpg")
board=pg.transform.scale(board,(700,700))



def drawing_window(screen,b):
    screen.blit(board,(0,0))
    b.draw(screen)
    pg.display.update()

def click(mouse_position):
    x=mouse_position[0]//70
    y=mouse_position[1]//70
    if x==0 or y==0 or x>=9 or y>=9:
        return None
    return (y-1,x-1)

def draw_winner(screen,loser,font):
    if loser=='b':

        text_content="White wins the Game"

    else:
        text_content="Black wins the Game"
    text_surface = font.render(text_content, True, (255,255,255))
    screen.fill((0, 0, 0))  # Black

    # Draw the text on the screen
    screen.blit(text_surface, (200, 350))

    # Update the screen
    pg.display.flip()

def main(screen):
    font = pg.font.Font(None, 36)
    running=True
    bo=Board.Board()
    game=True
    while running:
        if game:
            drawing_window(screen,bo)
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    running=False
                if pg.mouse.get_pressed()[0]:
                    loser=bo.update_all_moves()
                    if loser:
                        game=False
                        continue
                    mouse_pos=pg.mouse.get_pos()
                    x,y=click(mouse_pos)
                    bo.select_piece(x,y)
        
        else:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    running=False
            draw_winner(screen,loser,font)
                    

width=700
height=700
screen=pg.display.set_mode((width,height))
pg.display.set_caption("Chess")
main(screen)
