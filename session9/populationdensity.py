distric =["ST", "BĐ", "BTL", "CG","ĐĐ", "HBT"]
print(*distric, sep=", ")
population = [150300 , 247100 , 333300 , 266800 , 420900 , 318000 ]
print(*population, sep=" ; ")
area = [117.43,9.224,43.35,12.04,9.96,10.09]
print(*area, sep=" ; ")
for i in range(len(area)):
    populationdensity=population[i]//area[i]
    print(populationdensity)
m=(1279+26788+7688+22159+42259+31516)/6
print(m)