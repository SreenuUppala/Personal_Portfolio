"""nums = [2, 4, 6, 8, 9, 12, 36, 24, 89, 56]
m =10
hash_table = [None] * m

for num in nums:
    index = num % m

    # Linear probing: find next free index
    while hash_table[index] is not None:
        index = (index + 1) % m

    hash_table[index] = num

print(hash_table)
print(hash_table[2])
print(hash_table[0])
"""
from itertools import count

#3668
"""
order=[3,1,2,5,4]
friends=[1,3,4]
friends_set=set(friends)
s=[o for o in order if o in friends]
print(s)
"""
#duplicate(3289)
"""
nums=[0,1,1,0]
hash_table=set()
empty_list=[]
for num in nums:
    if num in hash_table:
        empty_list.append(num)
    else:
        hash_table.add(num)

print(empty_list)
"""
#1512
"""nums=[1,2,3,1,1,3]
n=len(nums)
count=0
for i in range(n):
    for j in range(i+1,n):

        if nums[i]==nums[j]:
            count=count+1

print(count)
"""
#function
"""
def pairs(nums):

    freq = {}
    count = 0
    for num in nums:
        if num in freq:
            count += freq[num]
            freq[num] += 1
        else:
            freq[num] = 1
    return count
print(pairs([1,2,3,1,1,3]))
"""
#contain duplicates
"""
def containsNearbyDuplicate(nums, k):


    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i

    return False

"""
# current num smaller than num
"""nums=[8,1,2,2,3]
n=len(nums)
hash_table=[]

for i in range(n):
    count = 0
    for j in range(n):
        if nums[j]<nums[i] :
            count=count+1
    hash_table.append(count)


print(hash_table)
"""
#consecative(128)
"""nums=[100,4,200,2,3,1]
n=len(nums)
count=1
longest=1
for num in range(0,n-1):
    if nums[num+1]>nums[num]:
        count=count+1
    else:
        longest=max(longest,count)
        count=1
longest=max(longest,count)
print(longest)
"""
#rnsomeNote(383)
"""
ransomNote = input("Please enter the ransom note: ").lower()
magazine = input("What magazine do you have:").lower()
found=True
for char in ransomNote :
    if magazine.count(char)<ransomNote.count(char):

        found=False
        break
print(found)
"""
#Happy number
num = 19
seen = set()

while num != 1 and num not in seen:
    seen.add(num)
    s=0
    while num>0:

          rem=num % 10
          s+=rem
          num=num // 10
    num=s

if num == 1:
    print(True)
else:
    print(False)
