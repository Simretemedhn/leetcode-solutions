class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        collec = []
        for p in paths:
            if p == "." or p == "":
                continue 
            elif p == "..":
                if collec:
                    collec.pop()
            else:
                collec.append(p)
        return "/" + "/".join(collec)