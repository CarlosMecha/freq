
class Trace(object):

  _id = None
  _timestamp = None
  _flight_id = None
  _speed = None
  _x = None
  _y = None
  _z = None

  def __init__(self):
    pass

  @property
  def id(self):
    return self._id

  @id.setter
  def id(self, id):
    self._id = id

  @property
  def timestamp(self):
    return self._timestamp

  @timestamp.setter
  def timestamp(self, timestamp):
    self._timestamp = timestamp

  @property
  def flight_id(self):
    return self._flight_id

  @flight_id.setter
  def flight_id(self, flight_id):
    self._flight_id = flight_id

  @property
  def speed(self):
    return self._speed

  @speed.setter
  def speed(self, speed):
    self._speed = speed

  @property
  def x(self):
    return self._x

  @x.setter
  def x(self, x):
    self._x = x

  @property
  def y(self):
    return self._y

  @y.setter
  def y(self, y):
    self._y = y

  @property
  def z(self):
    return self._z

  @z.setter
  def z(self, z):
    self._z = z

  def __repr__(self):
    return '{Trace: %s}' % (', '.join([
      'ID=%s' % self.id, 
      'T=%s' % self.timestamp, 
      'Flight=%s' % self.flight_id,
      'Speed=%s' % self.speed, 
      'X=%s' % self.x,
      'Y=%s' % self.y,
      'Z=%s' % self.z
    ]))

  def __str__(self):
    return self.__repr__()
