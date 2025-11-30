#WAP to to input any alphabet and check whether it is vowel or consonant
char =  str(input("Enter any alphabet :"))

vowel = "aeiouAEIOU"

if(char in vowel):
    print("It is vowel .")
else:
    print("Mentioned alphabet is consonant.")
