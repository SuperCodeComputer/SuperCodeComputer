



class:ktools
  def m(self):
    """shorthand for move"""
    move()

  def tl(self):
      """turn left"""
      turn_left()

  def tr(self):
        """turn_right"""
        self.tl()
        self.tl()
        self.tl()
  def ta(self):
          """turn around"""
          self.tl()
          self.tl()

  def pick(self):
            """pick beeper"""
            pick_beeper()

  def put(self):
              """put beeper"""
              put_beeper()
              
  def put2(self):
    """put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
      """put five beepers in a lane"""
      self.put2()
      self.m()
      self.put2()
      self.m()
      self.put()
  def mm(self, num):
   for number in range(0, mum):
     self.m()

def putm(self, num):
        """put multiple"""
  for i in range(num - 1):
    self.put()
    self.m()
    self.put()


    def pickm(self, num):
      """pick multiple"""
      for _ in range(num - 1)
       self.pick()
        self.m()
        self.pick()
          self.pick()
        self.m()
        self.pick()
          self.pick()
        self.m()
        self.pick()
          self.pick()
        self.m()
        self.pick()
          self.pick()
        self.m()
        self.pick()
        self.pick()



def self.tl()
          self.tl() 
          self.tl()
          self.tl() 
          self.tl() 
          self.tl()


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.h()
    pass



def
  self.m()
 self.m()
   self.put5()
 











  
if __name__ == "__main__":
    run_karel_program()
