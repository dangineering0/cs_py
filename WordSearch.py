class WordSearch(object):
    def exist(self, board, word):

        #find the letter

        firstChar = word[0]
        for pos, v in enumerate(board):
            for pos2, k in enumerate(v):
                if k == firstChar:
                    self.dfs(Node(pos, pos2), board, word)

    def dfs(self, node, board, word):
        xLim = len(board)
        yLim = len(board[0])
        visited = [[False * len(board[0])] * len(board)]
        stack = []
        stack.append(node)

        while (len(stack) != 0):
            curNode = stack.pop()
            visited[curNode.x][curNode.y] = True

            if (curNode.wordSoFar == word):
                return True

            if (not visited[curNode.x][curNode.y-1] and curNode.x >= 0 and curNode.y-1 >= 0):
                stack.push(Node(curNode.x, curNode.y-1, curNode.wordSoFar+board[curNode.x][curNode.y-1]))

            # do same for all 4

        return False



class Node(object):
    def __init__(self, x, y, wordSoFar):
        self.x = x
        self.y = y
        self.wordSoFar = wordSoFar