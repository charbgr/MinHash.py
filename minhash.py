import random
from hashlib import sha1
import distance

class MinHash(object):

	MAX_HASH = (1 << 32) - 1
	HASH_RANGE = (1 << 32)

	def __init__(self, numOfHashes = 200, seed = 0):
		super(MinHash, self).__init__()

		if numOfHashes <= 0:
			raise ValueError("Number Of Hashes must not be zero.")
		elif numOfHashes > self.HASH_RANGE:
			raise ValueError("Cannot have more than %d number of\
                    hash functions" % self.HASH_RANGE)

		self.numOfHashes = numOfHashes
		random.seed(seed)

		def create_perms():
			a = random.randint(1, self.MAX_HASH)
			b = random.randint(0, self.MAX_HASH)
			return lambda x : ((a * x + b)) % self.HASH_RANGE

		self.permutations = [create_perms() for _hash in range(numOfHashes)]



	def hashString(self, inputStr, noOfShingles = 2, charChingles = True):
		def hash(input):

			hashValue = int(input.hexdigest()[:8], 16) #8 bytes of 64 bits
			for i, hashFunc in enumerate(self.permutations):
				retValue = hashFunc(hashValue)
				if retValue < hashValues[i]:
					hashValues[i] = retValue

		shingles = Shingles.getCharShingles(inputStr, noOfShingles) if charChingles else Shingles.getShinglesFromText(inputStr, noOfShingles)
	
		hashValues = [self.MAX_HASH for _ in range(self.numOfHashes)]

		for shingle in shingles:
			shingleHex = sha1(shingle.encode('utf8'))
			hash(shingleHex)

		return hashValues

class Shingles(object):
	def __init__(self):
		super(Shingles, self).__init__()

	@staticmethod
	def getCharShingles(input, noOfShingles):
		return [input[i:i + noOfShingles] for i in range(len(input) - noOfShingles + 1)]

	@staticmethod
	def getShinglesFromText(input, noOfShingles):
		input = input.split()
		return [' '.join(input[i:i+noOfShingles]) for i in range(len(input) - noOfShingles +1)]



class Jaccard(object):

	def __init__(self):
		super(Jaccard, self).__init__()

	@staticmethod
	def similarity(a, b):
		if len(a) + len(b) == 0:
			return 0
		aSet = set(a)
		bSet = set(b)

		intersection = len(aSet.intersection(bSet))

		return float(intersection) / (len(aSet) + len(bSet) - intersection)
		#return float(intersection) / float(min([len(aSet), len(bSet)]))

	@staticmethod
	def distance(a, b):
		return 1 - Jaccard.similarity(a, b)

if __name__ == '__main__':
		
	minHash = MinHash(4, 0)
	tests = ["IONIO NHSI", "IOIOIO NHNHNHSIA"]
	hashValues = [None for _ in range(len(tests))]
	noOfShingles = 3

	for idx, test in enumerate(tests):
		print("TESTING -->", test)
		hashValues[idx] = minHash.hashString(test, noOfShingles)
		print("HashValues -->", hashValues[idx])


	print("\n============\n")

	print("Jaccard similarity:\t", Jaccard.similarity(hashValues[0], hashValues[1]))
	

