from game.scripting.action import Action


class DrawActorsAction(Action):
    

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor("scores")
        score2 = cast.get_group_actors("scores")
        p1 = cast.get_first_actor("player1")
        p1_segments = p1.get_segments()
        p2 = cast.get_first_actor("player2")
        p2_segments = p2.get_segments()

        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(p1_segments)
        self._video_service.draw_actors(p2_segments)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()