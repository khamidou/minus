from minus import *

class minusApp(View):
	def do_GET(self):
		return "OH HAI"

routes = {"/" : minusApp} 
app = App(routes)
run(app)
