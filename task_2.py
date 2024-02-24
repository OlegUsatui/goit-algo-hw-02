from collections import deque

def is_palindrome(string):
    string = string.lower().replace(" ", "")

    char_queue = deque()
    for char in string:
        char_queue.append(char)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True

input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))