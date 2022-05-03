from referee import *
from Node import *


def a_star(board, start, goal):
    # Node list for the priority determination in every iteration
    front_list = []

    # A list to store all the visited nodes
    visited = []

    cost_from_root = {}
    path = {}
    is_solution = False
    front_list.append(start)
    path.update({start.string_location: None})
    cost_from_root.update({start.string_location: 0})
    start.general_value = 0
    while front_list:
        # sort the list by f(N)
        front_list.sort(key=lambda Node: Node.general_value)

        # choose the node which has the smallest f(N)
        current_node = front_list[0]
        visited.append(current_node)
        del (front_list[0])

        # Goal has been found
        if current_node.string_location == goal.string_location:
            is_solution = True
            break

        pre_neighbour_list = current_node.get_neighbouring_node()
        # Storing all the reachable and valid neighbouring nodes
        final_neighbour_list = neighbour_in(pre_neighbour_list, board, visited)
        if final_neighbour_list:

            for next_node in final_neighbour_list:
                # iterating g(N)
                next_cost = cost_from_root[current_node.string_location] + 1
                if next_node.string_location not in cost_from_root or next_cost < cost_from_root[
                    next_node.string_location]:
                    cost_from_root.update({next_node.string_location: next_cost})

                    next_node.manhattan_distances = next_node.get_manhattan_distances(goal.location_s, goal.location_q,
                                                                                      goal.location_r)
                    next_node.general_value = next_node.manhattan_distances + next_cost

                    front_list.append(next_node)
                    path.update({next_node.string_location: current_node.string_location})

    if is_solution:
        route_len = len(back_tracking(path, goal))
        return route_len
    else:
        return 0


# Add the valid nodes into the final neighbouring node list
def neighbour_in(neighbour_list, board, visited):
    node_list = []
    for neighbour in neighbour_list:
        if is_neighbour_valid(neighbour, board, visited):
            nei_node = Node(neighbour[0], neighbour[1])
            node_list.append(nei_node)
    return node_list


# Determine if the neighbour node is valid or not
def is_neighbour_valid(neighbour, board, visited):
    if is_available(neighbour, board) and is_new(neighbour, visited):
        return True
    return False


# Determine if the neighbour is a block or beyond the board's size
def is_available(neighbour, board):
    if neighbour[0] >= board.n or neighbour[1] >= board.n:
        return False
    if neighbour[0] < 0 or neighbour[1] < 0:
        return False
    lst = []
    grids = {}

    for i in range(0, board.n):
        for j in range(0, board.n):
            grids[(i,j)] = board.__getitem__((i,j))
    for grid in grids:
        if grids[grid] is not None:
            lst.append(grid)
    for grid in lst:
        if grid[0] == neighbour[0] and neighbour[1] == grid[1]:
            return False
    return True


# Determine if the neighbour node is a new node
def is_new(neighbour, visited):
    for parent in visited:
        if parent.location_r == neighbour[0] and parent.location_q == neighbour[1]:
            return False
    return True


# Backtracking function to return the route towards the goal
def back_tracking(path_dic, goal_state):
    route = []
    i = 0
    z = goal_state.string_location
    for x, y in reversed(path_dic.items()):
        if x == z:
            if y is None:
                i -= 1
                route.insert(i, x)
                break
            i -= 1
            route.insert(i, x)
            z = y
    return route
