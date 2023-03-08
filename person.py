class Person:

    def __init__(self, f_name, l_name):
      self.f_name = f_name
      self.l_name = l_name
      
    def get_full_name(self):
      return f'{self.f_name} {self.l_name}'
      
