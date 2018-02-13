data = read.csv('inputList.csv')
summary(data)
oneway.test(value ~ factor, data=data)
TukeyHSD(aov(value ~ factor, data=data))
