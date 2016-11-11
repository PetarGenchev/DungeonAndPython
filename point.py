def get_neighbor(x, y, direction):
    neighbors = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
    if direction not in neighbors.keys():
        raise ValueError("Direction must be up, down, left or right.")
    new_x = x + neighbors[direction][0]
    new_y = y + neighbors[direction][1]
    return new_x, new_y


def point_is_passable(matrix, x, y):
    rows = len(matrix)
    cols = len(matrix[0])
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return False
    return matrix[x][y] != '#'
