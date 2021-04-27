lines = open("review_04.txt", "r").read()

lines = lines.replace(", ","\n")
lines = lines.replace("[","")
lines = lines.replace("]","")

f = open(f'clean_data.txt','w')

f.write(lines)