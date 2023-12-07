import os

here = os.path.dirname(os.path.abspath(__file__))
list = open(os.path.join(here, 'word_list.txt')) # Include database of words to scan
racism = 0

for word in list:
    if "nigga" in word or "nigger" in word or "chinese" in word:
        print(word)
        racism += 1

if racism > 0:
    print("This text file contains "+str(racism)+" racism.")
else:
    print("This text file is devoid of any racism.")
