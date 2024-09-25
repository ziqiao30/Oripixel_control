class Mover:
    def __init__(self, error_zone=0.1):
        self.error_zone = error_zone

    def next_move(self, current_x, current_y, target_x, target_y):
        if abs(current_x - target_x) <= self.error_zone and abs(current_y - target_y) <= self.error_zone:
            return 'Reached Target'
        elif abs(current_x - target_x) > self.error_zone:
            if current_x < target_x:
                return 'Right'
            else:
                return 'Left'
        elif abs(current_y - target_y) > self.error_zone:
            if current_y < target_y:
                return 'Up'
            else:
                return 'Down'

# Example usage:
mover = Mover(error_zone=0.1)
current_x, current_y = 1.0, 1.0
target_x, target_y = 3.0, 4.0

# Simulate movement
while True:
    move = mover.next_move(current_x, current_y, target_x, target_y)
    print(f'Current position: ({current_x}, {current_y}), Next action: {move}')
    if move == 'Reached Target':
        break
    elif move == 'Right':
        current_x += 1.0  # Adjust the step size as needed
    elif move == 'Left':
        current_x -= 1.0
    elif move == 'Up':
        current_y += 1.0
    elif move == 'Down':
        current_y -= 1.0
