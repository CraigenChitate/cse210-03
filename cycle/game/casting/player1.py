import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Player1(Actor):
   
    def __init__(self, score):
        super().__init__()
        self._segments = []
        self._prepare_body()
        self.player_score = score

    def get_segments(self):
        return self._segments

    def move_next(self):
        
        head = self._segments[0]
        head.move_next()

        position = self._segments[0].get_position()
        velocity = head.get_velocity()

        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text("#")
        segment.set_color(constants.GREEN)
        self._segments.append(segment)

    def turn_head(self, velocity):
        if (str(self._segments[0].get_velocity()) != str(velocity)):
            self.player_score.add_points(1)
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.MAX_X * (3 / 4))
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(0 , 1 * constants.CELL_SIZE)
            text = "8" if i == 0 else "#"
            color = constants.GREEN if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)