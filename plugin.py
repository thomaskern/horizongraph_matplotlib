import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from data_transformer import DataTransformer
import csv

class Horizon:

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

  def set_theme(self,ax):
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
    
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

  def run(self):
    x,y_all,labels = self.get_data()
    n = len(y_all)

    #F = plt.figure(figsize=(10,2))
    F = plt.figure(figsize=(20,3))
    F.clf()
    F.subplots_adjust(hspace=0) 

    colors = ("#A90E0A","#E02421","#EF9483","#0050A0","#2B7ABD","#8BBCD4")

    df = DataTransformer(y_all)

    for i in range(n):
      ax = F.add_subplot(n, 1, i+1)

      x1, bands = df.transform(y_all[i], x)
      #print(x1)
      #print bands

      for idx,band in enumerate(bands):

        #print(str(x1[idx])+"::"+str(band)+"::"+str(idx))
        l = len(bands)

        ax.fill_between(x1[idx],0,band,color=colors[l - 1 - idx])
        #print filling.get_dashes()
        #x = [5,6,7,8,9]
        #ax.bar(x,band,color=colors[l - 1 - idx],width=0.05,lw=0)

      plt.xlim(0,x[-1])
      plt.ylim(0,df.get_max()/3)
      self.set_theme(ax)
      ax.get_yaxis().set_visible(True)
      ax.set_yticks([])
      ax.set_ylabel(labels[i],rotation="horizontal")

    return plt

if __name__ == "__main__":
  plot = Horizon().run()
  plot.subplots_adjust(left=0.07, right=0.998, top=0.99,bottom=0.01)
  pp = PdfPages('multipage.pdf')
  plot.savefig(pp, format="pdf")
  pp.close()
  
