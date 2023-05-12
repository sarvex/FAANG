# 19th Solution
#---------------------------------------------------------

import sys

class Solution:
    def __init__(self):
        self.mystack = []
        self.myqueue = []
        return None

    def pushCharacter(self, char):
        self.mystack.append(char)

    def popCharacter(self):
        return self.mystack.pop(-1)

    def enqueueCharacter(self, char):
        self.mystack.append(char) 

    def dequeueCharacter(self):
        return self.mystack.pop(0)
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
isPalindrome = all(
    obj.popCharacter() == obj.dequeueCharacter() for _ in range(l // 2)
)
#finally print whether string s is palindrome or not.
if isPalindrome:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")    

