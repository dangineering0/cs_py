# @return list of words in the dict:
def exist(board, words):
    res = []


    for word in words:
        visited = [[False] * len(board[0]) for x in range(len(board))]
        if dfs(word, "", 0, 0, visited, board, 0):
            res.append(word)

    return res


def dfs(word, sSoFar, i, j, visited, board, index):


    if word == sSoFar:
        return True

    if len(sSoFar) >= len(word):
        return False

    if i < 0 or i >= len(board):
        return False

    if j < 0 or j >= len(board[0]):
        return False

    if visited[i][j]:
        return False

    curChar = board[i][j]
    visited[i][j] = True

    if curChar == word[index]:
        sSoFar += curChar
        index += 1

    if dfs(word, sSoFar, i+1, j, visited, board, index):
        return True

    elif dfs(word, sSoFar, i, j+1, visited, board, index):
        return True

    elif dfs(word, sSoFar, i-1, j, visited, board, index):
        return True
    elif dfs(word, sSoFar, i, j-1, visited, board, index):
        return True
    else:
        visited[i][j] = False
        return False


b = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
ws = ["oath","pea","eat","rain"]
print(exist(b, ws))


