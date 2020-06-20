numberOfSlots = 7

class C4Node:
    """A C4Node is a node in the tree of all possible game states.  It keeps track of the state (one of the player has won, or no one has won yet), and which player's turn yielded that node.  It also keeps track of all the nodes below it.
    """

    def __init__(self, player: str, n = numberOfSlots, state="", nodeArray = []):
        self.player = player
        self.state = state
        self.nodeArray = nodeArray
        if self.nodeArray == []:
            self.nodeArray = [None for i in range(n)]

    def __repr__(self):
        return f"C4Node({self.player}, {self.state}, {repr(nodeArray)})"

    def __str__(self):
        return f"Player: {self.player}, State: {self.state}"




if __name__ == '__main__':
    print('test')
    root = C4Node('red')
    root.state = 'red wins'
    root.nodeArray[2] = C4Node('black')

    print(root.nodeArray[2])




