# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index')


@blueprint.route('/contacts')
@login_required
def contacts():
    return render_template('home/contacts.html', segment='contacts')


@blueprint.route('/tasks')
@login_required
def tasks():
    return render_template('home/tasks.html', segment='tasks')


@blueprint.route('/opportunities')
@login_required
def opportunities():
    return render_template('home/opportunities.html', segment='opportunities')


@blueprint.route('/reports')
@login_required
def reports():
    return render_template('home/reports.html', segment='reports')


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
