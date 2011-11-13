import unittest
from plugin import Horizon, InputError

class TestSequenceFu(unittest.TestCase):

  # parameter tests
  def test_throw_exception_diff_length_labels_y(self):
    x = [1,2,3]
    y = [[1,2,3]]
    labels = ["Bmw", "Audi"]
    self.assertRaises(InputError, Horizon().run, x,y,labels, bands=3)
    
  def test_throw_exception_more_y_than_labels(self):
    x = [1,2,3]
    y = [[1,2,3],[1,2,3],[1,2,3]]
    labels = ["Bmw", "Audi"]
    self.assertRaises(InputError, Horizon().run, x,y,labels)
  
  def test_throw_exception_more_colors_than_bands(self):
    x = [1,2,3]
    y = [[1,2,3],[1,2,3]]
    labels = ["Bmw", "Audi"]
    colors = ["darkblue","lightblue","redblue","reddishblue"]
    self.assertRaises(InputError, Horizon().run, x,y,labels,colors=colors,bands=1)

  def test_throw_exception_more_bands_than_colors(self):
    x = [1,2,3]
    y = [[1,2,3],[1,2,3]]
    labels = ["Bmw", "Audi"]
    colors = ["darkblue","lightblue","redblue","reddishblue"]
    self.assertRaises(InputError, Horizon().run, x,y,labels,colors=colors)
    
  def test_no_exception_equal_bands_colors(self):
    x = [1,2,3]
    y = [[1,2,3],[1,2,3]]
    labels = ["Bmw", "Audi"]
    colors = ["black","white"]
    Horizon().run(x,y,labels,colors=colors,bands=1)
    self.assertTrue(True)

  def test_throw_exception_one_diff_y_x(self):
    x = [1,2,3]
    y = [[1,2,3],[1,2]]
    labels = ["Bmw", "Audi"]
    self.assertRaises(InputError, Horizon().run, x,y,labels)
  
  def test_throw_exception_diff_y_x(self):
    x = [1,2]
    y = [[1,2,3],[1,2,3]]
    labels = ["Bmw", "Audi"]
    self.assertRaises(InputError, Horizon().run, x,y,labels)
  
  def test_no_exception_equal_length_labels_y(self):
    x = [1,2,3]
    y = [[1,2,3],[1,2,3]]
    labels = ["Bmw", "Audi"]
    print Horizon().run(x,y,labels, bands=3)
    self.assertTrue(True)
    
