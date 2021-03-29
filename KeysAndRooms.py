class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        check_list = [False] * len(rooms)
        key_list = []
        num = 0
        
        key_list.append(0)
         
        while len(key_list)>0 :
            new_list = []
            for x in key_list :
                if not check_list[x]:
                    check_list[x] = True
                    num += 1
                    for e in rooms[x] :
                        if not check_list[e]:
                            new_list.append(e)
            key_list = new_list
        
        return num==len(rooms)
