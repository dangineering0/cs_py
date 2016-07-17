class AllCombinations(object):

    def comb(self, s):
        res = []
        self.helper(s, "", 0, res)

        return res


    def helper(self, s, sSoFar, index, res):

        if (len(s) == index):
            res.append(sSoFar)
            return

        #not include
        self.helper(s, sSoFar, index+1, res)

        #not include
        self.helper(s, sSoFar+s[index], index+1, res)




print(AllCombinations().comb("abc"))