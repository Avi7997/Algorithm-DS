#Author : Poojan / Avi
def lps(pattern):
    l = [0]
    i = 0
    for j in range(1,len(pattern)):
        if pattern[j]==pattern[i] :
            i+=1
            l.append(i)
        else:
            while i>0 and pattern[j]!=pattern[i] :
                i-=1
            if(i==0):
                l.append(0)
            else:
                i+=1
                l.append(i)
    return l
def kmp(string , pattern):
    s_len = len(string)
    p_len = len(pattern)
    lps_ = lps(pattern)
    j=0
    ans = []
    for i in range(s_len):
        if j==p_len:
            ans.append(i-p_len)
            j=lps_[j-1]
        if string[i] == pattern[j]:
            j+=1
        else:
            while j>0:
                if string[i]==pattern[j]:
                    j+=1
                    break
                else:
                    j=lps_[j-1]
    if j==p_len:
        print(j)
        ans.append(s_len-p_len)              
    return ans

string = input()
pat = input()
print(kmp(string,pat)) 