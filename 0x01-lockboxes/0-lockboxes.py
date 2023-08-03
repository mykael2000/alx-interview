#!/usr/bin/python3
''' working with lockboxes.
'''


def canUnlockAll(boxes):
    '''checks boxes in a list
    '''
    va = len(boxes)
    seenBoxes = set([0])
    unseenBoxes = set(boxes[0]).difference(set([0]))
    while len(unseenBoxes) > 0:
        boxId = unseenBoxes.pop()
        if not boxId or boxIdx >= va or boxId < 0:
            continue
        if boxId not in seenBoxes:
            unseenBoxes = unseenBoxes.union(boxes[boxId])
            seenBoxes.add(boxId)
    return va == len(seenBoxes)
