def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    head=0
    tail=0
    l=len(s)
    t_sp=list(t)
    m=len(s)
    short=s
    flag=False
    def check(a):
        for i in t_sp:
            if i in a:
                a.remove(i)
            else:
                return False
        return True

    if len(t)==1 :
        if t in s:
            return t
        else:
            return ""
    while head<l and tail<l:
        if s[head] not in t_sp:
            head+=1
            continue
        for tail in range(head+1,l):
            if s[tail] not in t_sp:
                continue
            a=list(s[head:tail+1])
            if check(a):
                if len(s[head:tail+1])<m:
                    short=s[head:tail+1]
                    m=len(short)
                flag=True
        head+=1
    if flag==True:
        return short
    return ""


        
        