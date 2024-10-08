#!/usr/bin/python3
"""
Module '0-lockboxes.py'
"""


def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False

    visitedBoxes = set()
    visitBox(0, boxes, visitedBoxes)

    return len(visitedBoxes) == len(boxes)


def visitBox(boxIndex, boxes, visitedBoxes):
    if boxIndex >= len(boxes) or boxIndex in visitedBoxes:
        return

    visitedBoxes.add(boxIndex)

    for key in boxes[boxIndex]:
        visitBox(key, boxes, visitedBoxes)
