import math
class MiniMax:

    def __init__(self, max_depth, tree):
        self.current_state = None
        self.max_depth = max_depth
        self.action_list = []
        self.game_tree = tree


    def minimax(self, state):
        # first, find the max value
        depth = 0
        best_val = self.max_value(state, depth)
        best_move = None
        for elem in self.action_list:
            if elem.value == best_val:
                best_move = elem
                break

        # return the best move correspond to best value that we've found
        return best_move


    def max_value(self, state, depth):
        if self.isTerminal(state) or self.max_depth == depth:
            return self.getUtility(state)
        infinity = float('inf')
        max_value = -infinity
        successors_states = self.getSuccessors(state)
        for state in successors_states:
            max_value = max(max_value, self.min_value(state))
        return max_value

    def min_value(self, state):
        if self.isTerminal(state):
            return self.getUtility(state)
        infinity = float('inf')
        min_value = infinity
        successor_states = self.getSuccessors(state)
        for state in successor_states:
            min_value = min(min_value, self.max_value(state))
        return min_value

    # successor states in a game tree are the child nodes…
    def getSuccessors(self, state):
        assert state is not None
        return state.children

    # return true if the node has NO children (successor states)
    def isTerminal(self, node):
        assert node is not None
        return len(node.children) == 0

    def getUtility(self, node):
        assert node is not None
        return node.value