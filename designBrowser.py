class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.curIndex=0
        

    def visit(self, url: str) -> None:
        self.history=self.history[:self.curIndex+1]
        self.history.append(url)
        self.curIndex=len(self.history)-1

    def back(self, steps: int) -> str:
        self.curIndex=max(0,self.curIndex-steps)
        return self.history[self.curIndex]

    def forward(self, steps: int) -> str:
        self.curIndex=min(len(self.history)-1,self.curIndex+steps)
        return self.history[self.curIndex]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

class BrowserHistory2:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.forwardL=[]
        

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.forwardL=[]

    def back(self, steps: int) -> str:
        for s in range(min(steps,len(self.history)-1)):
            self.forwardL.append(self.history.pop())
        return self.history[-1]

    def forward(self, steps: int) -> str:
        for s in range(min(steps,len(self.forwardL))):
            self.history.append(self.forwardL.pop())
        return self.history[-1]

class BrowserHistory3:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.curIndex=0
        

    def visit(self, url: str) -> None:
        for i in range(len(self.history)-1-self.curIndex):
            self.history.pop()
        self.history.append(url)
        self.curIndex=len(self.history)-1

    def back(self, steps: int) -> str:
        self.curIndex=max(0,self.curIndex-steps)
        return self.history[self.curIndex]

    def forward(self, steps: int) -> str:
        self.curIndex=min(len(self.history)-1,self.curIndex+steps)
        return self.history[self.curIndex]
