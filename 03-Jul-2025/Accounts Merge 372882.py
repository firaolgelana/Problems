# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class DSU:
    def __init__(self):
        self.parent = {}
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        rootU, rootV = self.find(u), self.find(v)
        if rootU != rootV:
            self.parent[rootU] = rootV


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        dsu = DSU()
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in dsu.parent:
                    dsu.parent[email] = email
                dsu.union(account[1], email)
                email_to_name[email] = name
        emails = defaultdict(list)
        for email in dsu.parent:
            root = dsu.find(email)
            emails[root].append(email)

        result = []
        for email, values in emails.items():
            name = email_to_name[email]
            result.append([name] + sorted(values))

        return result

