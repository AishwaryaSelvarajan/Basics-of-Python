'''Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.'''

million_number = [number for number in range(1,1000001)]
print (million_number)
minimum_number = min(million_number)
print ("Minimum Number is "+ str(minimum_number))
maximum_number = max(million_number)
print ("Maximum Number is "+ str(maximum_number))
sum_number = sum(million_number)
print ("The sum of million numbers are " + str(sum_number))