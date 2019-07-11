score = [45 , 67 , 56 , 78]
print("high score")
for i in range(4):
    print(score[i])
newscore=int(input("enter your new score:"))
score.append(newscore)
print("high score")
for m in range(len(score)):
    print(score[m])