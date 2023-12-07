#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    boxes (list): A list of lists where each list represents a box and contains keys.

    Returns:
    bool: True if all boxes can be opened, else False.
    """

    unlocked = set([0])

    stack = [key for key in boxes[0]]

    while stack:
        key = stack.pop()

        if key < len(boxes) and key not in unlocked:
            unlocked.add(key)

            stack.extend(boxes[key])

    return len(unlocked) == len(boxes)
