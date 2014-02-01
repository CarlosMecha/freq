
import bottle
import traces.routes

@bottle.get('/ping')
def dummy():
  return 'Pong'


