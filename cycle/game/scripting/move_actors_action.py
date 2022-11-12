from game.scripting.action import Action



class MoveActorsAction(Action):
    def execute(self, cast, script):
        list = cast.get_all_actors()
        for actor in list:
            actor.move_next()
