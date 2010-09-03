# minus - a microframework in python

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

class View(object):
	def __init__(self):
		self.status = b'200 OK' # By default, everything is always right
		self.headers = [(b'Content-type', b'text/plain; charset=utf-8')]

	def do_GET(self):
		pass
	
	def do_POST(self):
		pass

class App(object):
	def __init__(self, routings):
		self.routings = routings

	def __call__(self, environ, start_response):
		if environ["PATH_INFO"] in self.routings:
			view = self.routings[environ["PATH_INFO"]]()

			if environ["REQUEST_METHOD"] == "GET":
				response = view.do_GET()
				start_response(view.status, view.headers)
				return response
		
def run(app):
	httpd = make_server('', 8000, app)
	print("Serving on http://localhost:8000")
	httpd.serve_forever()
