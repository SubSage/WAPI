from pull_entities import Watson
from MapGenerator import MapOfLocations
from MapGenerator import HeapOfThings
from Vector2 import Vector2

import random
import wikipedia


#BEFORE WE START:
#Here's a very long explanation of what's about to go down:
#Using Watson, we're going to make several quieries in Wikipedia.com
#and will try to generate a game out of it.
#Step 1: Choose a villain in history (Genghis Khan, Vlad the Impaler, etc.)
#Step 2: Choose cities and geographic locations (up to some arbitrary number) to build a world map with random coordinates
#Step 3: Populate the map with people (up to some other arbitrary number and they have to be aligned either against or for the villain)
#	SPECIAL NOTE ON STEP 3: We want close to half of the people to be for the villain and another half to be against the villain
#More steps?

class Things:
	def __init__(self, name, relevance, s = None):
		self.name = name
		self.relevance = relevance
		self.s = None



class GameMap:
	def __init__(self, villain, amt_loc, amt_people, widthAndHeight):
		self.villain = villain	#String containing the name of the villain
		self.Watson = Watson()	#Wrapper class for IBM Watson
		self.max_loca = amt_loc	#Integer for the maximum amount of locations allowed in the world map
		self.max_people = amt_people	#Integer for the maximum amount of people who will populate the world map
		self.widthAndHeight = widthAndHeight

		self.heapOfLocations = HeapOfThings()
		self.heapOfPeople = HeapOfThings()

		self.mapOfLocations = MapOfLocations()
		self.listOfPeople = []

		self.addedLocations = dict()
		self.addedPeople = dict()

		self.amt_cities = 0
		self.amt_people = 0


	#Have IBM Watson search for cities relevant to the villain. If not enough cities are found (half of the total amount of locations we allow),
	#search for cities related to the cities we already found.
	#A NOTE: City names may be EXACTLY THE SAME besides some random character (such as a period)
	def chooseCities(self, keyword):
		content = wikipedia.page(keyword).content
		entities = self.Watson.pull_entities_from_text(content)
		cities = self.Watson.get_cities(entities)

		for city in cities:
			cityThing = Things(city.keys()[0], float(city.values()[0]))
			self.heapOfLocations.push(cityThing)
			self.addedLocations[cityThing.name] = False
			print "Pushing " + cityThing.name
			self.amt_cities +=1


		while self.amt_cities < int(self.max_loca):
			i = 0
			nothingToCheck = True
			print "Checking if there are anymore cities to check for"
			for c in self.heapOfLocations.heap:
				if not self.addedLocations.has_key(c.name):
					nothingToCheck = False
				elif not self.addedLocations[c.name]:
					nothingToCheck = False
			if nothingToCheck:
				print "Dead end in finding locations!"
				break
			else:
				while i < len(self.heapOfLocations.heap) and self.amt_cities < int(self.max_loca):
					content = wikipedia.page(self.heapOfLocations.heap[i].name).content
					entities = self.Watson.pull_entities_from_text(content)
					cities = self.Watson.get_cities(entities)
					for city in cities:
						if not self.addedLocations.has_key(city.keys()[0]):
							cityThing = Things(city.keys()[0], float(city.values()[0]))
							self.heapOfLocations.push(cityThing)
							self.addedLocations[cityThing.name] = False
							print "Pushing " + cityThing.name
							self.amt_cities += 1
						elif not self.addedLocations[city.keys()[0]]:
							self.addedLocations[cityThing.name] = True
							self.amt_cities += 1
				i+=1

	def addLocationsToMap(self, radius):
		places = self.heapOfLocations.getNLargest(self.max_loca)

		partition = self.widthAndHeight.x/(radius + len(places))
		min_range = 0
		for place in places:
			max_range = min_range + partition
			x = random.randrange(min_range, max_range)
			y = random.randrange(0, self.widthAndHeight.y)
			min_range += max_range + radius

			v = Vector2(x, y)
			self.mapOfLocations.addToMap(place.name, v)

	def choosePeople(self, keyword):
		content = wikipedia.page(keyword).content
		entities = self.Watson.pull_entities_from_text(content)
		people = self.Watson.get_people(entities)

		for person in people:
			personThing = Things(person[0], person[2], person[1])
			self.heapOfPeople.push(personThing)
			self.addedPeople[personThing.name] = False
			print "Pushing " + personThing.name
			self.amt_people +=1

		while self.amt_people < int(self.max_people):
			i = 0
			nothingToCheck = True
			print "Checking if there are anymore cities to check for"
			for p in self.heapOfPeople.heap:
				if not self.addedPeople.has_key(p.name):
					nothingToCheck = False
				elif not self.addedPeople[p.name]:
					nothingToCheck = False
			if nothingToCheck:
				print "Dead end in finding people!"
				break
			else:
				while i < len(self.heapOfPeople.heap) and self.amt_people < int(self.max_people):
					content = wikipedia.page(self.heapOfLocations.heap[i].name).content
					entities = self.Watson.pull_entities_from_text(content)
					people = self.Watson.get_people(entities)
					for person in people:
						if not self.addedLocations.has_key(person[0]):
							personThing = Things(person[0], person[2], person[1])
							self.heapOfPeople.push(personThing)
							self.addedPeople[personThing.name] = False
							print "Pushing " + personThing.name
							self.amt_people +=1
						elif not self.addedPeople[person[0]]:
							self.addedPeople[person[0]] = True
							self.amt_people += 1
				i+=1

	def makeListOfPeople(self):
		people = self.heapOfPeople.getNLargest(self.max_people)
		for person in people:
			self.listOfPeople += [person.name]