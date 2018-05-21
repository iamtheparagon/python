# ex11.py

print "First Name: ",
name = raw_input()
print "Last Name: ",
surname = raw_input()
print "Address: ",
address = raw_input()
print "City: ",
city = raw_input()
print "State: ",
state = raw_input()
print "Zip Code: ",
zipcode = raw_input()

print "Let me repeat the information."
print "Your name is %r %r." % (name, surname)
print "You live at %r," % (address)
print "in %r %r, %r." % (city, state, zipcode)
print "Correct?"
