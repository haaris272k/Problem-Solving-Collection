"""Problem Statement –

You have write a function that accepts, a string which length is “len”, the string has some “#”, in it you have to move all the hashes to the front of the string and return the whole string back and print it.

 


 

example :-

Sample Test Case

Input:

Move#Hash#to#Front

Output:

###MoveHashtoFront"""

string = "Move#Hash#to#Front"
hashes = ""
for i in string:
    if i == "#":
        string = string.replace(i, "")
        hashes += i

final_string = hashes + string
print(final_string)