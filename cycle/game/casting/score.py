from game.casting.actor import Actor


class Score(Actor):
   
    def __init__(self,player):
        super().__init__()
        self._points = 0
        self.player = player
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Player{self.player}: {self._points}")