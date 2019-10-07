class Mean:
    @staticmethod
    def sumMean(listValues):
        print('In method sumMean')
        sumMean = 0
        for val in listValues:
            sumMean += val
        print('The sum mean is ', sumMean)
        return sumMean

    def avgMean(self, listValues):
        print('In method avgMean')
        return self.sumMean(listValues) / len(listValues)


print('Number of values you want to calculate mean for :')
numberOfValues = input()
i = 0
x = []
while i < int(numberOfValues):
    print('Enter the value {}', i + 1)
    x.append(int(input()))
    i += 1
else:
    print('Entered all the values')
print('The mean of the values {0} is {1}'.format(x, Mean().avgMean(x)))
