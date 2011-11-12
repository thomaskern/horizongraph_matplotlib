import csv

class DataLoader:
  def write_to_disk(self, writer,typ,x,y):
    writer.writerow(["x","y","type"])
    for i in range(len(x)):
      writer.writerow([x[i],y[i],typ])

  def read_csv(self,filename):
    x = []
    y = []
    spamReader = csv.reader(open("data/"+filename,"rb"))
    spamReader.next()
    for row in spamReader:
      x.append(float(row[0]))
      y.append(float(row[1]))
    return x,y

  def get_data(self):
    y_all = []

    #x, y = self.generate_random_x_y()
    x, y = self.read_csv("apple_out_rel.csv")
    x, y1 = self.read_csv("bmw_out_rel.csv")
    x, y2 = self.read_csv("google_out_rel.csv")
    x, y3 = self.read_csv("goldman_out_rel.csv")
    x, y4 = self.read_csv("shell_out_rel.csv")
    x, y5 = self.read_csv("agu_out_rel.csv")
    x, y6 = self.read_csv("staples_out_rel.csv")
    x, y7 = self.read_csv("yahoo_out_rel.csv")
    x, y8 = self.read_csv("cabot_out_rel.csv")
    x, y9 = self.read_csv("france_telekom_out_rel.csv")
    y_all.append(y5)
    y_all.append(y)
    y_all.append(y8)
    y_all.append(y1)
    y_all.append(y9)
    y_all.append(y2)
    y_all.append(y3)
    y_all.append(y4)
    y_all.append(y6)
    y_all.append(y7)
    labels = ["Agu", "Apple", "Cabot", "BMW", 'France Telekom', 'Google', 'Goldman', 'Shell',  "Staples", "Yahoo"]
    #writer = csv.writer(open("data.csv","w"), delimiter = ',')
    #self.write_to_disk(writer,"",x,y)

    #y_all = [y4]
    #y_all = [
        #[-2 , -5 , 1 , -1 , 2 , 5 , 6 , -1 , -9]]
    #x = [0  , 1  , 2 , 3  , 4 , 5 , 6 , 7  , 8]

    #for i in range(n):
      #x1,y1 = self.generate_random_x_y()
      #y_all.append(y1)
      #y_all.append(y)

    #x1,y1 = self.generate_random_x_y(y_max=3)
    #y_all.append(y1)
    #n += 1
    #print(y_all)

    return x,y_all, labels

