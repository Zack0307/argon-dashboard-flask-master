# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from malware_file_execute import *
import torch
# import torch.nn as nn

device =  torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = VGG(num_classes = 2)
model.load_state_dict(torch.load('C:\Users\digital\Desktop\malware\malware_analysis1.pt', map_location = device))
model.eval()
npy_path = "C:\Users\digital\Desktop\malware\npy_output"
@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index')

@blueprint.route('/virus-upload', methods=['GET'])
def virus_upload():
    return render_template('home/virus_upload.html')

@blueprint.route('/virus-detect', methods=['POST'])
def virus_detect():
    #讀取檔案
    detect_file = read_file("接收要偵測的文件")
    #轉換markov
    markov_file = file_to_hex(detect_file)
    #markov轉換成npy
    npy_file = markov_to_npy(markov_file)
    #讀取npy檔
    datasets, cnt = load_markov_matrices2(npy_path)


    pass


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
