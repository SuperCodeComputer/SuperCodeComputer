from stanfordkarel import *



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

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.h()
    pass


if __name__ == "__main__":
    run_karel_program()