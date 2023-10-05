#!/usr/bin/python3
'''LockBoxes Challenge'''

def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not.
    
    Args:
        boxes (list of lists): Each box contains zero or more keys.
        
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''
    if not boxes:
        return False

    length = len(boxes)
    keys = {0}  # Start with the key for the first box
    opened_boxes = set()

    while keys:
        current_key = keys.pop()
        if current_key < length and current_key not in opened_boxes:
            opened_boxes.add(current_key)
            keys.update(boxes[current_key])

    return len(opened_boxes) == length
