import wikipedia

print(wikipedia.summary("Wikipedia"))

print(wikipedia.search("Barack"))

ny = wikipedia.page("New York")
print(ny.url())