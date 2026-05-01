players={}
for i in range(10):
    username,rating=input().split()
    players[username]=rating
print(players)