from pull_entities import Watson
from MapGenerator import MapOfLocations
from MapGenerator import HeapOfThings

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
		self.wAndH = widthAndHeight

		self.heapOfLocations = HeapOfThings()
		self.heapOfPeople = HeapOfThings()

		self.mapOfLocations = MapOfLocations()

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
			self.amt_cities +=1


		while self.amt_cities < int(self.max_loca):
			i = 0
			while i < len(self.heapOfLocations):
				content = wikipedia.page(self.heapOfLocations[i].name).content
				entities = self.Watson.pull_entities_from_text(content)
				cities = self.Watson.get_cities(entities)
				for city in cities:
					if not self.addedLocations.hasKey(city.keys()[0]):
						cityThing = Things(city.keys()[0], float(city.values()[0]))
						self.heapOfLocations.push(cityThing)
						self.addedLocations[cityThing.name] = False
						self.amt_cities += 1
					else:
						self.addedLocations[city.keys()[0]] = True
			i+=1

	def addLocationsToMap(self):
		places = self.heapOfLocations.getNLargest(self.max_loca)

		for place in places:
			x = random.rand(0, xAndH[0])
			y = random.rand(0, xAndH[1])
			self.mapOfLocations.addToMap(place.name, (x,y))

	def findPeople(self, keyword):
		content = wikipedia.page(keyword).content
		entities = self.Watson.pull_entities_from_text(content)
		people = self.Watson.get_people(entities)

		for person in people:
			personThing = Thing(person[0], person[2], person[3])
			self.heapOfPeople.push(personThing)
			self.addedPeople[personThing.name] = False
			self.amt_people +=1

		while self.amt_people < int(self.max_people):
			i = 0
			while i < len(self.heapOfPeople):
				content = wikipedia.page(keyword).content
				entities = self.Watson.pull_entities_from_text(content)
				people = self.Watson.get_people(entities)

				for person in people:
					if not personThing.hasKey(people[0]):
						personThing = Thing(person[0],person[2],person[3])
						self.heapOfPeople.push(personThing)
						self.addedLocations[personThing.name] = False
						self.amt_people +=1
			i+=1






