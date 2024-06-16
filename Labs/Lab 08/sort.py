# 1. Name:
#      Noah Jorgensen
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      Sorts a list
# 4. What was the hardest part? Be as specific as possible.
#      blah
# 5. How long did it take for you to complete the assignment?
#      blah

import json

def sort(filename):
    file_to_sort = open(filename)
    list_to_sort = json.load(file_to_sort)[
        "array"
    ]  # load from json and use the key "array" to load values into list
    file_to_search.close()

    sorted_list = []
    for i in len(list_to_sort):
        next_smallest = ""