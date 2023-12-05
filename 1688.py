# 1688. Count of Matches in Tournament
def matchesplayed(n):
    if n%2==0:
        matches=n//2
        return matches + matchesplayed(matches)
    if n%2!=0:
        if n==1:
            return 0
        matches=(n-1)//2
        return matches + 1 + matchesplayed(matches)
    
