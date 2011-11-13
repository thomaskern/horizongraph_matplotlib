from matplotlib.backends.backend_pdf import PdfPages
from data_loader import DataLoader
from plugin import Horizon, InputError

x,y,labels = DataLoader().get_data()
try:
  plot = Horizon().run(x,y,labels, bands=3)
  plot.subplots_adjust(left=0.07, right=0.998, top=0.99,bottom=0.01)
  pp = PdfPages('multipage.pdf')
  plot.savefig(pp, format="pdf")
  pp.close()
except InputError as e:
  print "Exception thrown. Reason: ", e.value
