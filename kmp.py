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

p = "AABAACAABAA"
l = lps(p)
print(l)    