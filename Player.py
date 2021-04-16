# Player

class Player:
    def __init__(self, gesture):
        self.gesture = gesture
        self.score = 0

        gesture.add("rock")
        gesture.add("paper")
        gesture.add("scissors")
        gesture.add("lizard")
        gesture.add("spock")




