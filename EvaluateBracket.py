class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        key = ""
        iskey = False
        news = ""
        ThisDic = {}
        for l in knowledge:
            ThisDic[l[0]]=l[1]
        # print(ThisDic)
        # print(ThisDic.get(knowledge[0][0]))
        for k in s:
            if k == ')' :
                iskey = False
                value = "?"
                if ThisDic.get(key) != None :
                    value = ThisDic[key]
                news+=value
                key=""
            if iskey :
                key+=k 
            if k == '(' :
                iskey = True
            if iskey==False and k != '(' and k!=')':
                news += k
                
        return news
                
