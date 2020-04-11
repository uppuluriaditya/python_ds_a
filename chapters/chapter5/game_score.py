
class GameEntry:
    """ Represents a single entry in a high scoring list """

    def __init__(self, name, score):
        self._name = name
        self._score = score
    
    def get_name(self):
        return self._name
    
    def get_score(self):
        return self._score

    def __str__(self):
        return '({}, {})'.format(self.get_name(), self.get_score())

class Scoreboard:
    """ Fixed length high score board """
    def __init__(self, capacity=10):
        self._board = [None] * capacity # list to track all the high scores
        self._n = 0 #Number of entries

    def __get_item__(self, k):
        """ Returns the item at the specified index """
        return self._board[k]
    
    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))
    
    def add(self, entry):
        score = entry.get_score()
        is_good_score = self._n < len(self._board) or score > self._board[-1].get_score()

        if is_good_score:
            if self._n < len(self._board):
                self._n += 1
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry


if __name__ == "__main__":
    score_card = Scoreboard(5)
    score_card.add(GameEntry('Aditya', 100))
    score_card.add(GameEntry('Aiswarya', 565))
    score_card.add(GameEntry('Pratibha', 98))
    score_card.add(GameEntry('Srividya', 123))
    score_card.add(GameEntry('Aditya', 67))
    score_card.add(GameEntry('Aiswarya', 620))

    print(score_card)