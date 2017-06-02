from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from .. import site_blueprint

@site_blueprint.route('/')
def index():
	return render_template('home.html')
