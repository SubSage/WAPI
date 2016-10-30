from pull_entities import Watson
import wikipedia
import json

w = Watson()

q = wikipedia.page("Vlad the Impaler").content

p = w.pull_entities_from_text(q)

s = w.get_people(p)

print (s)

for t in s:
    print t[0]
