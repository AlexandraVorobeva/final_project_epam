from flask import Flask
from flask_restful import Api
from flask_caching import Cache
from flasgger import Swagger


app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

cache = Cache(config={"CACHE_TYPE": "SimpleCache"})
cache.init_app(app)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True



DIR = "/Users/aleksandravorobeva/Desktop/litr"
