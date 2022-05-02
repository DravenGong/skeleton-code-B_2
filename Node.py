class Node:

    def __init__(self, location_r, location_q):
        self.node_info = {}
        self.manhattan_distances = 0.0
        self.path_distance = 0.0
        self.general_value = 0.0
        self.location_q = location_q
        self.location_r = location_r
        self.location_s = -(self.location_r) - (self.location_q)
        self.previous_node = None
        self.string_location = '('+str(self.location_r) + ',' + str(self.location_q) + ')'

    def get_location_q(self):
        return self.location_q
    def get_location_r(self):
        return self.location_r
    def get_location_s(self):
        return self.calculate_s()

    #update current node's previous node
    def insert_previous_node(self, previousNode):
        self.previous_node = previousNode



    # get all the possible 6 neighbouring nodes
    def get_neighbouring_node(self):
        neighbour_list = [(self.location_r - 1, self.location_q + 1), (self.location_r, self.location_q - 1),
                          (self.location_r - 1, self.location_q), (self.location_r + 1, self.location_q),
                          (self.location_r, self.location_q + 1), (self.location_r + 1, self.location_q - 1)]
        return neighbour_list

    #Manhattan distances formula
    def get_manhattan_distances(self, goal_s, goal_q, goal_r):
        det_q = abs(goal_q - self.location_q)
        det_s = abs(goal_s - self.location_s)
        det_r = abs(goal_r - self.location_r)
        manhattan_distances = (det_r + det_s + det_q)/2
        return manhattan_distances

    #Storing the node's neighbouring node's  f(N), h(n), g(n)
    def node_info_update(self, goal_s, goal_q, goal_r):

        neighbouring_node = Node.get_neighbouring_node(self)
        self.location_s = self.calculate_s()
        self.manhattan_distances = self.Manhattan_distances(goal_s, goal_q, goal_r)


        #h(n)
        self.node_info.update({"heuristic value": self.manhattan_distances})
        #g(N)
        self.node_info.update({"path distance value": self.path_distance})
        #f(n)
        self.general_value = self.manhattan_distances + self.path_distance
        self.node_info.update({"general value": self.general_value})
