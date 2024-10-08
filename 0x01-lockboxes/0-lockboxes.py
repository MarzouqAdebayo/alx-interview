#!/usr/bin/python3
"""
Module '0-lockboxes.py'
"""


def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False

    visitedBoxes = set()
    keys = [0]

    while keys:
        currentKey = keys.pop()
        if currentKey not in visitedBoxes:
            visitedBoxes.add(currentKey)
            for key in boxes[currentKey]:
                if key < len(boxes):
                    keys.append(key)

    return len(visitedBoxes) == len(boxes)
