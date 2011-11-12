import csv
import numpy as np

names =["apple","goldman", "google", "bmw", "shell" , "agu", "staples", "yahoo", "cabot","france_telekom"]
#names =["agu"]

def write_to_disk(name, x,y):
  writer = csv.writer(open("data/"+name + "_out_rel.csv","w"), delimiter = ',')
  writer.writerow(["x","y"])
  for i in range(len(x)):
    writer.writerow([x[i],y[i]])

rows = 400

for n in names:
  spamReader = csv.reader(open("data/"+n+ ".csv","rb"))
  row = spamReader.next()
  last = 0
  count = 0
  for row in spamReader:
    last = float(row[1])
    count += 1
    if count == rows:
      break

  spamReader = csv.reader(open("data/"+n+ ".csv","rb"))
  row = spamReader.next()
  row = spamReader.next()
  #last = float(row[1])

  y = []
  count = 0
  for row in spamReader:
    current = float(row[1])
    print(current)

    i = round((current - last) * 100 / last,3)
    y.insert(0,i)
    count += 1
    if count == rows:
      break
    #last = float(row[1])

  #print(len(y))
  x = np.arange(0, 0.05*rows, 0.05)
  #print(len(x))
  write_to_disk(n,x,y)

  print("last:"+str(last))


exit()

x = np.arange(0, 2, 0.05)
y = []
last = np.random.random_integers(-9,9)
y.append(last)

while len(x) != len(y):
  diff = np.random.random_integers(20,60)
  direction = np.random.random_integers(0,1)
  print(direction)

  if last == -9:
    direction = 0

  sub = round(abs(last * diff / float(100)),3)
  print(str(direction) + " :: "+ str(diff) + "::"+str(last)+"::"+str(sub))

  if direction == 1:
    last += sub
  else:
    last -= sub

  if last < -9:
    last = np.random.random_integers(-9,-4)

  if last == 0:
    last = np.random.random_integers(-1,1)

  if last > -1 and last < 1:
    last = np.random.random_integers(-4,4)

  if last > 9:
    last = np.random.random_integers(5,9)

  y.append(last)

print(y)
