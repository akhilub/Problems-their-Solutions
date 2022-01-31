#BACKTRACKING ALGORITHM TO SOLVE N QUEEN PROBLEM

def can_place(cur, x):
    for i, y in enumerate(cur):
        if y == x or len(cur) - i == abs(x - y):
            return False
    return True
 
def dfs(cur, n):
    if len(cur) == n:
        return 1
    ans = 0
    for row in range(n):
        if can_place(cur, row):
            # placing next queen
            ans += dfs(cur + [row], n)
    return ans
 
def queen(n):
    return dfs([], n)
    
# 92 solutions for 8x8 queen problem
print(queen(8))
