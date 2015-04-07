# MinHash.py
Estimate similarity of two sets using MinHash and Jaccard distance

# How to use 
```python
number_of_hashes = 200
seed = 0

minHash = MinHash(number_of_hashes, seed)
hashValues1 = minHash.hashString("MRHIAHTQRCLSRLTSLVALLLIVLPMVFSPAHSCGPGRGLGRHRARNLY", noOfShingles = 3, charChingles = True)
hashValues2 = minHash.hashString("MDRDSLPRVPDTHGDVVDEKLFSDLYIRTSWVDAQVALDQIDKGKARGSR", noOfShingles = 3, charChingles = True)
	
similarity = Jaccard.similarity(hashValues1, hashValues2)

print("Jaccard similarity :",  similarity)
print("Jaccard distance   :", (1 - similarity))
```

# Shingles
You can always shingle a text document, as follows:

```python
minHash.hashString("This is a sample text for shingling a text document", noOfShingles = 3, charChingles = False)
```
