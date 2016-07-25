class Solution(object):
    def alienOrder(self, words):
        # 1. construct graph
        # topsort

        wmap = {}

        for pos, word in enumerate(words):
            for c in list(word):
                if (c not in wmap):
                    wmap[c] = []

            if pos > 0:
                self.order(wmap, words[pos-1], word)

        return self.topSort(wmap)


    # since wordA > wordB
    # sort based on min length and put char at i to point to the char at b's i
    def order(self, wmap, wordA, wordB):
        minLen = min(len(wordA), len(wordB))

        for x in range(minLen):
            aChar = wordA[x]
            bChar = wordB[x]

            if (aChar != bChar):
                wmap[aChar].append(bChar)
                break


    def topSort(self, wmap):
        # build indegree
        indegree = {}
        answer = ""

        for k,v in wmap.items():
            for c in v:
                if c not in indegree:
                    indegree[c] = 1
                else:
                    indegree[c] += 1

        queue = []
        for k,v in wmap.items():
            if k not in indegree:
                queue.append(k)


        # while queue is not empty:
        # poll and decrement all its children by 1 indegree . if any of them became 0 add them to queue
        # add current one to solution set

        while queue:
            curC = queue.pop(0)
            for c in wmap[curC]:
                indegree[c]-=1
                if (indegree[c]==0):
                    queue.append(c)

            answer += curC

        for k,v in indegree.items():
            if v > 0:
                answer = ""

        return answer

print(Solution().alienOrder(["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"]))