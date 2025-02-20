
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

    def makeMove(self, move):
        self.pawnMove(move)
        self.knightMove(move)
        if move.moveId in self.legalMoves:
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.whiteToMove = not self.whiteToMove
            self.moves.append(move)
        self.legalMoves = []

    def undoMove(self):
        if len(self.moves) == 0:
            return
        move = self.moves.pop()
        self.board[move.startRow][move.startCol] = move.pieceMoved
        self.board[move.endRow][move.endCol] = move.pieceCaptured
        self.whiteToMove = not self.whiteToMove

    def pawnMove(self, move):
        if self.whiteToMove == True:
            if move.startRow == 6 and self.board[move.startRow - 2][move.startCol] == "--":
                legalMove = (move.startRow, move.startCol, move.startRow - 2, move.startCol)
                self.legalMoves.append(legalMove)

            if move.startRow >= 1:
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

            if move.startRow <= 6:
                if self.board[move.startRow + 1][move.startCol] == "--":
                    legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol)
                    self.legalMoves.append(legalMove)

                if  move.startCol > 0 and self.board[move.startRow + 1][move.startCol - 1][0] == "w":
                    legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol - 1)
                    self.legalMoves.append(legalMove)

                if  move.startCol < 7 and self.board[move.startRow + 1][move.startCol + 1][0] == "w":
                    legalMove = (move.startRow, move.startCol, move.startRow + 1, move.startCol + 1)
                    self.legalMoves.append(legalMove)

    def knightMove(self, move):
        if self.whiteToMove == True:
            color = "w"
        else:
            color = "b"

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














