from application.main import *

from du.DiskUsageParser import parse_du
from du.Tree import NodeEncoder

import json

from flask import render_template, jsonify, Response

import subprocess

@main_blueprint.route("/")
def index():
    return render_template("index.html")

def du_cmd():
    path = '.' # By default from the root
    cmd = ['du', '-d', '1', '-h', path]

    return subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0].decode('ascii')

# Returns raw du output as text
@main_blueprint.route("/du/raw")
def du_raw():
	return Response(du_cmd(), mimetype='text')

@main_blueprint.route("/du/json")
def du_json():
    du_output = du_cmd()

    # Parse to tree structure
    du_tree = parse_du(du_output)

    # Dump to JSON using the custom NodeEncoder
    du_json = json.dumps(du_tree, cls=NodeEncoder, indent=4)
    # du_json = ''
    return Response(du_json, mimetype='text/json')

    # return render_template("du.html")

# @main_blueprint.route("/disk/")
# def disk():

    # Read disk usage .txt
    # disk_usage_reader("/Users/gerardwerk/Git/disk-space-visualiser/data")
    # result = {}
    # return "Hello!"
    # ret
    # urn jsonify(result)