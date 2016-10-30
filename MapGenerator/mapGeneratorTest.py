from MapGenerator import HeapOfThings

class things:
        def __init__(self, n, r):
                self.name = n
                self.relevance = r

        def getName(self):
                return self.name

aBunchOfThings = [things("Grababa", 5.62317), things("Hello Games", 0.0), things("Wazzoo", 10.013213123)]

m = HeapOfThings()

n = 0
for x in aBunchOfThings:
        m.push(x)
        m.printAll()
        print "-----"
        n+=1

m.printAll()

l = m.getNLargest(m.length)
