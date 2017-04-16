from itertools import permutations, combinations

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hours = range(1, 5)
        minutes = range(1, 7)

        result = []
        for i in range(5):
            if num - i < 7 and 0 <= num - i:
                h = ["0"]*(4-i) + ["1"]*i
                m = ["0"]*(6 - (num - i)) + ["1"]*(num - i)
                perH = set(permutations(h))
                perM = set(permutations(m))
                for itemh in perH:
                    ho = "".join(itemh)
                    for itemm in perM:
                        mi = "".join(itemm)
                        hh = int(ho, 2)
                        mm = int(mi, 2)
                        if hh < 12 and mm < 60:
                            clock = "{}".format(hh) + ":" + "{:02}".format(mm)
                            result.append(clock)
        return result



print(len(Solution().readBinaryWatch(2)))
