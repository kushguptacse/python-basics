sample = (1,2,3)
print(sample) # print (1,2,3)
print(sample[0]) # print 1
print(sample[:2]) # print (1,2)
sample = ('a','a','b')
print(len(sample)) # print 3
print(sample.count('a')) # print 2
print(sample.index('a')) # print 0
sample = ('k',[1,2],9.1) # valid, tuple allows dict and all type as value
sample[1][1] = 44
print(sample) # print ('k', [1, 44], 9.1)