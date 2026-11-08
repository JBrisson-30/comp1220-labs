class LaserClass:

    
    def __init__(self, initial_power=100):
        self.remaining_power = initial_power
        self.direction = 0
        pass

    def turn_right(self):
        self.direction += 15
        pass

    def turn_left(self):
        self.direction -= 15
        pass

    def fire(self):
        if self.remaining_power >= 10:
            self.remaining_power = self.remaining_power - 10
            return True
        return False


class RechargeableLaser(LaserClass):
    
    def __init__(self, initial_power=100):
        super().__init__(initial_power)
        self.max_power = initial_power
        pass

    def recharge(self):
        self.remaining_power = self.max_power
        pass
