#!/usr/bin/env python3
'''Python lockboxes using breadth first search algorithm'''

def canUnlockAll(boxes):
    n = len(boxes)
    key = set(boxes[0])
