class Mover:
    def __init__(self, error_zone=0.1):
        self.error_zone = error_zone

    def next_move(self, current_x, current_y, target_x, target_y):
        """
        Determine the next move direction based on current and target positions.

        :param current_x: Current x-coordinate
        :param current_y: Current y-coordinate
        :param target_x: Target x-coordinate
        :param target_y: Target y-coordinate
        :return: Next move direction ('Up', 'Down', 'Left', 'Right', or 'Reached Target')
        """
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
        else:
            return 'Stay'

    def move_along_square(self, current_x, current_y, targets):
        """
        Control the object to move along a square path.

        :param current_x: Current x-coordinate of the object
        :param current_y: Current y-coordinate of the object
        :param targets: List of target positions in the format [(x1, y1), (x2, y2), ...]
        :return: Next move direction and updated target list
        """
        if not targets:
            return 'Finished', targets

        target_x, target_y = targets[0]

        # Check if the current target is reached
        if abs(current_x - target_x) <= self.error_zone and abs(current_y - target_y) <= self.error_zone:
            # Remove the reached target and proceed to the next one
            targets.pop(0)
            if not targets:
                return 'Finished', targets
            target_x, target_y = targets[0]

        # Determine the next move direction
        if abs(current_x - target_x) > self.error_zone:
            if current_x < target_x:
                return 'Right', targets
            else:
                return 'Left', targets
        elif abs(current_y - target_y) > self.error_zone:
            if current_y < target_y:
                return 'Up', targets
            else:
                return 'Down', targets
        else:
            return 'Stay', targets





# Example usage:
# Define the square's four vertices in order
square_targets = [(0, 0), (4, 0), (4, 4), (0, 4)]

# Initialize current position
current_x, current_y = 0.0, 0.0

# Create an instance of the Mover class
mover = Mover(error_zone=0.1)

# Simulate movement
while True:
    direction, square_targets = mover.move_along_square(current_x, current_y, square_targets)
    if direction == 'Finished':
        print('Finished moving along the square!')
        break
    else:
        print(f'Current position: ({current_x}, {current_y}), Move direction: {direction}')
        # Update current position based on the move direction
        if direction == 'Right':
            step = min(1.0, abs(square_targets[0][0] - current_x))
            current_x += step
        elif direction == 'Left':
            step = min(1.0, abs(current_x - square_targets[0][0]))
            current_x -= step
        elif direction == 'Up':
            step = min(1.0, abs(square_targets[0][1] - current_y))
            current_y += step
        elif direction == 'Down':
            step = min(1.0, abs(current_y - square_targets[0][1]))
            current_y -= step
