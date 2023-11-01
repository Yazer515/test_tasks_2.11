from sys import argv

script, elements_file = argv

nums = []

with open(elements_file, "r") as elements_f:
	for line in elements_f:
		element = line.strip()
		nums.append(int(element))

average = round(sum(nums) / len(nums))

steps = 0

for num in nums:
	steps += abs(num - average)
	
print(steps)	