import itertools

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

arr = ["AANPASSEN", "BEREIDDE", "CITATEN"
"DRANK", "ENTER", "FOTOGRAFIE",
"GENAAMD", "HERTZ", "INLEIDER",
"JOURNALIST", "KLOOTZAK", "LANDELIJKE",
"MOTIE", "NAUW", "OFFSET",
"POSEREN", "QUASI", "REALISEREN",
"SCHRIJVER", "TIMMEREN", "UTOPISCH",
"VERRASSING", "WAARDEREN", "MIXED",
"ZOVEEL", "ZUIDELIJKE", "ZANGER",
"COMPLEX", "FYSIEK", "ZESTIEN"]

def check(arr):
	str = ""
	for i in arr:
		str += i
	if (''.join(sorted(set(str))) == alphabet):
		return arr


n = 8
for comb in itertools.combinations(arr, n):
	found  = check(comb)
	if found:
		sum = 0
		for i in found:
			sum += len(i)
		print(found, sum)


