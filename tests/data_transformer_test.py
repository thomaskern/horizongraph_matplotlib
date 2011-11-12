import unittest
from data_transformer import DataTransformer

class DataTransformerTest(unittest.TestCase):
  
  def setUp(self):
    self.d = DataTransformer([[9,-9,0]])
    self.common_x_ret = [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]

    
  # mixed positive and negative values
  def test_top_range_mixed_negative_positives(self):
    self.run_me([4,1,-9],[[1,2,2.5, 3],[1,2,2.5,3],[1,2,2.5,3],[1,2,2.5,3],[1,2,2.5,3],[1,2,2.5,3]],[[0,0,0,3],[0,0,0,3],[0,0,0,3], [3,1,0,0],[1,0,0,0],[0,0,0,0]])

  def test_positive_zero_negative_positive(self):
    self.run_me([4,0,-9],self.common_x_ret,[[0,0,3],[0,0,3],[0,0,3],[3,0,0],[1,0,0],[0,0,0]])

  def test_mixed_zero_at_end(self):
    self.run_me([4,-1,0],[[1,1.5,2,3],[1,1.5,2,3],[1,1.5,2,3],[1,1.5,2,3],[1,1.5,2,3],[1,1.5,2,3]],[[0,0,1,0],[0,0,0,0],[0,0,0,0],[3,0,0,0],[1,0,0,0],[0,0,0,0]])

  def test_positive_negative_positive(self):
    self.run_me([4,1,-9],[[1,2,2.5, 3],[1,2,2.5,3],[1,2,2.5,3],[1,2,2.5,3],[1,2,2.5,3],[1,2,2.5,3]],[[0,0,0,3],[0,0,0,3],[0,0,0,3], [3,1,0,0],[1,0,0,0],[0,0,0,0]])

  def test_positive_zero_negative(self):
    self.run_me([4,1,-9,3],[[1,2,2.5,3,3.5,4],[1,2,2.5,3,3.5,4],[1,2,2.5,3,3.5,4],[1,2,2.5,3,3.5,4],[1,2,2.5,3,3.5,4],[1,2,2.5,3,3.5,4]],[[0,0,0,3,0,0],[0,0,0,3,0,0],[0,0,0,3,0,0], [3,1,0,0,0,3],[1,0,0,0,0,0],[0,0,0,0,0,0]], x_data=[1,2,3,4])


  # only positive OR negatives values

  def test_positive_bottom_edge(self):
    self.run_me([4.5,1,3],self.common_x_ret, [[0,0,0],[0,0,0],[0,0,0], [3,1,3],[1.5,0,0],[0,0,0]])

  def test_zero_at_beginning(self):
    self.run_me([0,3,0],self.common_x_ret,[[0,0,0],[0,0,0],[0,0,0],[0,3,0],[0,0,0],[0,0,0]])

  def test_zero_at_end(self):
    self.run_me([4,3,0],self.common_x_ret,[[0,0,0],[0,0,0],[0,0,0],[3,3,0],[1,0,0],[0,0,0]])

  def test_positive_zero_positive(self):
    self.run_me([4,0,1],self.common_x_ret,[[0,0,0],[0,0,0],[0,0,0],[3,0,1],[1,0,0],[0,0,0]])

  def test_top_range_no_negative(self):
    self.run_me([4,1,9],self.common_x_ret,[[0,0,0],[0,0,0],[0,0,0], [3,1,3],[1,0,3],[0,0,3]])

  def test_edgecases_medium(self):
    self.assertTrue(self.d.transform([2,5.99,3.81],[1,2,3]) == (self.common_x_ret,[[0,0,0],[0,0,0],[0,0,0], [2,3,3],[0,2.99,0.81],[0,0,0]]))

  def test_choice(self):
    self.assertTrue(self.d.transform([4,1,8],[1,2,3]) == (self.common_x_ret,[[0,0,0],[0,0,0],[0,0,0], [3,1,3],[1,0,3],[0,0,2]]))

  def test_edge_top_negative_value(self):
    self.assertTrue(self.d.transform([0,-7.5,-9],[1,2,3]) == (self.common_x_ret,[[0,3,3],[0,3,3],[0,1.5,3], [0,0,0],[0,0,0],[0,0,0]]))

  def test_edge_middle_negative_value(self):
    self.assertTrue(self.d.transform([-3.5,-6,-4],[1,2,3]) == (self.common_x_ret,[[3,3,3],[0.5,3,1],[0,0,0], [0,0,0],[0,0,0],[0,0,0]]))

  def test_edge_bottom_negative_value(self):
    self.run_me([-0.5,-3,-8],self.common_x_ret,[[0.5,3,3],[0,0,3],[0,0,2], [0,0,0],[0,0,0],[0,0,0]])

  def test_regular_bottom_negative_value(self):
    self.run_me([0,-2,-1],self.common_x_ret,[[0,2,1],[0,0,0],[0,0,0], [0,0,0],[0,0,0],[0,0,0]])

  def run_me(self, data, x,y, x_data=[1,2,3]):
    a,b = self.d.transform(data,x_data)
    print a
    print b
    self.assertTrue(a  == x)
    self.assertTrue(b  == y)

