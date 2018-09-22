import time
def insertion_sort(data):
    j = 1
    for j in range(j, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key

unsorted_cards=list(range(1,10)) # this is the list from 1 to 10
unsorted_cards.sort(reverse=True)  #this line I reverse my list, now list is from 10 to 1
print(unsorted_cards)  # this line I print out the cards with reverse order
start = time.time()
insertion_sort(unsorted_cards)   # this line i sort my reverse one to 1,10
print(unsorted_cards)
sum=0
sum = sum + ( time.time()- start )
print(sum)




import time
def insertion_sort(data):
    j = 1
    for j in range(j, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key

unsorted_cards=list(range(1,100)) # this is the list from 1 to 10
unsorted_cards.sort(reverse=True)  #this line I reverse my list, now list is from 10 to 1
print(unsorted_cards)  # this line I print out the cards with reverse order
start = time.time()
insertion_sort(unsorted_cards)   # this line i sort my reverse one to 1,10
print(unsorted_cards)
sum=0
sum = sum + ( time.time()- start )
print(sum)




import time
def insertion_sort(data):
    j = 1
    for j in range(j, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key

unsorted_cards=list(range(1,1000)) # this is the list from 1 to 10
unsorted_cards.sort(reverse=True)  #this line I reverse my list, now list is from 10 to 1
print(unsorted_cards)  # this line I print out the cards with reverse order
start = time.time()
insertion_sort(unsorted_cards)   # this line i sort my reverse one to 1,10
print(unsorted_cards)
sum=0
sum = sum + ( time.time()- start )
print(sum)




import time
def insertion_sort(data):
    j = 1
    for j in range(j, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key

unsorted_cards=list(range(1,10000)) # this is the list from 1 to 10
unsorted_cards.sort(reverse=True)  #this line I reverse my list, now list is from 10 to 1
print(unsorted_cards)  # this line I print out the cards with reverse order
start = time.time()
insertion_sort(unsorted_cards)   # this line i sort my reverse one to 1,10
print(unsorted_cards)
sum=0
sum = sum + ( time.time()- start )
print(sum)