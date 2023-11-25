# 205. Isomorphic Strings

def isIsomorphic(s,t):
    st,ts={},{} # two dictionary

    for i in range(len(s)):
        c1,c2=s[i],t[i] 

        if ((c1 in st and st[c1]!=c2) or ( c2 in ts and ts[c2]!=c1)): # c1 is present in st nad  c1 has diff
                                                                    # mapping already present  or vice versa 
            return False

        st[c1]=c2       #if mapping not present then add
        ts[c2]=c1
    return True