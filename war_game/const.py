suits = ['Hearts','Diamonds','Clubs','Spades']
ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
scores = {}
for i in range(2,15):
    scores[ranks[i-2].lower()] = i
war_resolution_count = 3