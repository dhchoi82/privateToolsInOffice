data = read.csv('inputList.csv')
summary(data)
attach(data)
data.table = table(factorA,factorB)
data.table
chisq.test(data.table)
detach(data)
