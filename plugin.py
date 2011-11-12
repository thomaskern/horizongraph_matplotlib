import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from data_transformer import DataTransformer
from data_loader import DataLoader

class Horizon:

  def set_theme(self,ax):
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
    
  def run(self, x, y, labels):
    n = len(y)

    F = plt.figure(figsize=(20,3))
    F.clf()
    F.subplots_adjust(hspace=0) 

    colors = ("#A90E0A","#E02421","#EF9483","#0050A0","#2B7ABD","#8BBCD4")

    df = DataTransformer(y)

    for i in range(n):
      ax = F.add_subplot(n, 1, i+1)

      x1, bands = df.transform(y[i], x)
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
  x,y,labels = DataLoader().get_data()
  plot = Horizon().run(x,y,labels)
  plot.subplots_adjust(left=0.07, right=0.998, top=0.99,bottom=0.01)
  pp = PdfPages('multipage.pdf')
  plot.savefig(pp, format="pdf")
  pp.close()
  
