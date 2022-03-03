'''
Input: names = ["pes","fifa","gta","pes(2019)"]
Output: ["pes","fifa","gta","pes(2019)"]

Input: names = ["gta","gta(1)","gta","avalon"]
Output: ["gta","gta(1)","gta(2)","avalon"]
'''
class Solution:
    def getFolderNames(self, names):
        res = []
        dic = {}

        for name in names:
            if name not in dic:
                dic[name] = 1
                res.append(name)
            else:
                count = dic[name]
                tmp = name + "(" + str(count) + ")"
                while tmp in dic:
                    count += 1
                    tmp = tmp = name + "(" + str(count) + ")"

                res.append(tmp)
                dic[tmp] = 1
                dic[name] = count

        return res
