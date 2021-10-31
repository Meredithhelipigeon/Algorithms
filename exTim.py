class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        #  Step 1. stack, times[]       
        stack = []
        times = [0]*n
        
        # Step 2. iterate logs
        for l in logs:
            id_name, command, time = l.split(":")
            id_name=int(id_name)
            time=int(time)
            if command=="start":
                stack.append([id_name,time])
            else:
                start = stack.pop()[1]
                time_change=time-start+1
                times[id_name]+=time_change
                for i in range(len(stack)):
                    stack[i][1]+=time_change

        return times
