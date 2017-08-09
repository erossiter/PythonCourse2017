class Clock(object):
  def __init__(self, hour, minutes):
    self.minutes = int(minutes)
    self.hour = int(hour)

  @classmethod
  def at(cls, hour, minutes=0):
    return cls(int(hour), int(minutes))

  def __str__(self):
    if len(str(self.minutes)) == 1 and len(str(self.hour)) == 1:
      time = "0%s:0%s" % (self.hour, self.minutes)
    elif len(str(self.minutes)) == 1:
      time = "%s:0%s" % (self.hour, self.minutes)
    elif len(str(self.hour)) == 1:
      time = "0%s:%s" % (self.hour, self.minutes)
    else:
      time = "%s:%s" % (self.hour, self.minutes)
    return time
    
  def __add__(self, minutes):
    total_minutes = self.minutes + minutes

    if total_minutes < 60 and total_minutes > 0:
      self.minutes = total_minutes
    else:
      self.minutes = total_minutes % 60
      self.hour += round(total_minutes / 60)
    
    while self.hour < 0 or self.hour >= 24:
      if self.hour <= 0:
        self.hour += 24     
      if self.hour >= 24:
        self.hour -= 24

    return Clock(self.hour, self.minutes)
    
  def __sub__(self, minutes):
    minutes *= -1
    return self + minutes

  def __eq__(self, other):
    return self.hour == other.hour and self.minutes == other.minutes

  def __ne__(self, other):  
    return not self.__eq__(other)

# clock1 = Clock(23, 5)
# clock2 = Clock(12, 45)

# print clock1 == clock2
# print clock1 != clock2

# print "\ntesting addition"
# clock1 + 60
# print "minutes: %s" %  clock1.minutes
# print "hour: %s" %  clock1.hour

# print "\ntesting subtraction"
# clock1 - 100
# print "minutes: %s" %clock1.minutes
# print "hour: %s" % clock1.hour

# print "\ntesting subtraction"
# clock2 - 5
# print "minutes: %s" % clock2.minutes
# print "hour: %s" %  clock2.hour

# print "\ntesting subtraction"
# clock2 - 65
# print "minutes: %s" % clock2.minutes
# print "hour: %s" %  clock2.hour

# print "\ntesting subtraction"
# clock3 = Clock(1, 5)
# clock3 - 60
# print "minutes: %s" % clock3.minutes
# print "hour: %s" %  clock3.hour

