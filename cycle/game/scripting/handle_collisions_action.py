import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.player1 import Player1
from game.casting.player2 import Player2


class HandleCollisionsAction(Action):
    
    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
        if self._is_game_over:
            self._handle_game_over(cast)

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        p1 = cast.get_first_actor("player1")
        p1_head = p1.get_segments()[0]
        p1_segments = p1.get_segments()[1:]

        p2 = cast.get_first_actor("player2")
        p2_head = p2.get_segments()[0]
        p2_segments = p2.get_segments()[1:]
        
        for p2_segment in p2_segments:
            if p1_head.get_position().equals(p2_segment.get_position()):
                self._is_game_over = True
                self._winner = "player2"

        for p1_segment in p1_segments:
            if p2_head.get_position().equals(p1_segment.get_position()):
                self._is_game_over = True
                self._winner = "player1"

        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            p1 = cast.get_first_actor("player1")
            p1_segments = p1.get_segments()

            p2 = cast.get_first_actor("player2")
            p2_segments = p2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()

            if self._winner == "player1":
                message.set_text("Game Over!  Player 1 Wins!")
                
            if self._winner == "player2":
                message.set_text("Game Over!  Player 2 Wins!")
            
            message.set_position(position)
            message.set_color(constants.RED)
            cast.add_actor("messages", message)

            for segment in p1_segments:
                segment.set_color(constants.WHITE)
            for segment in p2_segments:
                segment.set_color(constants.WHITE)
