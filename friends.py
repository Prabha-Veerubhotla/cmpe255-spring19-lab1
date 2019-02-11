users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    print("Finding number of friends for user {}".format(user))
    friendshipdict =  {}
    for friend in friendship:
        if friend[0] in friendshipdict.keys():
            friendshipdict[friend[0]] = friendshipdict.get(friend[0]) + 1
        else:
            friendshipdict[friend[0]] = 1
        if friend[1] in friendshipdict.keys():
            friendshipdict[friend[1]] = friendshipdict.get(friend[1]) + 1
        else:
             friendshipdict[friend[1]] = 1

    for u in users:      
        if u["id"] == user["id"]:
            count = friendshipdict.get(user["id"])
            print("{}:{} has {} friends".format(u["id"], u["name"], count))
            print(" ")
            break
    return count
    # TODO
    pass

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    sortdict = {}

    for user in users:
        sortdict[user["name"]] = num_friends(user)

    sortedtuple = sorted(sortdict.items() ,reverse=True, key=lambda userdetails: userdetails[1])

    print("Sorting by number of friends: most friends to least friends")
    print(" ")
    for item in sortedtuple:
         print("{} has {} friends".format(item[0], item[1]))
         print(" ")

    # TOODO
    pass


sort_by_num_friends()