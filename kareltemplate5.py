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
def sob(self)
"""standing on beeper"""
return beepers_present()

def jump(self)
"""jump for 510"""
while self.fic():
  self.m()
self.tl()
while self.rib():
  self.m()
self.tr()
while self.fic():
  self.m()
self.tl()

def find(self):
  """find for 515"""
 while not facing_north():
   self.tl()
self.m()
if not self.sob():
self.tl()
self.m()
self.tl()
self.m()
for _ in range(2):
  if not self.sob():
    self.m()
    self.tl()
    self.m()
pass






def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.h()
    pass


if __name__ == "__main__":
    run_karel_program ()