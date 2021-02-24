''' Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.'''

invite_people = []
invite_people.append('Aadhirayan')
invite_people.append('Tiny')
invite_people.append('Mollie')
print ("Hi "+ invite_people[0] + ", You are invited for adinner on Sunday evening")
print ("Hi "+ invite_people[1] + ", You are invited for adinner on Sunday evening")
print ("Hi "+ invite_people[2] + ", You are invited for adinner on Sunday evening")

absent = invite_people.pop()

print (absent + " could not make for dinner")

invite_people.append("Jack")

print ("Hi "+ invite_people[0] + ", You are invited for adinner on Sunday evening")
print ("Hi "+ invite_people[1] + ", You are invited for adinner on Sunday evening")
print ("Hi "+ invite_people[2] + ", You are invited for adinner on Sunday evening")

print ("I have founda bigger dining table, thereby inviting few more people")

invite_people.insert(0, 'Jason')
invite_people.insert(2, 'Lara')
invite_people.append('Clark')

print ("Hi "+ invite_people[0] + ", You are invited for adinner on Sunday evening")
print ("Hi "+ invite_people[1] + ", You are invited for adinner on Sunday evening")
print ("Hi "+ invite_people[2] + ", You are invited for adinner on Sunday evening")
print ("Hi "+ invite_people[3] + ", You are invited for adinner on Sunday evening")
print ("Hi "+ invite_people[4] + ", You are invited for adinner on Sunday evening")
print ("Hi "+ invite_people[5] + ", You are invited for adinner on Sunday evening")

print ("Sorry guys, my dinner table have not arrived on time,so please apologise for invitingonly two people for the dinner")
guest1 = invite_people.pop()
print ("Sorry " + guest1 + ", We could make up next time")

guest2 = invite_people.pop()
print ("Sorry " + guest2 + ", We could make up next time")

guest3 = invite_people.pop()
print ("Sorry " + guest3 + ", We could make up next time")

guest4 = invite_people.pop()
print ("Sorry " + guest4 + ", We could make up next time")

print ("Hi " +invite_people[0]+ ", You are invited")
print ("Hi " +invite_people[1]+ ", You are invited")

del invite_people[0]
del invite_people[0]

print ("The guest list is: ")
print (invite_people)
