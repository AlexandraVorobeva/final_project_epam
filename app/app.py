from flask import Flask, jsonify, abort, make_response, render_template
from flask_caching import Cache
import json
from .config import DIR
from .business_logic import *

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})

app = Flask(__name__)
cache.init_app(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/", methods=["GET"])
def hello():
    folder = group_folder_info(DIR)
    data = json.dumps({"folder": folder}, ensure_ascii=False)
    return render_template('index.html', data=data)


@app.route("/api/folder", methods=["GET"])
@cache.cached(timeout=30)
def get_folder_info():
    folder = group_folder_info(DIR)
    return json.dumps({"folder": folder}, ensure_ascii=False)


@app.route("/api/file/<string:file_name>", methods=["GET"])
@cache.cached(timeout=30)
def get_file_info(file_name):
    all_files = get_names_of_files(DIR)["names_of_files"]
    if file_name not in all_files:
        abort(404)
    path_to_file = get_path_for_filename(file_name)
    file = group_file_info(path_to_file)
    return json.dumps({"file": file}, ensure_ascii=False)


@app.route("/api/word/<string:word>", methods=["GET"])
@cache.cached(timeout=30)
def get_word_info(word):
    all_words = get_list_of_all_words(DIR)
    if word not in all_words:
        abort(404)
    word_info = group_word_info(word)
    data = jsonify({"word": word_info})
    return render_template('index.html', data=data)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error 404": "Not found"}), 404)


def main():
    app.run(host='0.0.0.0', port=4000)


if __name__ == '__main__':
    main()
