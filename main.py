#!/usr/bin/env python
import os
import jinja2
import webapp2
import random


template_dir = os.path.join(os.path.dirname(__file__), "pages")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
	def get(self):
		self.render_template("main.html")


class LotoHandler(BaseHandler):
    def get(self):
        stevila = []

        random_stevilo1 = random.randint(1, 39)
        random_stevilo2 = random.randint(1, 39)
        random_stevilo3 = random.randint(1, 39)
        random_stevilo4 = random.randint(1, 39)
        random_stevilo5 = random.randint(1, 39)
        random_stevilo6 = random.randint(1, 39)
        random_stevilo7 = random.randint(1, 39)
        random_stevilo8 = random.randint(1, 39)
        stevila.append(random_stevilo1)
        stevila.append(random_stevilo2)
        stevila.append(random_stevilo3)
        stevila.append(random_stevilo4)
        stevila.append(random_stevilo5)
        stevila.append(random_stevilo6)
        stevila.append(random_stevilo7)
        stevila.append(random_stevilo8)

        params = {"stevila": stevila}

        self.render_template("loto.html", params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
	webapp2.Route('/loto', LotoHandler)
], debug=True)
