import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from data_transformer import DataTransformer
from data_loader import DataLoader

class InputError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return rep(self.value)

class Horizon:

  def set_theme(self,ax):
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
    
  def adjust_visuals_line(self, x, df, ax, i):
    plt.xlim(0,x[-1])
    plt.ylim(0,df.get_max()/3)
    self.set_theme(ax)
    ax.get_yaxis().set_visible(True)
    ax.set_yticks([])
    ax.set_ylabel(labels[i], rotation="horizontal")
    
  def check_valid_params(self, x,y,labels, figsize, bands, colors):
    if bands * 2 != len(colors):
      raise InputError("Number of bands invalid for number of colors")
    pass

  def run(self, x, y, labels, figsize=(20,3), bands=2, colors=("#8BBCD4","#2B7ABD","#0050A0","#EF9483","#E02421", "#A90E0A")): # dark blue, medium blue, light blue, dark red, medium red, light red

    self.check_valid_params(x,y,labels,figsize,bands,colors) 
    n = len(y)

    F = plt.figure(figsize=figsize)
    F.clf()
    F.subplots_adjust(hspace=0) 

    df = DataTransformer(y, bands)

    for i in range(n):
      ax = F.add_subplot(n, 1, i+1)

      x1, bands = df.transform(y[i], x)
      #print(x1)
      #print bands

      for idx,band in enumerate(bands):

        #print(str(x1[idx])+"::"+str(band)+"::"+str(idx))
        l = len(bands)

        ax.fill_between(x1[idx],0,band,color=colors[idx])
        #print filling.get_dashes()
        #x = [5,6,7,8,9]
        #ax.bar(x,band,color=colors[l - 1 - idx],width=0.05,lw=0)

      self.adjust_visuals_line(x,df,ax, i)

    return plt

if __name__ == "__main__":
  x,y,labels = DataLoader().get_data()
  #plot = Horizon().run(x,y,labels,colors=("#0050A0","#8BBCD4","#A90E0A","#EF9483"))
  try:
    plot = Horizon().run(x,y,labels, bands=3)
    plot.subplots_adjust(left=0.07, right=0.998, top=0.99,bottom=0.01)
    pp = PdfPages('multipage.pdf')
    plot.savefig(pp, format="pdf")
    pp.close()
  except InputError as e:
    print "Exception thrown. Reason: ", e.value
  
