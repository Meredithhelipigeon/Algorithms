class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        self.pos=[0,0]
        # 'N','E','S','W'        
        self.directions = [[0,1],[1,0],[0,-1],[-1,0]]
        self.cur=0
        def helper_step(self):
            for i in instructions:
                if i=='G':
                    step=self.directions[self.cur]
                    self.pos[0]+=step[0]
                    self.pos[1]+=step[1]
                elif i=='L':
                    self.cur=(self.cur-1)%4
                else:
                    self.cur=(self.cur+1)%4
        for i in range(4):
            helper_step(self)
        
        if self.pos==[0,0]:
            return True
        else:
            return False
    
    # Actually, we don't have to run 4 times. If the current direction is changed, then
    # after changing 180 degrees, it will reverse back.
    def isRobotBounded2(self, instructions: str) -> bool:
        pos=[0,0]
        # 'N','E','S','W'        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        cur=0
        for i in instructions:
            if i=='G':
                step=directions[cur]
                pos[0]+=step[0]
                pos[1]+=step[1]
            elif i=='L':
                cur=(cur-1)%4
            else:
                cur=(cur+1)%4
        
        if pos==[0,0] or cur!=0:
            return True
        else:
            return False
