#!/usr/bin/python3

correct = __import__("0-lockboxes").canUnlockAll
canUnlockAll = __import__("iterative_lockbox").canUnlockAll
recur = __import__("recursive_lockbox").canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes) == correct(boxes) == recur(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 9, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes) == correct(boxes) == recur(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes) == correct(boxes) == recur(boxes))

boxes = []
print(canUnlockAll(boxes) == correct(boxes) == recur(boxes))

boxes = [[4], [1], []]
print(canUnlockAll(boxes) == correct(boxes) == recur(boxes))

boxes = [[2], [], [0]]
print(canUnlockAll(boxes) == correct(boxes) == recur(boxes))

boxes = [[3], [], [3]]
print(canUnlockAll(boxes) == correct(boxes) == recur(boxes))

boxes = [[1], [2], [3, 7, 8, 9, 10], [4], [6]]
print(canUnlockAll(boxes) == correct(boxes) == recur(boxes))
