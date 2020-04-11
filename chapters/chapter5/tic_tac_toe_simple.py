
class TicTacToe:
    """ Simple Management of Tic Tac Toe game """

    def __init__(self):
        """ Start a New game """
        self._board = [[' '] * 3 for i in range(3)]
        self._player = 'X'
    
    def mark(self, i, j):
        """ Put 'X' or 'O' mark at position (i, j) for the next players turn """
        if not(0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Invalid Board Position")
        if self._board[i][j] != ' ':
            raise ValueError("Board Position Occupied")
        if self.winner() is not None:
            raise ValueError("Game is already complete")
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'
    
    def _is_win(self, mark):
        """ Check whether the board configuration is a win for the given player """
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or # row 0
                mark == board[1][0] == board[1][1] == board[1][2] or # row 1
                mark == board[2][0] == board[2][1] == board[2][2] or # row 
                mark == board[0][0] == board[1][0] == board[2][0] or # column 0
                mark == board[0][1] == board[1][1] == board[2][1] or # column 1
                mark == board[0][2] == board[1][2] == board[2][2] or # column 2
                mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
                mark == board[0][2] == board[1][1] == board[2][0]) # rev diag
    
    def winner(self):
        """ Return the mark of winning player. or None to indicate tie """
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None
    
    def __str__(self):
        """ Returns string representation of the current board """
        rows = [' | ' .join(self._board[r]) for r in range(3)]
        return '\n------------\n'.join(rows)

if __name__ == "__main__":
    game = TicTacToe()
    game.mark(1, 1) # X
    game.mark(0, 2)
    game.mark(2, 2) # X
    game.mark(0, 0)
    game.mark(0, 1) # X
    game.mark(2, 1)
    game.mark(1, 2) # X
    game.mark(1, 0)
    game.mark(2, 0) # X

    print(game)

    winner = game.winner()
    if winner is None:
        print('Tie')
    else:
        print(winner, 'wins')
