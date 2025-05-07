#1
x="youssef"
print(len(x))
y="samir"
k=0
for i in  y:
    k+=1
print(k)
#2
z=input("please enter a word")
if len(z)<2:
    print("empty string")
else:
    print(z[:2]+z[-2:])
#3
u=input("please enter a word")
if len(u)<3:
    print(u)
elif u[-3:] == "ing" :
    print(u[0:-3]+"ly")
else:
    print((u) + "ing")
#4
def find_longest_word(word_list):
    longest_word = max(word_list, key=len)
    return longest_word, len(longest_word)
words = ["Python", "Exercises", "Tutorial", "Code"]
longest, length = find_longest_word(words)
print(longest)
print(length)
#5
x=input("please enter a word")
print("e"+x[1:-1]+"e")
for i in x:
    print("e"+x[1:-1]+"e")
    break
#6
n=input("please enter a word")
print(n[::2])
#7
text = "amr and ahmed are frindes but amr is the tallest"
words = text.lower().split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print( word_count)
print( word_count.get('amr', 0))
#8
x=input("please enter a word")
print(x.upper())
print(x.lower())
#9
x=input("please enter a word")
if len(x)%4==0:
    print(x[::-1])
else:
    print(x)
#10
x="hello\nworld"
print(x.replace("\n"," "))
#11
x=input("please enter a word")
if x.startswith("#") or x.startswith("@") or x.startswith("&") or x.startswith("$"):
    print(" string starts with specified charc")
else:
    print("string does not  starts with specified charc")
#12
text = """ronaldo is the
best player in
the whole world."""
prefix = ">> "
modified_text = '\n'.join(prefix + "youssef" for _ in text.splitlines())
print(modified_text)
#13
x=float(input("please enter a number"))
rounded_number= round(x,2)
print(rounded_number)
#14
x=float(input("please enter a number"))
rounded_number= round(x,2)
if rounded_number>0:
    print("+",rounded_number)
else:
    print(rounded_number)
#15
x=int(input("please enter a number"))
y=f"{x:,}"
print(y)
#16
x=input('please enter a word')
print(x[::-1])
x=list(x)
x.reverse()
print("".join(x))
#17
text = "football"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print("Repeated characters:")
for char, count in char_count.items():
    if count > 1:
        print(f"{char}: {count}")
#18
text = "football"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
for char in text:
    if char_count[char] == 1:
        first_non_repeating = char
        break
print(first_non_repeating)
#19
x=input("please enter a word")
x=list(x)
x="".join(x)
print(x[::2])
#20
text = "ton"
n = len(text)
total_substrings = n * (n + 1) // 2
print(total_substrings)
#21
x=[2,6,22,13,3,12]
x[0],x[-1]=x[-1],x[0]
print(x)
#22
x=[17,18,2,16,7,8,33]
x[0],x[3]=x[3],x[0]     #17 swaped with 16
print(x)
#23
my_list = [1, 2, 3, 4, 5]
print(len(my_list))
#23 second way
my_list = [5, 2, 10, 4, 5]
count = 0
for _ in my_list:
    count += 1
print(count)
#24
x=[22,88.76,3,255,1]
print(max(x))
#25
x=[22,88.76,3,255,1]
print(min(x))
#26
x=[17,18,2,16,7,8,33]
print(2 in x)
print(99 in x)
#27
x = [1, 2, 3]
x.clear()
print(x)
#27 2nd
x = [1, 2, 3]
x= []
print(x)
#28
x=[17,18,2,16,7,8,33,17,2]
x=list(dict.fromkeys((x)))
print(x)
#29
test_list = ["Gfg", 3, "is", 8]
key_list = ["name", "id"]
result = [dict(zip(key_list, test_list[i:i+len(key_list)])) for i in range(0, len(test_list), len(key_list))]
print(result)
#30
x = [1, 2, 2, 3, 4, 4, 5]
unique_count = len(set(x))
print(unique_count)
#30 2nd
x = [1, 2, 2, 3, 4, 4, 5]
unique_count = len(dict.fromkeys(x))
print(unique_count)
#31
test_list = [7, 6, 7, 0, 0, 7, 0, 7, 0, 8]
K = 3
freq = {}
for num in test_list:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
result = []
for key in freq:
    if freq[key] > K:
        result.append(key)
print( result)
#32
x=[2,3,4,5,6,7]
y=[max(a,b) for a,b in zip(x,x[1:])]
print(y)
#33
digits = [5, 6, 7]
for i in digits:
    for j in digits:
        for k in digits:
            if i != j and j != k and i != k:
                print(i, j, k,)

#34
test_list = [8, 5, 3]
def generate_combinations(start, path):
    if path:
        result.append(path)
    for i in range(start, len(test_list)):
        generate_combinations(i + 1, path + [test_list[i]])
result = []
generate_combinations(0, [])
for combo in result:
    print(combo)
#35
List_1 = ["a", "b"]
List_2 = [1, 2]
def generate_unique_combinations():
    result = []
    for i in range(len(List_2)):
        for j in range(len(List_2)):
            if i != j:
                combo = [(List_1[0], List_2[i]), (List_1[1], List_2[j])]
                result.append(combo)
    return result
Unique_combination = generate_unique_combinations()
for combo in Unique_combination:
    print(combo)
#36
input_list = [1, 1, 2, 3, 4, 5, 1, 2, 1]
element_to_remove = 1
output_list = [x for x in input_list if x != element_to_remove]
print(*output_list)
#37
list1 = ['Gfg', 'is', 'best']
list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
result = [list1[i] for i in list2]
print(result)
#38
def retain_records_simple(test_list, K, N):
  return [record for record in test_list if record.count(K) == N]
test_list1 = [(4, 5, 5, 4), (5, 4, 3)]
K1 = 5
N1 = 2
output1 = retain_records_simple(test_list1, K1, N1)
print(f"Input : test_list = {test_list1}, K = {K1}, N = {N1} Output : {output1}")
test_list2 = [(4, 5, 5, 4), (5, 4, 3)]
K2 = 5
N2 = 3
output2 = retain_records_simple(test_list2, K2, N2)
print(f"Input : test_list = {test_list2}, K = {K2}, N = {N2} Output : {output2}")
#39
array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
sorted_by_column_0 = sorted(array, key=lambda x: x[0])
print( sorted_by_column_0)
sorted_by_column_1 = sorted(array, key=lambda x: x[1])
print( sorted_by_column_1)
sorted_by_column_2 = sorted(array, key=lambda x: x[2])
print( sorted_by_column_2)
#40
x={5:"youssef",8:"mohamed",1:"ahmed",3:"samir"}
y=dict(sorted(x.items()))
print(y)
#41
x = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
K = 7
keys_to_remove = [key for key, value in x.items() if type(value) == int and value > K]
for key in keys_to_remove:
    del x[key]
print(x)
#42
x={"zed":1,'ahly':4}
y={"pet":3,"tnt":6}
z={"lol":7,"kick":9}
x.update(y),x.update(z)
print(x)
#43
x={"zed":1,'ahly':4,"ko":8}
for key,value in x.items():
    print(f"{key}: {value}")
#44
x={"zed":1,'ahly':4}
y={"pet":3,"tnt":6}
z=x.copy()
z.update(y)
print(z)
#45
x={"lol":7,"kick":9,"shed":10,"like":2}
y=max(x.values())
z=min(x.values())
print(y,z)
#46
original_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
new_dict = {key: value for key, value in original_dict.items() if value}
print(new_dict)
#47
x=(10,11,80,3,77)
print(x[2])
#48
x,y,z=(10,20,30)
print(x)
print(y)
print(z)
#49
x=(10,11,80,3,77)
x=list(x)
x.append("koko")
print(tuple(x))
#50
x=("kok","mok","tok","lok")
s=" ".join(x)
print(type(s))
#51
x=["shok",8,"mok","pok",4]
x=tuple(x)
print(x)
print(type(x))
#52
x=("kok",5,"tok","lok",9)
y=x[::-1]
print(y)
#53
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in sample_list]
print(updated_list)
#54
original_str = "youssef"
cleaned_str = original_str.replace(" ", "")
result_tuple = tuple(cleaned_str)
print(result_tuple)
#55
x = ((10, 20, 30), (40, 50, 60), (70, 80, 90))
total = 0
count = 0

for t in x:
    for num in t:
        total += num
        count += 1

average = total / count if count != 0 else 0
print( average)
#56
x={1,4,7,3,8}
x.add(9)
print(x)
#57
x={1,4,7,3,8}
x.discard(3)
print(x)
#58
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1 & set2
print(intersection)
union = set1 | set2
print( union)
difference = set1 - set2
print(difference)
symmetric_difference = set1 ^ set2
print(symmetric_difference)
#59
x={1,4,7,3,8,5}
print(max(x))
print(min(x))
#60
numbers = [2, 4, 3, 5, 7, 8, 1]
target_sum = 9
pairs = []
s = set()

for num in numbers:
    complement = target_sum - num
    if complement in s:
        pairs.append((complement, num))
    s.add(num)
print( target_sum, pairs)






















