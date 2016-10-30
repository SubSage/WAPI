###################
#
#   Given a maximum amount of locations (n) and figures in history (m)
#   and a "villain", create a map of the n most relevant places and
#   populate the locations as evenly as possible.
#
###################
import math


#A maxheap that should sort based on relevance to the "villain", according to
#results from IBM Watson Alchemy
class HeapOfThings:
    def __init__(self):
        self.heap = []
        self.length = 0

    def push(self, thing):
        self.heap += [thing]
        i = len(self.heap) - 1
        self.length +=1
        self.bubbleUp(i)

    def removeMax(self):
        removedThing = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.bubbleDown(0)
        self.length-=1
        return removedThing

    def parent(self, index):
        return self.heap[int(index/2)]

    def leftChild(self, index):
        return self.heap[int(2*index)]

    def rightChild(self, index):
        return self.heap[int(2*index+1)]

    def bubbleUp(self, currentIndex):
        if currentIndex > 0:
            if self.heap[currentIndex].relevance > self.parent(currentIndex).relevance:
                tempThing = self.parent(currentIndex)
                self.heap[int(currentIndex/2)] = self.heap[currentIndex]
                self.heap[currentIndex] = tempThing
                self.bubbleUp(int(currentIndex/2))
            

    def bubbleDown(self, currentIndex):
        if 2*currentIndex + 1 <= len(self.heap) -1:
            if self.rightChild(currentIndex).relevance > self.leftChild(currentIndex).relevance:
                if self.heap[currentIndex].relevance < self.rightChild(currentIndex).relevance:
                    tempThing = self.rightChild(currentIndex)
                    self.heap[2*currentIndex + 1] = self.heap[currentIndex]
                    self.heap[currentIndex] = tempThing
                    self.bubbleDown(int(2*currentIndex + 1))
            elif self.rightChild(currentIndex).relevance < self.leftChild(currentIndex).relevance:
                if self.heap[currentIndex].relevance < self.leftChild(currentIndex).relevance:
                    tempThing = self.leftChild(currentIndex)
                    self.heap[int(2*currentIndex)] = self.heap[currentIndex]
                    self.heap[currentIndex] = tempThing
                    self.bubbleDown(int(2*currentIndex))
        elif 2*currentIndex <= len(self.heap)-1:
            if self.heap[currentIndex].relevance < self.leftChild(currentIndex).relevance:
                tempThing = self.leftChild(currentIndex)
                self.heap[2*currentIndex] = self.heap[currentIndex]
                self.heap[currentIndex] = tempThing 
                self.bubbleDown(int(2*currentIndex))

    #Return n (or all, if n is not specified) things according to their
    #relevance
    def getNLargest(self, n):
        i = 0
        l = []
        while i < n:
            l += [self.removeMax()]
            i +=1

        return l

    def printAll(self):
        for t in self.heap:
            print t.name

#A map of locations that are just kind of arbitrarily thrown around
class MapOfLocations:
    def __init__(self):
        self.map = dict()

    #Add a doubly hashed coordinate-location pair
    def addToMap(self, loc, coord):
        self.map[coord] = loc
        self.map[loc] = coord

    #Given information about a location, return its coordinate pair
    def locationToCoordinate(self, loc):
        return self.map[loc]

    #Given a coordinate pair, return information about that location
    def coordinateToLocation(self, coord):
        return self.map[coord]



    
