class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parents = [i for i in range(n)]
        ranks = [1] * n

        # find parent and compress
        def find(i):
            if parents[i] == i:
                return i
            parents[i] = find(parents[i])
            return parents[i]
        
        def union(i, j):
            r1, r2 = find(i), find(j)
            if r1 == r2:
                return False
            if ranks[r1] > ranks[r2]:
                parents[r2] = r1 
            if ranks[r1] < ranks[r2]:
                parents[r1] = r2
            else:
                parents[r2] = r1
                ranks[r1] += 1
            return True

        emailToAccountIdx = {} # email -> index of account
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccountIdx:
                    union(i, emailToAccountIdx[email])
                else:
                    emailToAccountIdx[email] = i
#         {
#   "a@m.com": 0,
#   "b@m.com": 0
# }
        
        emailGroup = defaultdict(list)  # index of account -> list of emails
        for email, accountIndex in emailToAccountIdx.items():
            leaderIdx = find(accountIndex)
            emailGroup[leaderIdx].append(email)

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + emailGroup[i])

        return res
                

