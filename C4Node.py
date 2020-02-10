numberofslots = 7

class C4Node:

    def __init__(self, player: str, n = numberofslots, state="", nodearray = []):
        self.player = player
        self.state = state
        self.nodearray = nodearray
        if self.nodearray == []:
            self.nodearray = [None for i in range(n)]

    def __repr__(self):
        return f"C4Node({self.player}, {self.state}, {repr(nodearray)})"

    def __str__(self):
        return f"Player: {self.player}, State: {self.state}"




if __name__ == '__main__':
    print('test')
    root = C4Node('red')
    root.state = 'red wins'
    root.nodearray[2] = C4Node('black')

    print(root.nodearray[2])




