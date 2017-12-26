"""
    Information:
    * Date: 2017-12-25
    * Brief: making tests for programming collective intelligence chapter 2
             making recommendations
    * Author: haskellcg

    Platform:
    * Windows7_X64
    * Python3.6_X64

    Libs:

    Problems:

"""

critics={
        "Lisa Rose": {
            "Lady in the Water": 2.5,
            "Snakes on a Plane": 3.5,
            "Just My Luck": 3.0, 
            "Superman Returns": 3.5,
            "You, Me and Dupree": 2.5,
            "The Night Listener": 3.0
        },

        "Gene Seymour": {
            "Lady in the Water": 3.0,
            "Snakes on a Plane": 3.5,
            "Just My Luck": 1.5, 
            "Superman Returns": 5.0,
            "The Night Listener": 3.0,
            "You, Me and Dupree": 3.5
        },

        "Michael Phillips": {
            "Lady in the Water": 2.5,
            "Snakes on a Plane": 3.0,
            "Superman Returns": 3.5,
            "The Night Listener": 4.0
        },

        "Claudia Puig": {
            "Snakes on a Plane": 3.5,
            "Just My Luck": 3.0,
            "The Night Listener": 4.5,
            "Superman Returns": 4.0,
            "You, Me and Dupree": 2.5
        },

        "Mick LaSalle": {
            "Lady in the Water": 3.0,
            "Snakes on a Plane": 4.0,
            "Just My Luck": 2.0,
            "Superman Returns": 3.0,
            "The Night Listener": 3.0,
            "You, Me and Dupree": 2.0
        },

        "Jack Matthews": {
            "Lady in the Water": 3.0,
            "Snakes on a Plane": 4.0,
            "The Night Listener": 3.0,
            "Superman Returns": 5.0,
            "You, Me and Dupree": 3.5
        },

        "Toby": {
            "Snakes on a Plane":4.5,
            "You, Me and Dupree":1.0,
            "Superman Returns":4.0
        }
}


"""
    Euclidean Distance Score
"""

from math import sqrt

# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs, person1, person2):
    # Get the list of shared_items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
            
    # if they have no ratings in common, return 0
    if len(si) == 0:
        return 0

    # Add up the squares of all the differences
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] 
                          if item in prefs[person2]])

    return 1 / (1 + sum_of_squares)

# Test sim_distance function
print(sim_distance(critics, "Lisa Rose", "Gene Seymour"))


"""
    Pearson Correlation Score
"""

# Returns the Pearson correlation coefficient for person1 and person2
def sim_pearson(prefs, person1, person2):
    # Get the list of mutually rated items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # Find the number of elements
    n = len(si)

    # if they are no rating in common, return 0
    if n == 0:
        return 0

    # Add up all the preferences
    sum1 = sum([prefs[person1][it] for it in si])
    sum2 = sum([prefs[person2][it] for it in si])

    # Sum up the squares
    sum1Sq = sum([pow(prefs[person1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[person2][it], 2) for it in si])

    # Sum up the products
    pSum = sum([prefs[person1][it] * prefs[person2][it] for it in si])
    
    # Calculate Pearson score
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * 
               (sum2Sq - pow(sum2, 2) / n))

    if den == 0:
        return 0

    r = num / den

    return r

# Test sim_pearson function
print(sim_pearson(critics, "Lisa Rose", "Gene Seymour"))

# Returns the best matches for person from the prefs dictionary
# Number of results and similarity function are optional params
def top_matches(prefs, person, n = 5, similarity = sim_pearson):
    scores = [(similarity(prefs, person, other), other) 
              for other in prefs if other != person]

    # Sort the list so the highest scores appear at the top
    scores.sort()
    scores.reverse()

    return scores[0:n]


# Test top_matches function
print(top_matches(critics, "Toby", n = 3))

# Issue: Reveiwers who haven't reveiwed some of the movies that I might like
# Issue: Reveiwer who strangely liked a movie that got bad reviews 
#        from all the other critics returned by top_matches
# 使用权重的方法，而不是把最相似的人的电影全部推送
# 并且两人中有任何一人没看过的，不作为计算

# Gets recommendations for a person by using a weight average
# of every other user's rankings
def get_recommendations(prefs, person, similarity = sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        # don't compare me to myself
        if other == person:
            continue

        sim = similarity(prefs, person, other)

        # ignore scores of zero or lower
        if sim <= 0:
            continue

        for item in prefs[other]:
            # only score movies that I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # Create the normalized list
    rankings = [(total / simSums[item], item)
                for item, total in totals.items()]

    # Return the sorted list
    rankings.sort(reverse = True)
    return rankings

# Test get_recommendations function
print(get_recommendations(critics, "Toby"))
print(get_recommendations(critics, "Toby", similarity = sim_distance))

def transform_prefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            # Flip item and person
            result[item][person] = prefs[person][item]

    return result

# Test transform_prefs function
# Notice that in this example there are actually some negative correlation 
#   scores, which indicate that those who like Superman Returns tend to
#   dislike Just My Luck
movies = transform_prefs(critics)
print(top_matches(movies, "Superman Returns"))
print(get_recommendations(movies, "Just My Luck"))
