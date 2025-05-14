DIRECTIONS = {'RIGHT': 0, 'DOWN': 1, 'LEFT': 2, 'UP': 3}

def get_new_pos(direction, pos_x, pos_y):
    if direction == DIRECTIONS['RIGHT']:
        pos_x += 1
    elif direction == DIRECTIONS['DOWN']:
        pos_y += 1
    elif direction == DIRECTIONS['LEFT']:
        pos_x -= 1
    elif direction == DIRECTIONS['UP']:
        pos_y -= 1
    return pos_x, pos_y

def turn(direction):
    return (direction + 1) % 4

def snail(snail_map):

    if snail_map == [[]]:
        return []

    row_len = len(snail_map)
    total_steps = row_len * row_len

    pos_x, pos_y = 0, 0
    direction = DIRECTIONS['RIGHT']
    steps_after_turn = 0

    return_arr = []

    for i in range(total_steps):
        #Update map
        return_arr.append(snail_map[pos_y][pos_x])
        snail_map[pos_y][pos_x] = 'X'
        #turn
        test_x, test_y = get_new_pos(direction, pos_x, pos_y)
        if steps_after_turn >= row_len - 1 or snail_map[test_y][test_x] == 'X':
            direction = turn(direction)
            steps_after_turn = 0
        #step
        pos_x, pos_y = get_new_pos(direction, pos_x, pos_y)
        steps_after_turn += 1

    return return_arr

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(array)

print(snail(array))