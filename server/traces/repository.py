
import threading
import copy
import trace

_database = dict()
_lock = threading.Lock()


class TraceNotFound(Exception):
  
  _MSG = 'Trace %s not found.'

  def __init__(self, id):
    super(TraceNotFound, self).__init__(TraceNotFound._MSG, id)


def get(id):
  """
  Gets a trace.
  @param id: Trace id
  @return A copy safe trace.
  @throws TraceNotFound when the trace doesn't exist.
  """
  global _lock
  global _database

  print 'Getting trace %s' % id

  trace = None

  _lock.acquire()

  if _database.get(id) is not None:
    trace = copy.deepcopy(_database.get(id))
    _lock.release()
    return trace
  
  _lock.release()

  raise TraceNotFound(id)

def get_all():
  """
  Gets all traces. All entities are copy safe.
  """

  global _lock
  global _database

  print 'Getting all traces.'

  traces = list()

  _lock.acquire()
  for trace in _database.values():
    traces.append(copy.deepcopy(trace))
  _lock.release()

  return traces
  

def persist(trace):
  """
  Inserts an entity into the database. After that, it sets
  the assigned id to the returned object.
  @param trace: Trace entity.
  @return A copy safe entity.
  """

  global _lock
  global _database

  print 'Inserting %s' % trace

  new_trace = None

  _lock.acquire()

  trace.id = len(_database)
  _database[trace.id] = trace
  new_trace = copy.deepcopy(trace)

  _lock.release()

  return new_trace
  
def create(timestamp, flight_id, speed, x, y, z):
  """
  Creates a trace and inserts it in the database.
  @param timestamp: Trace timestamp.
  @param flight_id: Flight identificator.
  @param speed: Speed measure
  @param x: X component.
  @param y: Y component.
  @param z: Z component.
  @return Trace entity.
  @throws ValueError when a type is not correct.
  """

  print 'Creating %s at %s' % (flight_id, timestamp)

  ent = trace.Trace()
  try:
    ent.timestamp = long(timestamp)
  except ValueError as e:
    raise ValueError('Timestamp should be a long')

  ent.flight_id = str(flight_id)

  try:
    ent.speed = float(speed)
  except ValueError as e:
    raise ValueError('Speed should be a float')

  try:
    ent.x = x
    ent.y = y
    ent.z = z
  except ValueError as e:
    raise ValueError('Position coordinates should be floats')

  return persist(ent)

# Tests
create(10, 'RYA919', 500, 3, -4 , 1000)
create(20, 'RYA911', 600, -2, 10 , 8000)
create(30, 'RYA912', 500, 4, 7 , 5000)
create(40, 'RYA913', 700, 7, 0 , 3500)
create(50, 'RYA914', 500, 0, 2 , 3500)
create(60, 'RYA919', 500, -5, -5 , 1250)
