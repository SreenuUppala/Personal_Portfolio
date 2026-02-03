#Palindrome Checker
n=input("Enter the Word: ").lower()
if n[::-1]==n:
    print("is Palindrome")
else:
    print("is not palindrome")
