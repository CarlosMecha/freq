
import bottle
import pprint
import repository

def get_all():
  """
  Gets the list of traces.
  @return List of traces.
  """
  
  resp = bottle.response
  resp.body = pprint.pformat(repository.get_all())

  return resp

def get(id):
  """
  Gets a trace.
  @param id: Trace id.
  @return Trace.
  @code 404: Trace doesn't exist.
  @code 400: The id is not valid.
  """

  trace = None

  try:
    trace = repository.get(int(id))
  except repository.TraceNotFound as e:
    raise bottle.HTTPError(status=404)
  except ValueError as ve:
    raise bottle.HTTPError(status=400)

  resp = bottle.response
  resp.body = str(trace)

  return resp

def new():
  """
  Creates a new trace.
  @form timestamp: Timestamp.
  @form flight_id: Flight id.
  @form speed: Speed.
  @form x: X component.
  @form y: Y component.
  @form z: Z component.
  @return Trace.
  @code 400: Some parameter is not defined or incorrect.
  """

  data = bottle.request.forms
  resp = bottle.response

  if data.get('timestamp') is None\
    and data.get('flight_id') is None\
    and data.get('speed') is None\
    and data.get('x') is None\
    and data.get('y') is None\
    and data.get('y') is None:
    raise bottle.HTTPError(status=400)

  try:
    trace = repository.create(data['timestamp'], data['flight_id'], data['speed'], data['x'], data['y'], data['z'])
    resp.body = str(trace)
  except ValueError as e:
    raise bottle.HTTPError(status=400, body=str(e))
  
  return resp

