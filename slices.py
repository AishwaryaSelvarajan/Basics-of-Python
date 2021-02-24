'''Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.
• Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.'''

slice_list = ['Limerick','Cork', 'Galway','Dublin','Wexford', 'Kerry']
print ("The first three items in the list are: ")
print (slice_list[:3])

print ("Three items from the middle of the list are : ")
print (slice_list[2:5])

print("The last three itemsin the list are: ")
print(slice_list[3:])