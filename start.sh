#!/bin/bash

export FLASK_APP=app.py
export FLASK_ENV=development

pip install flask flask_cors flask_restful

flask run
