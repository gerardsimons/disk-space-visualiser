from application.main import *

from du.DiskUsageParser import parse_du
from du.Tree import NodeEncoder

import json

from flask import render_template, jsonify, Response, request

import subprocess

@main_blueprint.route("/")
def index():
    return render_template("index.html")

def du_cmd(depth=1, path='.'):
    cmd = ['du', '-d', str(depth), path]
    print("Executing disk usage command : '{}'".format(" ".join(cmd)))
    return subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0].decode('ascii')

# Returns raw du output as text
@main_blueprint.route("/du/raw")
def du_raw():
	return Response(du_cmd(), mimetype='text')

@main_blueprint.route("/du/json")
def du_json():
    depth = request.args.get('depth')
    if depth is None:
        print("JSON -- NO DEPTH FOUND")
        depth = 1

    path = request.args.get('path')
    if path is None:
        print("JSON -- NO PATH FOUND")
        path = '.' # By default from the current dir
        
    du_output = du_cmd(depth=depth, path=path)

    # Parse to tree structure
    du_tree = parse_du(du_output)

    # Dump to JSON using the custom NodeEncoder
    du_json = json.dumps(du_tree, cls=NodeEncoder, indent=4)
    
    return Response(du_json, mimetype='text/json')

@main_blueprint.route("/du/tree-map")
def du_tree_map():
    depth = request.args.get('depth')
    if depth is None:
        depth = 1

    path = request.args.get('path')
    if path is None:
        path = '.' # By default from the current dir

    print("path={}".format(path))
    print("depth={}".format(depth))

    return render_template("treemap.html", depth=depth, path=path)

@main_blueprint.route("/treemap_example")
def example_treemap():
    return render_template("treemap_example.html")

# @main_blueprint.route("/disk/")
# def disk():

    # Read disk usage .txt
    # disk_usage_reader("/Users/gerardwerk/Git/disk-space-visualiser/data")
    # result = {}
    # return "Hello!"
    # ret
    # urn jsonify(result)