
import bottle
import service

app = bottle.default_app()
app.get('/traces', callback=service.get_all)
app.get('/traces/<id:int>', callback=service.get)
app.post('/traces', callback=service.new)
