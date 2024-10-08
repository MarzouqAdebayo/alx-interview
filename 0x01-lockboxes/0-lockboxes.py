#!/usr/bin/python3
"""
Module '0-lockboxes.py'
"""


def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False
    visitedBoxes = []
    visitBox(0, boxes, visitedBoxes)
    # return len(visitedBoxes) == len(boxes)
    return set(visitedBoxes) == set([i for i in range(len(boxes))])


def visitBox(boxIndex, boxes, visitedBoxes):
    if boxIndex > len(boxes) - 1:
        return
    keys = boxes[boxIndex]
    visitedBoxes.append(boxIndex)
    for key in keys:
        if key not in visitedBoxes:
            visitBox(key, boxes, visitedBoxes)
