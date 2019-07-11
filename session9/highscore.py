score = [45 , 67 , 56 , 78]
print("high score")
m=max(score)
print(m)
max2=score[0]
max3=score[0]
max4=score[0]
for a in range(len(score)):
    if max2 < score[a] < m:
        max2 = score[a]
        print(max2)
        for b in range(len(score)):
            if max3 < score[b] < max2 <m:
                max3 = score[b]
                print(max3)
                for c in range(len(score)):
                    if max4 < score[c]< max3 < max2 < m:
                        max4 = score[c]
                        print(max4)



        

