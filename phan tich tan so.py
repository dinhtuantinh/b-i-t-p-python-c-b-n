n = int(input())
counts = {}
# Print a value:
for _ in range(n):
  for word in input().split():
    counts[word] = counts.get(word, 0) + 1
freqs = [(-count, word) for (word, count) in counts.items()]
for c, word in sorted(freqs):
     print(word,c)