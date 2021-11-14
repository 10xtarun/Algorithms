# https://www.geeksforgeeks.org/check-string-substring-another/
# https://www.hackerrank.com/challenges/find-a-string/problem

s1 = "the index of the first occurrence"
s2 = "first"

# algo 1
# TC: O(m*n)
# SC: O(1)
for x in range(0, len(s1)-len(s2)):
    for y in range(0, len(s2)): 
        if(s1[x+y] != s2[y]):
           break
        
    if(y+1 == len(s2)):
            print(x)



# Algo2
# TC: O(m*n) : Worst Case
# SC: O(1)
def algo2(s1, s2):
    ptr=0
    for x in range(0, len(s1)):
        if(s1[x] == s2[ptr]):
            ptr+=1
        else :
            ptr=0
        if(ptr==len(s2)):
            return x - ptr
    return -1

print(algo2(s1, s2))