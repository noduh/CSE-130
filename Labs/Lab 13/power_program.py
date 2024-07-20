# 1. Name:
#      Noah Jorgensen
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      Find the largest average of consecutive numbers in a given list
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was adding a bunch of asserts everywhere
# 5. How long did it take for you to complete the assignment?
#      My guess is the whole thing took about an hour

import json
import io


def largest_average(num_list: list, num_range: int) -> int:
    """
    Purpose:
        Find the largest average of consecutive numbers in a given list.

    Params:
        num_list: list of numbers
        num_range: size of sublist for the average

    Returns:
        int: the largest average of consecutive numbers
    """

    assert all(
        isinstance(element, int) for element in num_list
    ), "list must be all integers"
    assert isinstance(num_range, int), "the range must be an integer"
    assert len(num_list) > num_range, "the list must be larger than the range"

    end_index = len(num_list) - num_range
    avg_list = []
    total = 0

    # First average
    for i in range(num_range):
        total += num_list[i]
    avg_list.append(total / num_range)

    # Remaining averages
    for start_index in range(1, end_index):
        total -= num_list[start_index - 1]
        total += num_list[start_index + num_range - 1]
        avg_list.append(total / num_range)

    # Find largest average
    largest_avg = avg_list[0]
    avg_list_len = len(avg_list)
    for i in range(avg_list_len):
        current_avg = avg_list[i]
        if current_avg > largest_avg:
            largest_average = current_avg

    return largest_average


def list_from_json(filename: str) -> list:
    """
    Purpose:
        Get a list from a json file, provided the file name.

    Params:
        filename: the location of the file

    Returns:
        list: the list stored in the json file, or an empty list if something goes wrong
    """
    assert isinstance(filename, str), "filename must be a string"

    list_from_json = None
    assert_message = ""
    failed = False
    file_to_read = None

    if not filename.split(".")[-1] == "json":
        assert_message = "file must be json"
        failed = True

    try:
        if not failed:
            file_to_read = open(filename)
    except:
        assert_message = "bad filename"
        failed = True

    try:
        if not failed:
            list_from_json = json.load(file_to_read)["array"]
    except:
        assert_message = "bad json"

    if (
        isinstance(file_to_read, io.TextIOBase)
        or isinstance(file_to_read, io.BufferedIOBase)
        or isinstance(file_to_read, io.RawIOBase)
        or isinstance(file_to_read, io.IOBase)
    ):
        if not file_to_read.closed:
            file_to_read.close()

    assert list_from_json != None, assert_message

    return list_from_json


# Test Cases
# average = largest_average(list_from_json("banana.txt"), 0)  # Bad File
# average = largest_average(list_from_json("small.json"), 1000)  # Bad Subset
# average = largest_average(list_from_json("small.json"), 10)  # Small
# average = largest_average(list_from_json("large.json"), 100)  # Large

# print(f"Largest Average: {average}")
