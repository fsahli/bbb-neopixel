import os
import opc, time
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
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

@app.route('/update/<pixels_to_update>/<rgb>')
def update(pixels_to_update,rgb):
	global red, green, blue
	pixels_to_update = [int(x) for x in pixels_to_update.split(',')]
	rgb = [int(x) for x in rgb.split(',')]
	print pixels_to_update
	red = rgb[0]
	green = rgb[1]
	blue = rgb[2]
	np.update_pixels(pixels_to_update,rgb)
	print red, green, blue	
#	green = request.form['g'] 
#	blue = request.form['b'] 
#	print red, green, blue
    	return redirect(url_for('show_entries'))
if __name__ == '__main__':
    app.run(host='0.0.0.0')
