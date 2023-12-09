#!/usr/bin/python3
'''Unlockability of secured containers.
'''


def isUnlockableContainers(containerList):
    '''Checks if all the containers in a list of boxes containing the access
    keys (indices) to other containers can be unlocked, assuming that the first
    container is already unlocked.
    '''
    numContainers = len(containerList)
    visitedContainers = set([0])
    unvisitedContainers = set(containerList[0]).difference(set([0]))

    while len(unvisitedContainers) > 0:
        currentContainerIdx = unvisitedContainers.pop()

        if not currentContainerIdx or currentContainerIdx >= numContainers or currentContainerIdx < 0:
            continue

        if currentContainerIdx not in visitedContainers:
            unvisitedContainers = unvisitedContainers.union(containerList[currentContainerIdx])
            visitedContainers.add(currentContainerIdx)

    return numContainers == len(visitedContainers)
