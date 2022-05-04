from Minimax import *
from referee.board import Board

class Player:
    colour = ""
    n = int()

    def __init__(self, player, n):
        """
        Called once at the beginning of a game to initialise this player.
        Set up an internal representation of the game state.

        The parameter player is the string "red" if your player will
        play as Red, or the string "blue" if your player will play
        as Blue.
        """
        # put your code here
        self.colour = player
        self.n = n
        self.board = None

        # eason add1
        self.board_dic = {}

        print(self.colour)
        print(self.n)


    def action(self):
        """
        Called at the beginning of your turn. Based on the current state
        of the game, select an action to play.
        """
        # put your code here

        action = ("PLACE", 1, 1)
        return action

    def print_board_dic(self):
        print("\n")
        print("\n")
        for r in range(self.n):
            for q in range(self.n):
                # print((r, q) + ':' + self.board_dic[(r, q)])
                print("location:{} status: {}".format((r,q),self.board_dic[(r, q)]))

    def turn(self, player, action, board):
        """
        Called at the end of each player's turn to inform this player of 
        their chosen action. Update your internal representation of the 
        game state based on this. The parameter action is the chosen 
        action itself. 
        
        Note: At the end of your player's turn, the action parameter is
        the same as what your player returned from the action method
        above. However, the referee has validated it at this point.
        """
        # put your code here
        # EASON ADD
        self.board = board

        print("for red")
        print(player)
        print(action)
        self.board_dic = self.board.store_board_as_dic(self.n)
        self.print_board_dic()
        # print(self.board.total_is_occupied(6))
