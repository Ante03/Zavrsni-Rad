import pygame as p

class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moves = []
        self.legalMoves = []
        self.checkKing = []
        self.whiteKingPosition = [7, 4]
        self.blackKingPosition = [0, 4]


    def makeMove(self, move):
        if (self.whiteToMove and self.board[move.startRow][move.startCol][0] != "w") or (not self.whiteToMove and self.board[move.startRow][move.startCol][0] != "b"):
            return

        self.legalMoves = []
        if self.board[move.startRow][move.startCol][1] == "P":
            self.pawnMove(move)
        elif self.board[move.startRow][move.startCol][1] == "N":
            self.knightMove(move)
        elif self.board[move.startRow][move.startCol][1] == "R":
            self.rockMove(move)
        elif self.board[move.startRow][move.startCol][1] == "B":
            self.bishopMove(move)
        elif self.board[move.startRow][move.startCol][1] == "Q":
            self.bishopMove(move)
            self.rockMove(move)
        elif self.board[move.startRow][move.startCol][1] == "K":
            self.kingMove(move)

        if move.moveId in self.legalMoves:
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.moves.append(move)
            self.whiteToMove = not self.whiteToMove
            self.checkChecks()
            if len(self.checkKing) > 0:
                self.undoMove()

        else:
            self.castling(move)
            self.elpassantAndPromotion(move)

        self.legalMoves = []

    def checkChecks(self):
        self.checkKing = []
        if self.whiteToMove == True:
            color = "w"
            for i in range(8):
                for j in range(8):
                    if self.board[i][j][0] == color:
                        if self.board[i][j][1] == "P":
                            self.checkPawnMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                        elif self.board[i][j][1] == "N":
                            self.checkKnightMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                        elif self.board[i][j][1] == "R":
                            self.checkRockMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                        elif self.board[i][j][1] == "B":
                            self.checkBishopMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                        elif self.board[i][j][1] == "Q":
                            self.checkBishopMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                            self.checkRockMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                        elif self.board[i][j][1] == "K":
                            self.checkKingMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
        else:
            color = "b"
            for i in range(8):
                for j in range(8):
                    if self.board[i][j][0] == color:
                        if self.board[i][j][1] == "P":
                            self.checkPawnMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                        elif self.board[i][j][1] == "N":
                            self.checkKnightMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                        elif self.board[i][j][1] == "R":
                            self.checkRockMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                        elif self.board[i][j][1] == "B":
                            self.checkBishopMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                        elif self.board[i][j][1] == "Q":
                            self.checkBishopMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                            self.checkRockMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                        elif self.board[i][j][1] == "K":
                            self.checkKingMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])

    def undoMove(self):
        if len(self.moves) == 0:
            return
        move = self.moves.pop()
        if move.pieceMoved == "wK":
            self.whiteKingPosition[0] = move.startRow
            self.whiteKingPosition[1] = move.startCol
        if move.pieceMoved == "bK":
            self.blackKingPosition[0] = move.startRow
            self.blackKingPosition[1] = move.startCol
            print("AAAA")

        if len(self.moves) != 0:
            lastMove = self.moves.pop()
            self.moves.append(lastMove)

        if move.startRow == 7 and move.startCol == 4 and move.endRow == 7 and move.pieceMoved == "wK":
            if move.endCol == 7:
                self.board[move.startRow][move.startCol] = "wK"
                self.board[move.endRow][move.endCol] = "wR"
                self.board[7][5] = "--"
                self.board[7][6] = "--"
                self.whiteToMove = not self.whiteToMove
            elif move.endCol == 0:
                self.board[move.startRow][move.startCol] = "wK"
                self.board[move.endRow][move.endCol] = "wR"
                self.board[7][1] = "--"
                self.board[7][2] = "--"
                self.board[7][3] = "--"
                self.whiteToMove = not self.whiteToMove
        elif move.startRow == 0 and move.startCol == 4 and move.endRow == 0 and move.pieceMoved == "bK":
            if move.endCol == 7:
                self.board[move.startRow][move.startCol] = "bK"
                self.board[move.endRow][move.endCol] = "bR"
                self.board[0][5] = "--"
                self.board[0][6] = "--"
                self.whiteToMove = not self.whiteToMove
            elif move.endCol == 0:
                self.board[move.startRow][move.startCol] = "bK"
                self.board[move.endRow][move.endCol] = "bR"
                self.board[0][1] = "--"
                self.board[0][2] = "--"
                self.board[0][3] = "--"
                self.whiteToMove = not self.whiteToMove

        elif move.startRow == 3 and move.pieceMoved == "wP" and lastMove.pieceMoved == "bP" and lastMove.startRow == 1 and lastMove.endRow == 3 and (lastMove.startCol == move.startCol - 1 or lastMove.startCol == move.startCol + 1):
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = "--"
            self.board[move.endRow + 1][move.endCol] = "bP"
            self.whiteToMove = not self.whiteToMove

        elif move.startRow == 4 and move.pieceMoved == "bP" and lastMove.pieceMoved == "wP" and lastMove.startRow == 6 and lastMove.endRow == 4 and (lastMove.startCol == move.startCol - 1 or lastMove.startCol == move.startCol + 1):
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = "--"
            self.board[move.endRow - 1][move.endCol] = "wP"
            self.whiteToMove = not self.whiteToMove

        elif self.whiteToMove and move.pieceMoved == "wP" and move.endRow == 0:
            self.board[move.startRow][move.startCol] = "wP"
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

        elif not self.whiteToMove and move.pieceMoved == "bP" and move.endRow == 7:
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove


        else:
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    def pawnMove(self, move):
        if self.whiteToMove == True:
            if move.startRow == 6 and self.board[move.startRow - 2][move.startCol] == "--":
                legalMove = (move.startRow, move.startCol, move.startRow - 2, move.startCol)
                self.legalMoves.append(legalMove)

            if move.startRow >= 2:
                if self.board[move.startRow - 1][move.startCol] == "--":
                    legalMove = (move.startRow, move.startCol, move.startRow - 1, move.startCol)
                    self.legalMoves.append(legalMove)

                if  move.startCol > 0 and self.board[move.startRow - 1][move.startCol - 1][0] == "b":
                    legalMove = (move.startRow, move.startCol, move.startRow - 1, move.startCol - 1)
                    self.legalMoves.append(legalMove)

                if move.startCol < 7 and self.board[move.startRow - 1][move.startCol + 1][0] == "b":
                    legalMove = (move.startRow, move.startCol, move.startRow - 1, move.startCol + 1)
                    self.legalMoves.append(legalMove)

        elif self.whiteToMove == False:
            if move.startRow == 1 and self.board[move.startRow + 2][move.startCol] == "--":
                legalMove = (move.startRow, move.startCol, move.startRow + 2, move.startCol)
                self.legalMoves.append(legalMove)

            if move.startRow <= 5:
                if self.board[move.startRow + 1][move.startCol] == "--":
                    legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol)
                    self.legalMoves.append(legalMove)

                if  move.startCol > 0 and self.board[move.startRow + 1][move.startCol - 1][0] == "w":
                    legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol - 1)
                    self.legalMoves.append(legalMove)

                if  move.startCol < 7 and self.board[move.startRow + 1][move.startCol + 1][0] == "w":
                    legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol + 1)
                    self.legalMoves.append(legalMove)

    def checkPawnMove(self, startRow, startCol, row, col):
        if self.whiteToMove == True:
            if startRow >= 1:
                if startCol > 0 and startRow - 1 == row and startCol - 1 == col:
                    checkMove = (startRow, startCol, startRow - 1, startCol - 1)
                    self.checkKing.append(checkMove)


                if startCol < 7 and startRow - 1 == row and startCol + 1 == col:
                    checkMove = (startRow, startCol, startRow - 1, startCol + 1)
                    self.checkKing.append(checkMove)
        else:
            if startRow <= 6:
                if startCol > 0 and startRow + 1 == row and startCol - 1 == col:
                    checkMove = (startRow, startCol, startRow + 1, startCol - 1)
                    self.checkKing.append(checkMove)

                if startCol < 7 and startRow + 1 == row and startCol + 1 == col:
                    checkMove = (startRow, startCol, startRow + 1, startCol + 1)
                    self.checkKing.append(checkMove)

    def knightMove(self, move):
        if self.whiteToMove == True:
            color = "w"
            oppositeColor = "b"
        else:
            color = "b"
            oppositeColor = "w"
        if move.startRow > 1:
            if move.startCol - 1 >= 0 and self.board[move.startRow - 2][move.startCol - 1][0] != color:
                legalMove = (move.startRow, move.startCol, move.startRow - 2, move.startCol - 1)
                self.legalMoves.append(legalMove)
            if move.startCol + 1 <= 7 and self.board[move.startRow - 2][move.startCol + 1][0] != color:
                legalMove = (move.startRow, move.startCol, move.startRow - 2, move.startCol + 1)
                self.legalMoves.append(legalMove)
        if move.startRow < 6:
            if move.startCol - 1 >= 0 and self.board[move.startRow + 2][move.startCol - 1][0] != color:
                legalMove = (move.startRow, move.startCol, move.startRow + 2, move.startCol - 1)
                self.legalMoves.append(legalMove)
            if move.startCol + 1 <= 7 and self.board[move.startRow + 2][move.startCol + 1][0] != color:
                legalMove = (move.startRow, move.startCol, move.startRow + 2, move.startCol + 1)
                self.legalMoves.append(legalMove)
        if move.startRow > 0:
            if move.startCol - 2 >= 0 and self.board[move.startRow - 1][move.startCol - 2][0] != color:
                legalMove = (move.startRow, move.startCol, move.startRow - 1, move.startCol - 2)
                self.legalMoves.append(legalMove)
            if move.startCol + 2 <= 7 and self.board[move.startRow - 1][move.startCol + 2][0] != color:
                legalMove = (move.startRow, move.startCol, move.startRow - 1, move.startCol + 2)
                self.legalMoves.append(legalMove)
        if move.startRow < 7:
            if move.startCol - 2 >= 0 and self.board[move.startRow + 1][move.startCol - 2][0] != color:
                legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol - 2)
                self.legalMoves.append(legalMove)
            if move.startCol + 2 <= 7 and self.board[move.startRow + 1][move.startCol + 2][0] != color:
                legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol + 2)
                self.legalMoves.append(legalMove)

    def checkKnightMove(self, startRow, startCol, row, col):
        if self.whiteToMove == True:
            color = "w"
        else:
            color = "b"
        if startRow > 1:
            if startCol - 1 >= 0 and self.board[startRow - 2][startCol - 1][0] != color:
                if startRow - 2 == row and startCol - 1 == col:
                    checkMove = (startRow, startCol, startRow - 2, startCol - 1)
                    self.checkKing.append(checkMove)
            if startCol + 1 <= 7 and self.board[startRow - 2][startCol + 1][0] != color:
                if startRow - 2 == row and startCol + 1 == col:
                    checkMove = (startRow, startCol, startRow - 2, startCol + 1)
                    self.checkKing.append(checkMove)
        if startRow < 6:
            if startCol - 1 >= 0 and self.board[startRow + 2][startCol - 1][0] != color:
                if startRow + 2 == row and startCol - 1 == col:
                    checkMove = (startRow, startCol, startRow + 2, startCol - 1)
                    self.checkKing.append(checkMove)
            if startCol + 1 <= 7 and self.board[startRow + 2][startCol + 1][0] != color:
                if startRow + 2 == row and startCol + 1 == col:
                    checkMove = (startRow, startCol, startRow + 2, startCol + 1)
                    self.checkKing.append(checkMove)
        if startRow > 0:
            if startCol - 2 >= 0 and self.board[startRow - 1][startCol - 2][0] != color:
                if startRow - 1 == row and startCol - 2 == col:
                    checkMove = (startRow, startCol, startRow - 1, startCol - 2)
                    self.checkKing.append(checkMove)
            if startCol + 2 <= 7 and self.board[startRow - 1][startCol + 2][0] != color:
                if startRow - 1 == row and startCol + 2 == col:
                    checkMove = (startRow, startCol, startRow - 1, startCol + 2)
                    self.checkKing.append(checkMove)
        if startRow < 7:
            if startCol - 2 >= 0 and self.board[startRow + 1][startCol - 2][0] != color:
                if startRow + 1 == row and startCol - 2 == col:
                    checkMove = (startRow, startCol, startRow + 1, startCol - 2)
                    self.checkKing.append(checkMove)
            if startCol + 2 <= 7 and self.board[startRow + 1][startCol + 2][0] != color:
                if startRow + 1 == row and startCol + 2 == col:
                    checkMove = (startRow, startCol, startRow + 1, startCol + 2)
                    self.checkKing.append(checkMove)

    def rockMove(self, move):
        if self.whiteToMove == True:
            color = "w"
            oppositeColor = "b"
        else:
            color = "b"
            oppositeColor = "w"

        for i in range(1, 8 - move.startRow):
            if self.board[move.startRow + i][move.startCol] == "--":
                legalMove = (move.startRow, move.startCol, move.startRow + i, move.startCol)
                self.legalMoves.append(legalMove)
            elif self.board[move.startRow + i][move.startCol][0] == oppositeColor:
                legalMove = (move.startRow, move.startCol, move.startRow + i, move.startCol)
                self.legalMoves.append(legalMove)
                break
            elif self.board[move.startRow + i][move.startCol][0] == color:
                break

        for i in range(1, move.startRow + 1):
            if self.board[move.startRow - i][move.startCol] == "--":
                legalMove = (move.startRow, move.startCol, move.startRow - i, move.startCol)
                self.legalMoves.append(legalMove)
            elif self.board[move.startRow - i][move.startCol][0] == oppositeColor:
                legalMove = (move.startRow, move.startCol, move.startRow - i, move.startCol)
                self.legalMoves.append(legalMove)
                break
            elif self.board[move.startRow - i][move.startCol][0] == color:
                break

        for i in range(1, 8 - move.startCol):
            if self.board[move.startRow][move.startCol + i] == "--":
                legalMove = (move.startRow, move.startCol, move.startRow, move.startCol + i)
                self.legalMoves.append(legalMove)
            elif self.board[move.startRow][move.startCol + i][0] == oppositeColor:
                legalMove = (move.startRow, move.startCol, move.startRow, move.startCol + i)
                self.legalMoves.append(legalMove)
                break
            elif self.board[move.startRow][move.startCol + i][0] == color:
                break

        for i in range(1, move.startCol + 1):
            if self.board[move.startRow][move.startCol - i] == "--":
                legalMove = (move.startRow, move.startCol, move.startRow, move.startCol - i)
                self.legalMoves.append(legalMove)
            elif self.board[move.startRow][move.startCol - i][0] == oppositeColor:
                legalMove = (move.startRow, move.startCol, move.startRow, move.startCol - i)
                self.legalMoves.append(legalMove)
                break
            elif self.board[move.startRow][move.startCol - i][0] == color:
                break

    def checkRockMove(self, startRow, startCol, row, col):
        if self.whiteToMove == True:
            color = "w"
            oppositeColor = "b"
        else:
            color = "b"
            oppositeColor = "w"

        for i in range(1, 8 - startRow):
            if self.board[startRow + i][startCol][0] == oppositeColor:
                if startRow + i == row and startCol == col:
                    checkMove = (startRow, startCol, startRow + i, startCol)
                    self.checkKing.append(checkMove)
                break
            elif self.board[startRow + i][startCol][0] == color:
                break

        for i in range(1, startRow + 1):
            if self.board[startRow - i][startCol][0] == oppositeColor:
                if startRow - i == row and startCol == col:
                    checkMove = (startRow, startCol, startRow - i, startCol)
                    self.checkKing.append(checkMove)
                break
            elif self.board[startRow - i][startCol][0] == color:
                break

        for i in range(1, 8 - startCol):
            if self.board[startRow][startCol + i][0] == oppositeColor:
                if startRow == row and startCol + i == col:
                    checkMove = (startRow, startCol, startRow, startCol + i)
                    self.checkKing.append(checkMove)
                break
            elif self.board[startRow][startCol + i][0] == color:
                break

        for i in range(1, startCol + 1):
            if self.board[startRow][startCol - i][0] == oppositeColor:
                if startRow == row and startCol - i == col:
                    checkMove = (startRow, startCol, startRow, startCol - i)
                    self.checkKing.append(checkMove)
                break
            elif self.board[startRow][startCol - i][0] == color:
                break

    def bishopMove(self, move):
        if self.whiteToMove == True:
            color = "w"
            oppositeColor = "b"
        else:
            color = "b"
            oppositeColor = "w"

        for i in range(1, 8):
            if move.startCol + i > 7 or move.startRow + i > 7:
                break
            elif self.board[move.startRow + i][move.startCol + i] == "--":
                legalMove = (move.startRow, move.startCol, move.startRow + i, move.startCol + i)
                self.legalMoves.append(legalMove)
            elif self.board[move.startRow + i][move.startCol + i][0] == oppositeColor:
                legalMove = (move.startRow, move.startCol, move.startRow + i, move.startCol + i)
                self.legalMoves.append(legalMove)
                break
            elif self.board[move.startRow + i][move.startCol + i][0] == color:
                break

        for i in range(1, 8):
            if move.startCol - i > 7 or move.startRow + i > 7:
                break
            elif self.board[move.startRow + i][move.startCol - i] == "--":
                legalMove = (move.startRow, move.startCol, move.startRow + i, move.startCol - i)
                self.legalMoves.append(legalMove)
            elif self.board[move.startRow + i][move.startCol - i][0] == oppositeColor:
                legalMove = (move.startRow, move.startCol, move.startRow + i, move.startCol - i)
                self.legalMoves.append(legalMove)
                break
            elif self.board[move.startRow + i][move.startCol - i][0] == color:
                break

        for i in range(1, 8):
            if move.startCol + i > 7 or move.startRow - i > 7:
                break
            elif self.board[move.startRow - i][move.startCol + i] == "--":
                legalMove = (move.startRow, move.startCol, move.startRow - i, move.startCol + i)
                self.legalMoves.append(legalMove)
            elif self.board[move.startRow - i][move.startCol + i][0] == oppositeColor:
                legalMove = (move.startRow, move.startCol, move.startRow - i, move.startCol + i)
                self.legalMoves.append(legalMove)
                break
            elif self.board[move.startRow - i][move.startCol + i][0] == color:
                break

        for i in range(1, 8):
            if move.startCol - i > 7 or move.startRow - i > 7:
                break
            elif self.board[move.startRow - i][move.startCol - i] == "--":
                legalMove = (move.startRow, move.startCol, move.startRow - i, move.startCol - i)
                self.legalMoves.append(legalMove)
            elif self.board[move.startRow - i][move.startCol - i][0] == oppositeColor:
                legalMove = (move.startRow, move.startCol, move.startRow - i, move.startCol - i)
                self.legalMoves.append(legalMove)
                break
            elif self.board[move.startRow - i][move.startCol - i][0] == color:
                break

    def checkBishopMove(self, startRow, startCol, row, col):
        if self.whiteToMove == True:
            color = "w"
            oppositeColor = "b"
        else:
            color = "b"
            oppositeColor = "w"

        for i in range(1, 8):
            if startRow + i > 7 or startCol + i > 7:
                break
            elif self.board[startRow + i][startCol + i][0] == oppositeColor:
                if startRow + i == row and startCol + i == col:
                    checkMove = (startRow, startCol, startRow + i, startCol + i)
                    self.checkKing.append(checkMove)
                break
            elif self.board[startRow + i][startCol + i][0] == color:
                break

        for i in range(1, 8):
            if startRow + i > 7 or startCol - i < 0:
                break
            elif self.board[startRow + i][startCol - i][0] == oppositeColor:
                if startRow + i == row and startCol - i == col:
                    checkMove = (startRow, startCol, startRow + i, startCol - i)
                    self.checkKing.append(checkMove)
                break
            elif self.board[startRow + i][startCol - i][0] == color:
                break

        for i in range(1, 8):
            if startRow - i < 0 or startCol + i > 7:
                break
            elif self.board[startRow - i][startCol + i][0] == oppositeColor:
                if startRow - i == row and startCol + i == col:
                    checkMove = (startRow, startCol, startRow - i, startCol + i)
                    self.checkKing.append(checkMove)
                break
            elif self.board[startRow - i][startCol + i][0] == color:
                break

        for i in range(1, 8):
            if startRow - i < 0 or startCol - i < 0:
                break
            elif self.board[startRow - i][startCol - i][0] == oppositeColor:
                if startRow - i == row and startCol - i == col:
                    checkMove = (startRow, startCol, startRow - i, startCol - i)
                    self.checkKing.append(checkMove)
                break
            elif self.board[startRow - i][startCol - i][0] == color:
                break

    def kingMove(self, move):
        if self.whiteToMove == True:
            color = "w"
            if move.startRow - 1 >= 0:
                if self.board[move.startRow - 1][move.startCol][0] != color:
                    legalMove = (move.startRow, move.startCol, move.startRow - 1, move.startCol)
                    self.legalMoves.append(legalMove)
                if move.startCol - 1 >= 0:
                    if self.board[move.startRow - 1][move.startCol - 1][0] != color:
                        legalMove = (move.startRow, move.startCol, move.startRow - 1, move.startCol - 1)
                        self.legalMoves.append(legalMove)
                if move.startCol + 1 <= 7:
                    if self.board[move.startRow - 1][move.startCol + 1][0] != color:
                        legalMove = (move.startRow, move.startCol, move.startRow - 1, move.startCol + 1)
                        self.legalMoves.append(legalMove)

            if move.startRow + 1 <= 7:
                if self.board[move.startRow + 1][move.startCol][0] != color:
                    legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol)
                    self.legalMoves.append(legalMove)
                if move.startCol - 1 >= 0:
                    if self.board[move.startRow + 1][move.startCol - 1][0] != color:
                        legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol - 1)
                        self.legalMoves.append(legalMove)
                if move.startCol + 1 <= 7:
                    if self.board[move.startRow + 1][move.startCol + 1][0] != color:
                        legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol + 1)
                        self.legalMoves.append(legalMove)

            if move.startCol - 1 >= 0 and self.board[move.startRow][move.startCol - 1][0] != color:
                legalMove = (move.startRow, move.startCol, move.startRow, move.startCol - 1)
                self.legalMoves.append(legalMove)

            if move.startCol + 1 <= 7 and self.board[move.startRow][move.startCol + 1][0] != color:
                legalMove = (move.startRow, move.startCol, move.startRow, move.startCol + 1)
                self.legalMoves.append(legalMove)

            if move.moveId in self.legalMoves:
                self.whiteKingPosition = [move.endRow, move.endCol]
                print(self.whiteKingPosition[0], self.whiteKingPosition[1])



        elif self.whiteToMove == False:
            color = "b"
            if move.startRow - 1 >= 0:
                if self.board[move.startRow - 1][move.startCol][0] != color:
                    legalMove = (move.startRow, move.startCol, move.startRow - 1, move.startCol)
                    self.legalMoves.append(legalMove)
                if move.startCol - 1 >= 0:
                    if self.board[move.startRow - 1][move.startCol - 1][0] != color:
                        legalMove = (move.startRow, move.startCol, move.startRow - 1, move.startCol - 1)
                        self.legalMoves.append(legalMove)
                if move.startCol + 1 <= 7:
                    if self.board[move.startRow - 1][move.startCol + 1][0] != color:
                        legalMove = (move.startRow, move.startCol, move.startRow - 1, move.startCol + 1)
                        self.legalMoves.append(legalMove)

            if move.startRow + 1 <= 7:
                if self.board[move.startRow + 1][move.startCol][0] != color:
                    legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol)
                    self.legalMoves.append(legalMove)
                if move.startCol - 1 >= 0:
                    if self.board[move.startRow + 1][move.startCol - 1][0] != color:
                        legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol - 1)
                        self.legalMoves.append(legalMove)
                if move.startCol + 1 <= 7:
                    if self.board[move.startRow + 1][move.startCol + 1][0] != color:
                        legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol + 1)
                        self.legalMoves.append(legalMove)

            if move.startCol - 1 >= 0 and self.board[move.startRow][move.startCol - 1][0] != color:
                legalMove = (move.startRow, move.startCol, move.startRow, move.startCol - 1)
                self.legalMoves.append(legalMove)

            if move.startCol + 1 <= 7 and self.board[move.startRow][move.startCol + 1][0] != color:
                legalMove = (move.startRow, move.startCol, move.startRow, move.startCol + 1)
                self.legalMoves.append(legalMove)

            if move.moveId in self.legalMoves:
                self.blackKingPosition = [move.endRow, move.endCol]
                print(self.blackKingPosition[0], self.blackKingPosition[1])

    def checkKingMove(self, startRow, startCol, row, col):
        if self.whiteToMove == True:
            oppositeColor = "b"
        else:
            oppositeColor = "w"

        if startRow - 1 >= 0:
            if startRow - 1 == row and startCol == col:
                checkMove = (startRow, startCol, startRow - 1, startCol)
                self.checkKing.append(checkMove)
            if startCol - 1 >= 0:
                if startRow - 1 == row and startCol - 1 == col:
                    checkMove = (startRow, startCol, startRow - 1, startCol - 1)
                    self.checkKing.append(checkMove)
            if startCol + 1 <= 7:
                if startRow - 1 == row and startCol + 1 == col:
                    checkMove = (startRow, startCol, startRow - 1, startCol + 1)
                    self.checkKing.append(checkMove)

        if startRow + 1 <= 7:
            if startRow + 1 == row and startCol == col:
                checkMove = (startRow, startCol, startRow + 1, startCol)
                self.checkKing.append(checkMove)
            if startCol - 1 >= 0:
                if startRow + 1 == row and startCol - 1 == col:
                    checkMove = (startRow, startCol, startRow + 1, startCol - 1)
                    self.checkKing.append(checkMove)
            if startCol + 1 <= 7:
                if startRow + 1 == row and startCol + 1 == col:
                    checkMove = (startRow, startCol, startRow + 1, startCol + 1)
                    self.checkKing.append(checkMove)

        if startCol - 1 >= 0 and startRow == row and startCol - 1 == col:
            checkMove = (startRow, startCol, startRow, startCol - 1)
            self.checkKing.append(checkMove)

        if startCol + 1 <= 7 and startRow == row and startCol + 1 == col:
            checkMove = (startRow, startCol, startRow, startCol + 1)
            self.checkKing.append(checkMove)

    def get_promotion_choice(self):
        while True:
            for event in p.event.get():
                if event.type == p.KEYDOWN:
                    if event.key == p.K_q:
                        return "Q"
                    elif event.key == p.K_n:
                        return "N"
                    elif event.key == p.K_b:
                        return "B"
                    elif event.key == p.K_r:
                        return "R"

    def castling(self, move):
        if move.startRow == 7 and move.startCol == 4:
            if move.endRow == 7 and move.endCol == 7 and all("wK" not in mv.pieceMoved for mv in self.moves) and \
                    self.board[7][5] == "--" and self.board[7][6] == "--":
                self.checkCastling(move)
                if len(self.checkKing) == 0:
                    self.board[move.startRow][move.startCol] = "--"
                    self.board[move.endRow][move.endCol] = "--"
                    self.board[7][6] = move.pieceMoved
                    self.board[7][5] = "wR"
                    self.whiteToMove = not self.whiteToMove
                    self.moves.append(move)
                    self.whiteKingPosition[0] = move.endRow
                    self.whiteKingPosition[1] = move.endCol

            elif move.endRow == 7 and move.endCol == 0 and all("wK" not in mv.pieceMoved for mv in self.moves) and \
                    self.board[7][3] == "--" and self.board[7][2] == "--" and self.board[7][1] == "--":
                self.checkCastling(move)
                if len(self.checkKing) == 0:
                    self.board[move.startRow][move.startCol] = "--"
                    self.board[move.endRow][move.endCol] = "--"
                    self.board[7][2] = move.pieceMoved
                    self.board[7][3] = "wR"
                    self.whiteToMove = not self.whiteToMove
                    self.moves.append(move)
                    self.whiteKingPosition[0] = move.endRow
                    self.whiteKingPosition[1] = move.endCol

        elif move.startRow == 0 and move.startCol == 4:
            if move.endRow == 0 and move.endCol == 7 and all("bK" not in mv.pieceMoved for mv in self.moves) and \
                    self.board[0][5] == "--" and self.board[0][6] == "--":
                self.checkCastling(move)
                if len(self.checkKing) == 0:
                    self.board[move.startRow][move.startCol] = "--"
                    self.board[move.endRow][move.endCol] = "--"
                    self.board[0][6] = move.pieceMoved
                    self.board[0][5] = "bR"
                    self.whiteToMove = not self.whiteToMove
                    self.moves.append(move)
                    self.blackKingPosition[0] = move.endRow
                    self.blackKingPosition[1] = move.endCol

            elif move.endRow == 0 and move.endCol == 0 and all("bK" not in mv.pieceMoved for mv in self.moves) and \
                    self.board[0][3] == "--" and self.board[0][2] == "--" and self.board[0][1] == "--":
                self.checkCastling(move)
                if len(self.checkKing) == 0:
                    self.board[move.startRow][move.startCol] = "--"
                    self.board[move.endRow][move.endCol] = "--"
                    self.board[0][2] = move.pieceMoved
                    self.board[0][3] = "bR"
                    self.whiteToMove = not self.whiteToMove
                    self.moves.append(move)
                    self.blackKingPosition[0] = move.endRow
                    self.blackKingPosition[1] = move.endCol

    def checkCastling(self, move):
        self.checkKing = []
        if self.whiteToMove == True:
            color = "b"
            self.whiteToMove = not self.whiteToMove
            for i in range(8):
                for j in range(8):
                    if self.board[i][j][0] == color:
                        if self.board[i][j][1] == "P":
                            if move.endCol == 7:
                                self.checkPawnMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                                self.checkPawnMove(i, j, 7, 5)
                                self.checkPawnMove(i, j, 7, 6)
                                self.checkPawnMove(i, j, 7, 7)
                            else:
                                self.checkPawnMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                                self.checkPawnMove(i, j, 7, 0)
                                self.checkPawnMove(i, j, 7, 1)
                                self.checkPawnMove(i, j, 7, 2)
                                self.checkPawnMove(i, j, 7, 3)

                        elif self.board[i][j][1] == "N":
                            if move.endCol == 7:
                                self.checkKnightMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                                self.checkKnightMove(i, j, 7, 5)
                                self.checkKnightMove(i, j, 7, 6)
                                self.checkKnightMove(i, j, 7, 7)
                            else:
                                self.checkKnightMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                                self.checkKnightMove(i, j, 7, 0)
                                self.checkKnightMove(i, j, 7, 1)
                                self.checkKnightMove(i, j, 7, 2)
                                self.checkKnightMove(i, j, 7, 3)
                        elif self.board[i][j][1] == "R":
                            if move.endCol == 7:
                                self.checkRockMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                                self.checkRockMove(i, j, 7, 5)
                                self.checkRockMove(i, j, 7, 6)
                                self.checkRockMove(i, j, 7, 7)
                            else:
                                self.checkRockMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                                self.checkRockMove(i, j, 7, 0)
                                self.checkRockMove(i, j, 7, 1)
                                self.checkRockMove(i, j, 7, 2)
                                self.checkRockMove(i, j, 7, 3)

                        elif self.board[i][j][1] == "B":
                            if move.endCol == 7:
                                self.checkBishopMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                                self.checkBishopMove(i, j, 7, 5)
                                self.checkBishopMove(i, j, 7, 6)
                                self.checkBishopMove(i, j, 7, 7)
                            else:
                                self.checkBishopMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                                self.checkBishopMove(i, j, 7, 0)
                                self.checkBishopMove(i, j, 7, 1)
                                self.checkBishopMove(i, j, 7, 2)
                                self.checkBishopMove(i, j, 7, 3)
                        elif self.board[i][j][1] == "Q":
                            if move.endCol == 7:
                                self.checkRockMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                                self.checkRockMove(i, j, 7, 5)
                                self.checkRockMove(i, j, 7, 6)
                                self.checkRockMove(i, j, 7, 7)
                                self.checkBishopMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                                self.checkBishopMove(i, j, 7, 5)
                                self.checkBishopMove(i, j, 7, 6)
                                self.checkBishopMove(i, j, 7, 7)
                            else:
                                self.checkRockMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                                self.checkRockMove(i, j, 7, 0)
                                self.checkRockMove(i, j, 7, 1)
                                self.checkRockMove(i, j, 7, 2)
                                self.checkRockMove(i, j, 7, 3)
                                self.checkBishopMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
                                self.checkBishopMove(i, j, 7, 0)
                                self.checkBishopMove(i, j, 7, 1)
                                self.checkBishopMove(i, j, 7, 2)
                                self.checkBishopMove(i, j, 7, 3)
                        elif self.board[i][j][1] == "K":
                            self.checkKingMove(i, j, self.whiteKingPosition[0], self.whiteKingPosition[1])
            self.whiteToMove = not self.whiteToMove

        else:
            self.whiteToMove = not self.whiteToMove
            color = "w"
            for i in range(8):
                for j in range(8):
                    if self.board[i][j][0] == color:
                        if self.board[i][j][1] == "P":
                            if move.endCol == 7:
                                self.checkPawnMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                                self.checkPawnMove(i, j, 0, 5)
                                self.checkPawnMove(i, j, 0, 6)
                                self.checkPawnMove(i, j, 0, 7)
                            else:
                                self.checkPawnMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                                self.checkPawnMove(i, j, 0, 0)
                                self.checkPawnMove(i, j, 0, 1)
                                self.checkPawnMove(i, j, 0, 2)
                                self.checkPawnMove(i, j, 0, 3)

                        elif self.board[i][j][1] == "N":
                            if move.endCol == 7:
                                self.checkKnightMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                                self.checkKnightMove(i, j, 0, 5)
                                self.checkKnightMove(i, j, 0, 6)
                                self.checkKnightMove(i, j, 0, 7)
                            else:
                                self.checkKnightMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                                self.checkKnightMove(i, j, 0, 0)
                                self.checkKnightMove(i, j, 0, 1)
                                self.checkKnightMove(i, j, 0, 2)
                                self.checkKnightMove(i, j, 0, 3)
                        elif self.board[i][j][1] == "R":
                            if move.endCol == 7:
                                self.checkRockMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                                self.checkRockMove(i, j, 0, 5)
                                self.checkRockMove(i, j, 0, 6)
                                self.checkRockMove(i, j, 0, 7)
                            else:
                                self.checkRockMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                                self.checkRockMove(i, j, 0, 0)
                                self.checkRockMove(i, j, 0, 1)
                                self.checkRockMove(i, j, 0, 2)
                                self.checkRockMove(i, j, 0, 3)

                        elif self.board[i][j][1] == "B":
                            if move.endCol == 7:
                                self.checkBishopMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                                self.checkBishopMove(i, j, 0, 5)
                                self.checkBishopMove(i, j, 0, 6)
                                self.checkBishopMove(i, j, 0, 7)
                            else:
                                self.checkBishopMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                                self.checkBishopMove(i, j, 0, 0)
                                self.checkBishopMove(i, j, 0, 1)
                                self.checkBishopMove(i, j, 0, 2)
                                self.checkBishopMove(i, j, 0, 3)
                        elif self.board[i][j][1] == "Q":
                            if move.endCol == 7:
                                self.checkRockMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                                self.checkRockMove(i, j, 0, 5)
                                self.checkRockMove(i, j, 0, 6)
                                self.checkRockMove(i, j, 0, 7)
                                self.checkBishopMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                                self.checkBishopMove(i, j, 0, 5)
                                self.checkBishopMove(i, j, 0, 6)
                                self.checkBishopMove(i, j, 0, 7)
                            else:
                                self.checkRockMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                                self.checkRockMove(i, j, 0, 0)
                                self.checkRockMove(i, j, 0, 1)
                                self.checkRockMove(i, j, 0, 2)
                                self.checkRockMove(i, j, 0, 3)
                                self.checkBishopMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
                                self.checkBishopMove(i, j, 0, 0)
                                self.checkBishopMove(i, j, 0, 1)
                                self.checkBishopMove(i, j, 0, 2)
                                self.checkBishopMove(i, j, 0, 3)
                        elif self.board[i][j][1] == "K":
                            self.checkKingMove(i, j, self.blackKingPosition[0], self.blackKingPosition[1])
            self.whiteToMove = not self.whiteToMove

    def elpassantAndPromotion(self, move):
        if move.startRow == 3 and self.board[move.startRow][move.startCol] == "wP" and move.endCol == (move.startCol - 1 or move.endCol == move.startCol + 1):
                lastMove = self.moves.pop()
                self.moves.append(lastMove)
                if lastMove.pieceMoved == "bP" and lastMove.startRow == 1 and lastMove.endRow == 3 and lastMove.startCol == move.startCol - 1:
                    self.board[move.startRow][move.startCol] = "--"
                    self.board[move.startRow - 1][move.startCol - 1] = move.pieceMoved
                    self.board[move.startRow][move.startCol - 1] = "--"
                    self.whiteToMove = not self.whiteToMove
                    self.moves.append(move)
                    self.checkChecks()
                    if len(self.checkKing) > 0:
                        self.undoMove()
                elif lastMove.pieceMoved == "bP" and lastMove.startRow == 1 and lastMove.endRow == 3 and lastMove.startCol == move.startCol + 1:
                    self.board[move.startRow][move.startCol] = "--"
                    self.board[move.startRow - 1][move.startCol + 1] = move.pieceMoved
                    self.board[move.startRow][move.startCol + 1] = "--"
                    self.whiteToMove = not self.whiteToMove
                    self.moves.append(move)
                    self.checkChecks()
                    if len(self.checkKing) > 0:
                        self.undoMove()

        elif move.startRow == 4 and self.board[move.startRow][move.startCol] == "bP" and move.endCol == (move.startCol - 1 or move.endCol == move.startCol + 1):
                lastMove = self.moves.pop()
                self.moves.append(lastMove)
                if lastMove.pieceMoved == "wP" and lastMove.startRow == 6 and lastMove.endRow == 4 and lastMove.startCol == move.startCol - 1:
                    self.board[move.startRow][move.startCol] = "--"
                    self.board[move.startRow + 1][move.startCol - 1] = move.pieceMoved
                    self.board[move.startRow][move.startCol - 1] = "--"
                    self.whiteToMove = not self.whiteToMove
                    self.moves.append(move)
                    self.checkChecks()
                    if len(self.checkKing) > 0:
                        self.undoMove()
                elif lastMove.pieceMoved == "wP" and lastMove.startRow == 6 and lastMove.endRow == 4 and lastMove.startCol == move.startCol + 1:
                    self.board[move.startRow][move.startCol] = "--"
                    self.board[move.startRow + 1][move.startCol + 1] = move.pieceMoved
                    self.board[move.startRow][move.startCol + 1] = "--"
                    self.whiteToMove = not self.whiteToMove
                    self.moves.append(move)
                    self.checkChecks()
                    if len(self.checkKing) > 0:
                        self.undoMove()


        elif self.whiteToMove and move.pieceMoved == "wP" and move.endRow == 0:
            promotion_piece = "w" + self.get_promotion_choice()
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = promotion_piece
            self.whiteToMove = not self.whiteToMove
            self.moves.append(move)
            self.checkChecks()
            if len(self.checkKing) > 0:
                self.undoMove()

        elif not self.whiteToMove and move.pieceMoved == "bP" and move.endRow == 7:
            promotion_piece = "b" + self.get_promotion_choice()
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = promotion_piece
            self.whiteToMove = not self.whiteToMove
            self.moves.append(move)
            self.checkChecks()
            if len(self.checkKing) > 0:
                self.undoMove()




class Move():
    ranksToRows = {"1" : 7, "2" : 6, "3" : 5, "4" : 4, "5" : 3, "6" : 2, "7" : 1, "8" : 0}
    rowsToRanks = {}
    for rank, row in ranksToRows.items():
        rowsToRanks[row] = rank

    filesToCols = {"h": 7, "g": 6, "f": 5, "e": 4, "d": 3, "c": 2, "b": 1, "a" : 0}
    colsToFiles = {}
    for file, col in filesToCols.items():
        colsToFiles[col] = file

    def __init__(self, startPoint, endPoint, board):
        self.startRow = startPoint[0]
        self.startCol = startPoint[1]
        self.endRow = endPoint[0]
        self.endCol = endPoint[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveId = (self.startRow, self.startCol, self.endRow, self.endCol)

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, row, col):
        return self.colsToFiles[col] + self.rowsToRanks[row]



