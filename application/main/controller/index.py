from application.main import *

from flask import render_template, jsonify, Response

import subprocess
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

# Returns raw du output as text
@main_blueprint.route("/du/raw")
def du_raw():
	path = '.' # By default from the root
	cmd = ['du', '-d', '1', '-h', path]

	print("COMMAND = ", " ".join(cmd))

	ret = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]

	return Response(ret, mimetype='text')


    # return render_template("du.html")

# @main_blueprint.route("/disk/")
# def disk():

    # Read disk usage .txt
    # disk_usage_reader("/Users/gerardwerk/Git/disk-space-visualiser/data")
    # result = {}
    # return "Hello!"
    # ret
    # urn jsonify(result)