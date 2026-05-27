from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            first_email = account[1]
            
            if first_email not in parent:
                parent[first_email] = first_email
            email_to_name[first_email] = name
            
            for i in range(2, len(account)):
                email = account[i]
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)
        
        root_to_emails = defaultdict(list)
        for email in parent.keys():
            root = find(email)
            root_to_emails[root].append(email)
        
        result = []
        for root, emails in root_to_emails.items():
            name = email_to_name[root]
            merged_account = [name] + sorted(emails)
            result.append(merged_account)
        
        return result