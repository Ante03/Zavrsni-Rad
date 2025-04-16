

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
        self.validMoves = []
        self.specificMoves = []
        self.checkKing = []
        self.whiteKingPosition = [7, 4]
        self.blackKingPosition = [0, 4]
        self.gameOver = False

    def makeMove(self, move):
        if (self.whiteToMove and self.board[move.startRow][move.startCol][0] != "w") or (not self.whiteToMove and self.board[move.startRow][move.startCol][0] != "b"):
            return

        if(move.startRow == 7 and move.startCol == 4 and move.endRow == 7 and move.endCol == 7 and self.board[move.startRow][move.startCol] == "wK"):
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = "--"
            self.board[7][5] = "wR"
            self.board[7][6] = "wK"
            self.whiteKingPosition[0] = 7
            self.whiteKingPosition[1] = 6
            self.moves.append(move)
            self.whiteToMove = not self.whiteToMove
        elif (move.startRow == 7 and move.startCol == 4 and move.endRow == 7 and move.endCol == 0 and self.board[move.startRow][move.startCol] == "wK"):
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = "--"
            self.board[7][3] = "wR"
            self.board[7][2] = "wK"
            self.whiteKingPosition[0] = 7
            self.whiteKingPosition[1] = 2
            self.moves.append(move)
            self.whiteToMove = not self.whiteToMove
        elif (move.startRow == 0 and move.startCol == 4 and move.endRow == 0 and move.endCol == 0 and self.board[move.startRow][move.startCol] == "bK"):
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = "--"
            self.board[0][3] = "bR"
            self.board[0][2] = "bK"
            self.blackKingPosition[0] = 0
            self.blackKingPosition[1] = 6
            self.moves.append(move)
            self.whiteToMove = not self.whiteToMove
        elif (move.startRow == 0 and move.startCol == 4 and move.endRow == 0 and move.endCol == 7 and self.board[move.startRow][move.startCol] == "bK"):
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = "--"
            self.board[0][5] = "bR"
            self.board[0][6] = "bK"
            self.blackKingPosition[0] = 0
            self.blackKingPosition[1] = 2
            self.moves.append(move)
            self.whiteToMove = not self.whiteToMove
        else:
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.moves.append(move)
            self.whiteToMove = not self.whiteToMove
        if move.pieceMoved == "wK":
            self.whiteKingPosition[0] = move.endRow
            self.whiteKingPosition[1] = move.endCol
        elif move.pieceMoved == "bK":
            self.blackKingPosition[0] = move.endRow
            self.blackKingPosition[1] = move.endCol

    def makeSpecificMove(self, move):
        if (self.whiteToMove and self.board[move.startRow][move.startCol][0] != "w") or (not self.whiteToMove and self.board[move.startRow][move.startCol][0] != "b"):
            return

        if(move.startRow == 7 and move.startCol == 4 and move.endRow == 7 and move.endCol == 7):
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = "--"
            self.board[7][5] = "wR"
            self.board[7][6] = "wK"
            self.whiteKingPosition[0] = 7
            self.whiteKingPosition[1] = 6
            self.moves.append(move)
            self.whiteToMove = not self.whiteToMove
        elif (move.startRow == 7 and move.startCol == 4 and move.endRow == 7 and move.endCol == 0):
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = "--"
            self.board[7][3] = "wR"
            self.board[7][2] = "wK"
            self.whiteKingPosition[0] = 7
            self.whiteKingPosition[1] = 2
            self.moves.append(move)
            self.whiteToMove = not self.whiteToMove
        elif (move.startRow == 0 and move.startCol == 4 and move.endRow == 0 and move.endCol == 0):
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = "--"
            self.board[0][3] = "bR"
            self.board[0][2] = "bK"
            self.blackKingPosition[0] = 0
            self.blackKingPosition[1] = 6
            self.moves.append(move)
            self.whiteToMove = not self.whiteToMove
        elif (move.startRow == 0 and move.startCol == 4 and move.endRow == 0 and move.endCol == 7):
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = "--"
            self.board[0][5] = "bR"
            self.board[0][6] = "bK"
            self.blackKingPosition[0] = 0
            self.blackKingPosition[1] = 2
            self.moves.append(move)
            self.whiteToMove = not self.whiteToMove

    def getLegalMoves(self):
        self.legalMoves = []
        self.specificMoves = []
        color = "w" if self.whiteToMove else "b"

        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece == "--" or piece[0] != color:
                    continue

                pieceType = piece[1]
                if pieceType == "P":
                    self.pawnMove(i, j)
                elif pieceType == "N":
                    self.knightMove(i, j)
                elif pieceType == "R":
                    self.rockMove(i, j)
                elif pieceType == "B":
                    self.bishopMove(i, j)
                elif pieceType == "Q":
                    self.bishopMove(i, j)
                    self.rockMove(i, j)
                elif pieceType == "K":
                    self.kingMove(i, j)
                    self.castling(i, j)

    def getValidMoves(self):
        moves = self.legalMoves.copy() + self.specificMoves.copy()
        self.validMoves = []
        for move in moves:
            mv = Move([move[0], move[1]], [move[2], move[3]], self.board)
            self.makeMove(mv)
            self.checkChecks()
            if len(self.checkKing) == 0:
                self.validMoves.append(mv)
            self.undoMove()

    def checkChecks(self):
        self.checkKing = []
        if self.whiteToMove == True:
            color = "w"
            for i in range(8):
                for j in range(8):
                    if self.board[i][j][0] == color:
                        if self.board[i][j][1] == "P":
                            self.checkPawnMove(i, j)
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
                            self.checkPawnMove(i, j)
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

    def isCheckmate(self):
        self.getLegalMoves()
        if len(self.legalMoves) == 0:
            if self.isKingInCheck():
                print("Šah-mat!")
                self.gameOver = True
                return True
            else:
                print("Pat! Neriješeno.")
                self.gameOver = True
                return False
        return False

    def undoMove(self):
        if len(self.moves) == 0:
            return
        move = self.moves.pop()

        if(move.startRow == 7 and move.startCol == 4 and move.endRow == 7 and move.endCol == 7 and move.pieceMoved == "wK"):
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = "wR"
            self.board[7][5] = "--"
            self.board[7][6] = "--"
            self.whiteKingPosition[0] = 7
            self.whiteKingPosition[1] = 4
            self.whiteToMove = not self.whiteToMove
        elif (move.startRow == 7 and move.startCol == 4 and move.endRow == 7 and move.endCol == 0 and move.pieceMoved == "wK"):
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = "wR"
            self.board[7][1] = "--"
            self.board[7][2] = "--"
            self.board[7][3] = "--"
            self.whiteKingPosition[0] = 7
            self.whiteKingPosition[1] = 4
            self.whiteToMove = not self.whiteToMove
        elif (move.startRow == 0 and move.startCol == 4 and move.endRow == 0 and move.endCol == 7 and move.pieceMoved == "bK"):
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = "bR"
            self.board[0][5] = "--"
            self.board[0][6] = "--"
            self.blackKingPosition[0] = 0
            self.blackKingPosition[1] = 4
            self.whiteToMove = not self.whiteToMove
        elif (move.startRow == 0 and move.startCol == 4 and move.endRow == 0 and move.endCol == 0 and move.pieceMoved == "bK"):
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = "bR"
            self.board[0][1] = "--"
            self.board[0][2] = "--"
            self.board[0][3] = "--"
            self.blackKingPosition[0] = 0
            self.blackKingPosition[1] = 4
            self.whiteToMove = not self.whiteToMove
        else:
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    def isKingInCheck(self):
        self.checkChecks()
        return len(self.checkKing) > 0

    def pawnMove(self, startRow, startCol):
        direction = -1 if self.whiteToMove else 1
        enemyColor = "b" if self.whiteToMove else "w"

        if self.board[startRow + direction][startCol] == "--":
            self.legalMoves.append((startRow, startCol, startRow + direction, startCol))

            if (self.whiteToMove and startRow == 6) or (not self.whiteToMove and startRow == 1):
                if self.board[startRow + 2 * direction][startCol] == "--":
                    self.legalMoves.append((startRow, startCol, startRow + 2 * direction, startCol))

        for side in [-1, 1]:
            newCol = startCol + side
            if 0 <= newCol < 8 and self.board[startRow + direction][newCol][0] == enemyColor:
                self.legalMoves.append((startRow, startCol, startRow + direction, newCol))

    def checkPawnMove(self, startRow, startCol):
        direction = -1 if self.whiteToMove else 1
        enemyKing = "bK" if self.whiteToMove else "wK"

        for side in [-1, 1]:
            newRow, newCol = startRow + direction, startCol + side
            if 0 <= newRow < 8 and 0 <= newCol < 8 and self.board[newRow][newCol] == enemyKing:
                self.checkKing.append((startRow, startCol, newRow, newCol))

    def knightMove(self, startRow, startCol):
        color = "w" if self.whiteToMove else "b"
        knightMoves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

        for dr, dc in knightMoves:
            newRow, newCol = startRow + dr, startCol + dc
            if 0 <= newRow < 8 and 0 <= newCol < 8 and self.board[newRow][newCol][0] != color:
                self.legalMoves.append((startRow, startCol, newRow, newCol))

    def checkKnightMove(self, startRow, startCol, row, col):
        oppositeColor = "b" if self.whiteToMove else "w"
        knightMoves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

        for dr, dc in knightMoves:
            newRow, newCol = startRow + dr, startCol + dc
            if 0 <= newRow < 8 and 0 <= newCol < 8:
                if self.board[newRow][newCol] == oppositeColor + "K":
                    self.checkKing.append((startRow, startCol, newRow, newCol))

    def rockMove(self, startRow, startCol):
        oppositeColor = "b" if self.whiteToMove else "w"
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            for i in range(1, 8):
                newRow, newCol = startRow + dr * i, startCol + dc * i
                if 0 <= newRow < 8 and 0 <= newCol < 8:
                    piece = self.board[newRow][newCol]
                    if piece == "--":
                        self.legalMoves.append((startRow, startCol, newRow, newCol))
                    elif piece[0] == oppositeColor:
                        self.legalMoves.append((startRow, startCol, newRow, newCol))
                        break
                    else:
                        break
                else:
                    break

    def checkRockMove(self, startRow, startCol, row, col):
        oppositeColor = "b" if self.whiteToMove else "w"
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            for i in range(1, 8):
                newRow, newCol = startRow + dr * i, startCol + dc * i
                if 0 <= newRow < 8 and 0 <= newCol < 8:
                    piece = self.board[newRow][newCol]
                    if piece == oppositeColor + "K":
                        self.checkKing.append((startRow, startCol, newRow, newCol))
                        break
                    elif piece[0] == oppositeColor or piece[0] == self.board[startRow][startCol][0]:
                        break
                else:
                    break

    def bishopMove(self, startRow, startCol):
        oppositeColor = "b" if self.whiteToMove else "w"
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

        for dr, dc in directions:
            for i in range(1, 8):
                newRow, newCol = startRow + dr * i, startCol + dc * i
                if 0 <= newRow < 8 and 0 <= newCol < 8:
                    piece = self.board[newRow][newCol]
                    if piece == "--":
                        self.legalMoves.append((startRow, startCol, newRow, newCol))
                    elif piece[0] == oppositeColor:
                        self.legalMoves.append((startRow, startCol, newRow, newCol))
                        break
                    else:
                        break
                else:
                    break

    def checkBishopMove(self, startRow, startCol, row, col):
        oppositeColor = "b" if self.whiteToMove else "w"
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

        for dr, dc in directions:
            for i in range(1, 8):
                newRow, newCol = startRow + dr * i, startCol + dc * i
                if 0 <= newRow < 8 and 0 <= newCol < 8:
                    piece = self.board[newRow][newCol]
                    if piece == oppositeColor + "K":
                        self.checkKing.append((startRow, startCol, newRow, newCol))
                        break
                    elif piece[0] == oppositeColor or piece[0] == self.board[startRow][startCol][0]:
                        break
                else:
                    break

    def kingMove(self, startRow, startCol):
        color = "w" if self.whiteToMove else "b"
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dr, dc in directions:
            newRow, newCol = startRow + dr, startCol + dc
            if 0 <= newRow < 8 and 0 <= newCol < 8:
                if self.board[newRow][newCol][0] != color:
                    self.legalMoves.append((startRow, startCol, newRow, newCol))

    def checkKingMove(self, startRow, startCol, row, col):
        oppositeColor = "b" if self.whiteToMove else "w"
        directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dr, dc in directions:
            newRow, newCol = startRow + dr, startCol + dc
            if 0 <= newRow < 8 and 0 <= newCol < 8:
                if self.board[newRow][newCol] == oppositeColor + "K":  # Provjera šaha
                    self.checkKing.append((startRow, startCol, newRow, newCol))

    def castling(self, startRow, startCol):
        color = "w" if self.whiteToMove else "b"
        if self.board[startRow][startCol][0] == "w":
            if self.board[7][5] == "--" and self.board[7][6] == "--" and self.board[7][7] == "wR":
                self.specificMoves.append((startRow, startCol, 7, 7))
            if self.board[7][1] == "--" and self.board[7][2] == "--" and self.board[7][3] == "--" and self.board[7][0] == "wR":
                self.specificMoves.append((startRow, startCol, 7, 0))
        elif self.board[startRow][startCol][0] == "b":
            if self.board[0][5] == "--" and self.board[0][6] == "--" and self.board[0][7] == "bR":
                self.specificMoves.append((startRow, startCol, 0, 7))
            if self.board[0][1] == "--" and self.board[0][2] == "--" and self.board[0][3] == "--" and self.board[0][0] == "bR":
                self.specificMoves.append((startRow, startCol, 0, 0))

    def get_promotion_choice(self):
        pass
        #while True:
            #for event in p.event.get():
                #if event.type == p.KEYDOWN:
                    #if event.key == p.K_q:
                        #return "Q"
                    #elif event.key == p.K_n:
                        #return "N"
                    #elif event.key == p.K_b:
                        #return "B"
                    #elif event.key == p.K_r:
                        #return "R"



    """def elpassantAndPromotion(self):
        if self.board[3] == "wP" and (move.endCol == move.startCol - 1 or move.endCol == move.startCol + 1):
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

        elif move.startRow == 4 and self.board[move.startRow][move.startCol] == "bP" and (move.endCol == move.startCol - 1 or move.endCol == move.startCol + 1):
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
                self.undoMove()"""



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

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveId == other.moveId
        return False

    def __hash__(self):
        return hash(self.moveId)

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, row, col):
        return self.colsToFiles[col] + self.rowsToRanks[row]


