def mutualFriends(userA_friends, userB_friends):
    # Returns elements (people) both users know
    return userA_friends.intersection(userB_friends)

def differentFriends(userA_friends, userB_friends):
    # Returns elements in User A that are not in User B
    return userA_friends.difference(userB_friends)

def unionFriends(userA_friends, userB_friends):
    # Returns every person from both lists, with no duplicates
    return userA_friends.union(userB_friends)

def calculateSimilarity(userA_friends, userB_friends):
    # This part will tell us how similar two people are
    mutual = mutualFriends(userA_friends, userB_friends)
    all_friends = unionFriends(userA_friends, userB_friends)
    
    # Control to prevent error
    if len(all_friends) == 0:
        return 0.0
        
    result = len(mutual) / len(all_friends)
    return result

def friendSuggest(target_user, social_network):
    suggestions = set()  
    my_friends = social_network[target_user]

    for friend in my_friends:
        friends_of_friend = social_network[friend]

        for person in friends_of_friend:
            # Only suggest if they aren't me and aren't already my friend
            if person != target_user and person not in my_friends:
                suggestions.add(person)

    return suggestions

# --- Example ---
network = {
    "Elenie": {"Eylül", "Yeongjun", "Ali"},
    "Eylül": {"Elenie", "Yeongjun", "Ayşe"},
    "Yeongjun": {"Elenie", "Eylül", "Can"},
    "Ali": {"Elenie", "Can"},
    "Ayşe": {"Eylül"},
    "Can": {"Ali", "Yeongjun"}
}

# suggestions test
suggest = friendSuggest("Eylül", network)
print(f"Friend suggestions for Eylül: {suggest}")

