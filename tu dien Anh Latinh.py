latin_eng = {}
for _ in range(int(input())):
  eng, *latin = input().replace('- ', '').replace(',', '').split()
  for la_word in latin:
    if la_word not in latin_eng.keys():
      latin_eng[la_word] = []
    latin_eng[la_word].append(eng)

print()
print(len(latin_eng))
for w in sorted(latin_eng.keys()):                            
  print(w, '-', ', '.join(sorted(list(set(latin_eng[w])))))