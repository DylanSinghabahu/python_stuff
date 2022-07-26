for item in range(5, 10, 2): #iterates each number within the range by 2
    print(item)
print("------------------------------")
for poo in range(5, 10): #iterates the numbers in the range 5-10, exlcuding 10
    print(poo)
print("------------------------------")
for po in (1,2,3,4,5): #iterates each number
    print(po)
print("------------------------------")
for pp in range(10):
    print(f"pp is {pp}")
print("------------------------------")
for po1 in ('Mosh', 'John', 'Sarah'): #iterates each word
    print(po1)
print("------------------------------")
for poe in ("Mosh"): #iterates each letter of the word
    print(poe)
print("--------------------------------------------------------------")
prices = (10, 20, 30)
total = 0
for price in prices:
    total = total + price # iteration: so starts with 10 + 0, makes new "total"=10, then 10 + 20 = new total 30, and 30+30 = 60
    #total += price is the same
print("Total:"+str(total))

print("----------------------")
#Example
x=3
x+=3
print(x)

print("-------------")

friends = ["Jim", "Kim", "Josh", "Tom"]

# print(len(friends)) --> Gives "4" meaning 4 elements

for index in range(len(friends)):  # Gives range of the 4 elements "0,1,2,3"
    # print(index) --> iterates through each index of the elements "0" "1" "2"
    print(friends[index])  # prints the elements, based on the iterated index: "print(friends[0]) --> Jim

