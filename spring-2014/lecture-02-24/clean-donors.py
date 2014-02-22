'''
clean-donors.py

Your assignment is to take a dirty input file of campaign contributions to New York
mayoral candidates and clean it up so it's ready for analysis. Specifically, the 
script should do four things:

- Make sure every text field is in a consistent case (upper, lower or title)
- Be sure amounts are represented as floats, not integers or strings
- Fix the &nbsp; characters in the city field (which are HTML representations of spaces)
by turning them back into actual spaces
- Save the cleaned output back into a list of lists, where you can think of the outer
list as the whole document, and each list within it as a row. In other words, something
like this:

[['row1 data', 'more row1 data'], ['row2 data', 'more row2 data'] ... etc.]

You'll see some code in the body of the program already. It's there to get you started,
so you'll probably want to leave it in.

Hint: Use print statements to check your input and output at various stages of the program!
It's helpful to watch, a step at a time, how your code affects the input as it moves through
your program.
'''


# This opens the input file and splits it into lines of strings. You'll want to
# remember this for the future -- you'll be using it a lot.
data = open('nycdonors-cleanme.csv', 'r').readlines()

# This list should contain the final output
output = []

for line in data:
    # Just a bit of added cleanup because of the file format. Leave this in.
    line = line.replace('\r\n', '')

    ########## YOUR CODE STARTS HERE ##########
    
    print line # You can replace this

    ########## YOUR CODE ENDS HERE ##########

print output # This will show your final output