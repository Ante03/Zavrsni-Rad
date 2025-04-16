import random
import time

pieceScore = {"K" : 0, "Q" : 10, "R" : 5, "B" : 3, "N" : 3, "P" : 1}
CHECKMATE = 1000
STALEMATE = 0
DEPTH = 2

def findBestMove(gs, validMoves, timeLimit=3.0):
    global nextMove
    startTime = time.time()
    nextMove = None
    random.shuffle(validMoves)
    for depth in range(1, DEPTH + 1):
        if time.time() - startTime > timeLimit:
            break
        findMoveNegaMaxAlphaBeta(gs, validMoves, depth, -CHECKMATE, CHECKMATE, 1 if gs.whiteToMove else -1)
    return nextMove

def findMoveNegaMaxAlphaBeta(gs, validMoves, depth, alpha, beta, turnMultiplier):
    global nextMove

    if depth == 0:
        return turnMultiplier * scoreBoard(gs)

    maxScore = -CHECKMATE

    for move in validMoves:
        gs.makeMove(move)
        gs.getLegalMoves()
        gs.getValidMoves()
        score = - findMoveNegaMaxAlphaBeta(gs, gs.validMoves, depth-1, -beta, -alpha, -turnMultiplier)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move
        gs.undoMove()
        if maxScore > alpha:
            alpha = maxScore
        if alpha >= beta:
            break

    return maxScore


def scoreBoard(gs):
    if gs.gameOver:
        if gs.whiteToMove:
            return -CHECKMATE
        else:
            return CHECKMATE
    score = 0
    for row in gs.board:
        for col in row:
            if col[0] == "w":
                score += pieceScore[col[1]]
            elif col[0] == "b":
                score -= pieceScore[col[1]]

    return score


