# Fibonnaci Sequence

# Difficulty: Advanced

# NOTE: This is *not* a practical example of how you'll use coding in your day to day, BUT it does appear on a surprising number of in-person coding interviews.  Why employers rely on something so impractical to gauge your coding ability is beyond me.
#       But since they're using it, maybe in this narrow sense it's a practical exercise to know how to do after all.


# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... The next number is found by adding up the two numbers before it.

# Create a program that will generate the first 10 numbers in the Fibonacci Sequence.

# When completed, your program should have the output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# numberList = []
# for number in range(10):
# 	numberList.append(number)
# print("Number List:{0}".format(numberList))

# FibonacciList = numberList
# for index, number in enumerate(FibonacciList):
# 	previousNumber = FibonacciList[index-1]
# 	print("Adding {0}+{1}").format(previousNumber,number)
# 	numberToAdd = previousNumber + number
# 	FibonacciList.append(numberToAdd)
# 	print(FibonacciList)
# 		#FibonacciList.append(previousNumber+numberToAdd)
# #print FibonacciList

# Create list to hold sequence
FibonacciList = [0,1]
for number in range(10):
	# # If FibonacciList has had numbers added to it, we need to get the previous number
	# if (len(FibonacciList) > 0):
	# 	previousNumber = FibonacciList[number-1]
	# else:
	# 	previousNumber = 0
	print("{0}+{1}").format(FibonacciList[-1],FibonacciList[-2])
	FibonacciList.append(FibonacciList[-1]+FibonacciList[-2])
	# currentNumber = FibonacciList[number]
	# print("Adding {0} + {1}".format(previousNumber, currentNumber))
	# summedNumber = previousNumber + currentNumber
	# FibonacciList.append(summedNumber)
print(FibonacciList)
