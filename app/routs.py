from flask import Flask, jsonify
from flask_restful import Resource
import json
from .config import *
from .business_logic import *


ALL_WORDS = get_list_of_all_words(DIR)


class Folder(Resource):
    @cache.cached(timeout=30)
    def get(self):
        """
        GET information about home directory.
        Get analysis of home directory.
        ---
        responses:
         200:
           description: ok (in case of success)
        """
        folder = group_folder_info(DIR)
        return jsonify({"folder": folder})


class File(Resource):
    def get(self, file_name):
        """
        GET information about a file.
        Get analysis of a file from home directory
        ---
        parameters:
         - in: path
           name: file_name
           type: string
           required: true
        responses:
         200:
           description: ok (in case of success)
        """
        all_files = get_names_of_files(DIR)["names_of_files"]
        if file_name not in all_files:
            return {"error 404": "Not found"}, 404
        path_to_file = get_path_for_filename(file_name)
        file = group_file_info(path_to_file)
        return jsonify({"file": file})


class Word(Resource):
    @cache.cached(timeout=30)
    def get(self, word):
        """
        GET information about a word.
        Get phonetic analysis of a word from home directory
        ---
        parameters:
         - in: path
           name: word
           type: string
           required: true
        responses:
         200:
           description: ok (in case of success)
        """
        if word not in ALL_WORDS:
            return {"error 404": "Not found"}, 404
        word_info = group_word_info(word)
        return jsonify({"word": word_info})

    def post(self, word):
        """
        POST new word.
        Add new word in list of word in home directory
        ---
        parameters:
         - in: path
           name: word
           type: string
           required: true
        responses:
         201:
           description: created (in case of success)
        """
        word_info = group_word_info(word)
        ALL_WORDS.append(word)
        return json.dumps({"word": word_info}, ensure_ascii=False), 201

    def delete(self, word):
        """
        DELETE a word
        Delete a word from list of all word.
        ---
        parameters:
         - in: path
           name: word
           type: string
           required: true
        responses:
         200:
           description: ok (in case of success)
        """
        if word not in ALL_WORDS:
            return {"error 404": "Not found"}, 404
        ALL_WORDS.remove(word)
        return jsonify({"result": True})


api.add_resource(Folder, "/api/folder")
api.add_resource(File, "/api/file/<string:file_name>")
api.add_resource(Word, "/api/word/<string:word>", "/api/word/<string:word>", "/api/word/<string:word>")
