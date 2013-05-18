import os, random
from conf import *


class catDb(object):
	def __init__(self):
		self.dbFile = 'catDb.csv'
		self.csvContent = ''
		self.lowestValue = -1
		self.allCats = {}

		if os.path.isfile(self.dbFile):
			dbFileHandle = open(self.dbFile, 'r')
			self.csvContent = dbFileHandle.read()
			dbFileHandle.close()
			for row in self.csvContent.split('\n'):
				keyVal = row.split(';')
				if len(keyVal) == 2:
					self.allCats[keyVal[0]] = int(keyVal[1])
					if (self.lowestValue == -1 or self.allCats[keyVal[0]] < self.lowestValue) and os.path.isfile( "%s/%s" % (pathToCats, keyVal[0]) ):
						self.lowestValue = self.allCats[keyVal[0]]

		for availableCat in os.listdir(pathToCats):
			if availableCat not in self.allCats:
				self.allCats[availableCat] = 0
				self.lowestValue = 0

	def getCat(self):
		catsNeedLoveToo = []
		for cat, count in sorted(self.allCats.iteritems()):
			if count == self.lowestValue and os.path.isfile( "%s/%s" % (pathToCats, cat) ):
				catsNeedLoveToo.append(cat)

		if len(catsNeedLoveToo) == 0:
			raise "NoKittensError: please put a few kittens into :"+ pathToCats

		return random.choice(catsNeedLoveToo)

	def countThatCat(self, cat):
		if cat in self.allCats:
			self.allCats[cat] += 1
		else:
			self.allCats[cat] = 1

	def saveDb(self):
		fullCsv = ''
		for cat, count in self.allCats.iteritems():
			fullCsv += "%s;%d\n" % (cat, count)

		# ONLY save, if DB has been changed!
		if fullCsv != self.csvContent:
			dbFileHandle = open(self.dbFile, 'w')
			dbFileHandle.write(fullCsv)
			dbFileHandle.close()