from application.main import *
from flask import render_template, jsonify

# class DiskUsageParserError(Exception):
#     pass
#
# def disk_usage_reader(file_path):
#
#     try:
#         with open(file_path) as fp:
#             for line in fp:
#                 print(line)
#
#     except FileNotFoundError:
#         print("Disk file does not exist")

    


@main_blueprint.route("/")
def index():
    return render_template("index.html")

# @main_blueprint.route("/disk/")
# def disk():

    # Read disk usage .txt
    # disk_usage_reader("/Users/gerardwerk/Git/disk-space-visualiser/data")
    # result = {}
    # return "Hello!"
    # ret
    # urn jsonify(result)