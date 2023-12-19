# 1436. Destination City

def destCity(paths):

    hashmap={}

    for path in paths:
        hashmap[path[0]]=path[1]
    for path in paths:
        if path[1] not in hashmap:
            return path[1]
        


def destCity_1(paths):
    start_cities, end_cities = map(set, zip(*paths))
    destination = (end_cities - start_cities).pop()
    
    return destination
