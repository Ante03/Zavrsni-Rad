
import pygame as p
import ChessEngine, smartMove

WIDTH = HEIGHT = 400
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
IMAGES = {}
MAX_FPS = 15
playerOne = True
playerTwo = False
def main():
    gs = ChessEngine.GameState()
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption("Ante Chess")
    loadImages()
    sqSelected = ()
    playerClicks = []
    running = True
    while running:
        humenTurn = gs.whiteToMove
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

            elif event.type == p.MOUSEBUTTONDOWN:
                if humenTurn:
                    location = p.mouse.get_pos()
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    if sqSelected == (row, col):
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected)
                    if len(playerClicks) == 2:
                        move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        gs.makeMove(move)
                        sqSelected = ()
                        playerClicks = []

            elif not humenTurn:
                gs.getLegalMoves()
                validMoves = gs.legalMoves
                aiMove = validMoves[smartMove.findMove(validMoves)]
                a = [aiMove[0], aiMove[1]]
                b = [aiMove[2], aiMove[3]]
                print(aiMove)
                move = ChessEngine.Move(a, b, gs.board)
                gs.makeMove(move)

            elif event.type == p.KEYDOWN:
                if event.key == p.K_z:
                    gs.undoMove()
                    sqSelected = ()
                    playerClicks = []


        drawGameState(screen, gs)
        p.display.flip()


def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.image.load("Pieces/" + piece + ".svg")

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("dark green")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))



if __name__ == "__main__":
    main()