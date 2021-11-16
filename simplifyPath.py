class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens=path.split("/")
        
        stack=[]
        for t in tokens:
            if t=="..":
                if stack:
                    stack.pop()
            elif t!="." and t!="":
                stack.append(t)
        
        return "/"+"/".join(stack)
