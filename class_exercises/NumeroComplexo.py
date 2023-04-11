class NumeroComplexo():
  def __init__(self, r, i):
    self.r = r
    self.i = i
  def multiplica_por(self, num):
    temp_i = self.i * num.r + self.r * num.i
    temp_r = self.r * num.r - self.i * num.i
    return NumeroComplexo(temp_r, temp_i)
 def __(str)__(self):
  if self.i < 0:
    return f'{self.r}{self.i}j'
  return f'{self.r}+{self.i}j''

