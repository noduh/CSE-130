# 1. Name:
#      Noah Jorgensen
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      Effeciently find an element in a sorted json file and return True if it's found, and False otherwise.
# 4. Algorithmic Efficiency
#      The effeciency is O(log n). If we say the input isn't the file but just the thing to search for, then every time the loop runs, the number of things it's searching is divided in half. This is the only thing in the program that isn't O(1) and therefore the effeciency is O(log n).
# 5. What was the hardest part? Be as specific as possible.
#      I hit a few bumps when using json properly, and I had a comparison sign swapped the wrong way. After fixing those, everything worked great.
# 6. How long did it take for you to complete the assignment?
#      about 20 minutes

import json


def search(filename, target):
    # Open the file and load into a list
    file_to_search = open(filename)
    list_to_search = json.load(file_to_search)[
        "array"
    ]  # load from json and use the key "array" to load values into list
    file_to_search.close()

    # set initial range of indexes to search
    max_index = len(list_to_search) - 1
    min_index = 0

    # iterate through list cutting the amount of things to search in half each time
    while max_index >= min_index:
        check_index = (min_index + max_index) // 2
        if list_to_search[check_index] == target:  # if it's found, return
            return True
        # adjust indexes based on which direction to sort, and skipping the index we already checked
        elif list_to_search[check_index] > target:
            max_index = check_index - 1
        else:
            min_index = check_index + 1
    return False  # only returns false if the element was never found


# test cases
print(
    search("Lab06.empty.json", "Empty"),                        # not found
    "\n",
    search("Lab06.trivial.json", "trivial"),                    # found
    "\n",
    search("Lab06.trivial.json", "missing"),                    # not found
    "\n",
    search("Lab06.languages.json", "C++"),                      # found
    "\n",
    search("Lab06.languages.json", "Lisp"),                     # not found
    "\n",
    search("Lab06.countries.json", "United States of America"), # found
    "\n",
    search("Lab06.countries.json", "United States"),            # not found
)
