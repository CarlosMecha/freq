
import bottle
import routes

@bottle.route('/ping')
def dummy():
  """
  Do nothing.
  """
  return 'Pong'

bottle.run(host='localhost', port=8686)
