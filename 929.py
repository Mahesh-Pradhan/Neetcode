# 929. Unique Email Addresses

def numUniquemail(emails):
    found=set()

    for e in emails:
        email=""
        local,domain=e.split('@')
        for c in local:
            if c=="+":
                break
            if c==".":
                continue
            email+=c
        found.add((email,domain))
    return len(found)