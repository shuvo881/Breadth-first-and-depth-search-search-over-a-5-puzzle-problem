from collections import deque # required for Queue
class Pazzel:
    def __int__(self):  # constructor
        # required private variables
        self.parent = None  # stores the parent puzzle object
        self.action = ""  # stores the action taken to reach this puzzle configuration from its parent
        self.pathCost = 0  # stores the cost of the path from the initial state to this puzzle configuration
        self.arr = list()  # stores the puzzle configuration as a list of lists

    def initialState(self):
        # prompt user to input number of rows and columns in puzzle
        print("Enter total row and column number")
        r, c = map(int, input().split())

        # initialize empty list for puzzle configuration
        arr = []

        # prompt user to input values for each element in the puzzle
        print("Enter Value of line by line")
        for i in range(r):
            a = []
            for j in range(c):
                a.append(int(input()))
            arr.append(a)

        # set instance variables for initial puzzle configuration
        self.action = "int" # initial code sate define
        self.pathCost = 0 # initial Path cost is 0
        self.arr = arr
        self.parent = None # initial time no parent for this node

        # return initial puzzle configuration
        return self.arr

    def goal(self):
        # define goal puzzle configuration
        ans = [[1, 2, 3], [4, 5, 0]]

        # check if puzzle configuration of state parameter matches goal configuration
        if self.arr == ans:
            return True
        return False

    def childSate(self, action):
        # find position of blank space in puzzle
        ii = 0
        ckr = False
        while ii < len(self.arr):
            jj = 0
            while jj < len(self.arr[0]):
                if self.arr[ii][jj] == 0:
                    ckr = True
                    break
                jj += 1
            if ckr:
                break
            ii += 1

        # copy puzzle configuration
        arr = []
        for x in self.arr:
            a = []
            for itm in x:
                a.append(itm)
            arr.append(a)

        # modify puzzle configuration based on action parameter
        if action == "down":
            try:
                # swap blank space with element below it
                arr[ii][jj] = arr[ii + 1][jj]
                arr[ii + 1][jj] = 0
                # self.action = "up"
                # self.pathCost += 1
                return arr
            except:
                # index out of range error if move is not possible
                # print("Index Overflow")
                return []
        if action == "up":
            if ii - 1 < 0:
                # move is not possible if blank space is in top row
                return []
            try:
                # swap blank space with element above it
                arr[ii][jj] = arr[ii - 1][jj]
                arr[ii - 1][jj] = 0
                # action = "down"
                # self.pathCost += 1
                return arr
            except:
                # index out of range
                # action not possible
                return []
        if action == "left":
            if jj - 1 < 0:
                # action not possible
                return []
            try:
                # swap blank space with element to left of it
                arr[ii][jj] = arr[ii][jj - 1]
                arr[ii][jj - 1] = 0
                return arr
            except:
                # action not possible
                return []
        if action == "right":
            try:
                # swap blank space with element to right of it
                arr[ii][jj] = arr[ii][jj + 1]
                arr[ii][jj + 1] = 0
                return arr
            except:
                # action not possible
                return []
            # invalid action
        print("action case problem")
        return []

    def actionFun(self, ar):
        # check if puzzle configuration is same as parent's
        try:
            if ar == self.parent.arr:
                # return None if it is
                return None
        except:
            # create new Pazzel object with given puzzle configuration and current object as parent
            obj = Pazzel()
            obj.arr = ar
            obj.parent = self
            return obj

        # create new Pazzel object with given puzzle configuration and current object as parent
        obj = Pazzel()
        obj.arr = ar
        obj.parent = self
        return obj
# DFS aperoch
def dfs(root):
    # queue for storing nodes waiting to be processed
    que = deque([root])

    # continue as long as there are nodes in the queue
    while que:
        # process each node in the queue

        for i in range(len(que)):
            # remove node from front of queue
            node = que.popleft()
            if node.goal():
                return node
            # generate child nodes for possible moves from current puzzle configuration
            arrUp = node.childSate("up")
            arrDown = node.childSate("down")
            arrRight = node.childSate("right")
            arrLeft = node.childSate("left")

            # check if any child node represents the goal state
            if len(arrUp):
                newState = node.actionFun(arrUp)
                if newState:
                    newState.action = 'up'
                    newState.pathCost = node.pathCost+1
                    que.append(newState)

            if len(arrDown):
                newState = node.actionFun(arrDown)
                if newState:
                    newState.action = 'down'
                    newState.pathCost = node.pathCost + 1
                    que.append(newState)

            if len(arrRight):
                newState = node.actionFun(arrRight)

                if newState:
                    newState.action = 'right'
                    newState.pathCost = node.pathCost + 1
                    que.append(newState)

            if len(arrLeft):
                newState = node.actionFun(arrLeft)

                if newState:
                    newState.action = 'left'
                    newState.pathCost = node.pathCost + 1
                    que.append(newState)


#BFS approche

def bfs(root):
    # Stak for storing nodes waiting to be processed
    stk = [root]

    # continue as long as there are nodes in the stack
    while stk:
        # process each node in the stk
            # remove node from front of stk
        node = stk.pop()
        if node.goal():
            return node
        # generate child nodes for possible moves from current puzzle configuration
        arrUp = node.childSate("up")
        arrDown = node.childSate("down")
        arrRight = node.childSate("right")
        arrLeft = node.childSate("left")

        # check if any child node represents the goal state
        if len(arrUp):
            newState = node.actionFun(arrUp)
            if newState:
                newState.action = 'up'
                newState.pathCost = node.pathCost + 1
                stk.append(newState)

        if len(arrDown):
            newState = node.actionFun(arrDown)
            if newState:
                newState.action = 'down'
                newState.pathCost = node.pathCost + 1
                stk.append(newState)

        if len(arrRight):
            newState = node.actionFun(arrRight)

            if newState:
                newState.action = 'right'
                newState.pathCost = node.pathCost + 1
                stk.append(newState)

        if len(arrLeft):
            newState = node.actionFun(arrLeft)

            if newState:
                newState.action = 'left'
                newState.pathCost = node.pathCost + 1
                stk.append(newState)


# Perform a breadth-first search (BFS) on a puzzle object
root = Pazzel() # create a new puzzle object
root.initialState() # initialize the puzzle to its starting state
print("Type 1 for BFS or Type 2 for DFS")
if input() == "1":
    path = bfs(root) # perform the BFS search and return the path from the initial state to the goal state
else:
    path = dfs(root)  # perform the BFS search and return the path from the initial state to the goal state
print("Total Cost: ", path.pathCost) # print the path cost (i.e., the number of steps to reach the goal state)

# Iterate through the path and print the details of each state
while path:
    print(path.arr[0]) # print the first element of the state tuple
    print(path.arr[1]) # print the second element of the state tuple
    print(path.action) # print the action taken to transition to this state
    print() # print an empty line
    path = path.parent # move to the next node in the list (i.e., the parent node of the current node)


""" ---------------- Complete Right Code ------"""


