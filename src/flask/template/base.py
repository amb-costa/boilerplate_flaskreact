# Using 4Geeks' React + Flask API boilerplate code here
# utils.py contains basic code to render basic HTML if the env successfully develops
# https://github.com/4GeeksAcademy/react-flask-hello/blob/main/src/api/utils.py

from flask import jsonify, url_for

class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def generate_sitemap(app):
    links = ["/admin/"]
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if "/admin/" not in url:
                links.append(url)

    links_html = "".join(["<li><a href='" + y + "'>" + y + "</a></li>" for y in links])
    return """
        <div style="text-align: center;">
        <h1>Flask is working!</h1>
        <h3>This is basic HTML to show Flask is running on sitemap mode</h3>
        <h3>This only appears on ENV mode</h3>
        <h3>You already got these endpoints:</h3>
        <ul style="text-align: center;">"""+links_html+"</ul><h3>Make sure to add more endpoints on the app.py file</h3></div>"
    
     