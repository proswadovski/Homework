# Peyton Roswadovski
# UWYO COSC 1010
# 10/29/24
# HW 02
# Lab Section: 14
# Sources, people worked with, help given to: Ryan Zafft
# your
# comments
# here

#For this homework assignment you will be writing a program that translates between plaintext and Morse Code.


#When your program first starts it should ask the user for the input string. If plaintext alphabet cahracters is entered output the Morse Code equivalent.

#You may assume that only alphabet characters will be entered, and may ignore other input characters.

#You can use the equivalencies below.

# A: .-        N: -.
# B: -...        O: ---
# C: -.-.        P: .--.
# D: -..         Q: --.-
# E: .           R: .-.
# F: ..-.        S: ...
# G: --.         T: -
# H: ....        U: ..-
# I: ..          V: ...-
# J: .---        W: .--
# K: -.-         X: -..-
# L: .-..        Y: -.-- 
# M: --          Z: --..

# Morse_code = {
# "A":" .-",
# "B":"-...",
# "C: -.-.",
# "D: -..",
# "E: .",
# "F: ..-.",
# "G: --.",
# "H: ....",
# "I: ..","J: .---","K: -.-","L: .-..","M: --","N: -.",
# "O: ---","P: .--.","Q: --.-","R: .-.","S: ...","T: -","U: ..-","V: ...-",
# "W: .--","X: -..-","Y: -.--","Z: --.."}

Morse_code = {
"A":" .-",
"B":" -...",
"C":" -.-.",
"D":" -..",
"E":" .",
"F":" ..-.",
"G":" --.",
"H":" ....",
"I":" ..",
"J":" .---",
"K":" -.-",
"L":" .-..",
"M":" --",
"N":" -.",
"O":" ---",
"P":" .--.",
"Q":" --.-",
"R":" .-.",
"S":" ...",
"T":" -",
"U":" ..-",
"V":" ...-",
"W":" .--",
"X":" -..-",
"Y":" -.--",
"Z":" --.."}
 
decoded_message = input("Morse Code Message")
decoded_message = decoded_message.strip()
encoded_message = ""
for char in decoded_message: 
    if char == '':
        encoded_message += " "
    elif char.isalpha():
        morse_code_value = Morse_code[char.upper()]
        encoded_message += morse_code_value

print(encoded_message)






#Your program should output the correct Morse Code regardless of casing of the input characters. You should output spaces in the input string as two spaces, and separation between  Morse Code characters should be a single space.

#For example the message 'Go Pokes' would be equivalent to:

#--. ---  .--. --- -.- . ...

#Where there is a space between the "G" and "o" in Morse code and two spaces between the "Go" and "Pokes".

#Tips and tricks:

#Dictionaries will be your friend for this assignment
#You can utilize the `isalpha()` method on a string to see if it is  an alphabet character
#`if string_variable.isalpha():`
#The Morse Code characters will only ever be `-` or `.`  or a space
#You can treat strings much like you would a list, meaning you can iterate through them and access characters based on an index position
#Remember you can utilize string concatenation with `+=` to build new strings
#Name your file: LastnameFirstname-HW02.py

#Your file MUST include the standard comments at the top of the file that are expected with the labs.
