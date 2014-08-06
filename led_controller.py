import os
import opc, time
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from neopixel import Neopixel

np = Neopixel()

red = 0
green = 0
blue = 0

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def show_entries():
    global red, green, blue
    return render_template('layout.html',red=red,green=green,blue=blue,numLEDs=np.numLEDs )

@app.route('/update')
def update():
	global red, green, blue
	red = request.args.get('r', 0, type=int)
        green = request.args.get('g', 0, type=int)
        blue = request.args.get('b', 0, type=int)
        pixels_to_update = request.args.get('leds_to_update', 0, type=str)
	print red, green, blue	
	if pixels_to_update is not '':
		pixels_to_update = [int(x) for x in pixels_to_update.split(',')]
		print pixels_to_update
		np.update_pixels(pixels_to_update,[red,green,blue])
#	green = request.form['g'] 
#	blue = request.form['b'] 
#	print red, green, blue
    	return redirect(url_for('show_entries'))
if __name__ == '__main__':
    app.run(host='0.0.0.0')
