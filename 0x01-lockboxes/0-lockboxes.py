#!/usr/bin/python3
"""
Module '0-lockboxes.py'
"""


def canUnlockAll(boxes):
    visitedBoxes = set()
    visitBox(0, boxes, visitedBoxes)
    return len(visitedBoxes) == len(boxes)


def visitBox(boxIndex, boxes, visitedBoxes):
    keys = boxes[boxIndex]
    visitedBoxes.add(boxIndex)
    if len(keys) == 0:
        return
    for key in keys:
        if key not in visitedBoxes:
            visitBox(key, boxes, visitedBoxes)
