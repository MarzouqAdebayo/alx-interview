def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False

    visitedBoxes = set()
    keys = [0]

    while keys:
        box = keys.pop()
        if box not in visitedBoxes:
            visitedBoxes.add(box)
            for key in boxes[box]:
                if key < len(boxes):
                    keys.append(key)
    return len(visitedBoxes) == len(boxes)
