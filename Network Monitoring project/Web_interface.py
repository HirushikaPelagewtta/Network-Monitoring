from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_devices():
    conn = sqlite3.connect('devices.db')
    c = conn.cursor()
    c.execute("SELECT * FROM devices")
    devices = c.fetchall()
    conn.close()
    return devices

def get_up_device_count():
    conn = sqlite3.connect('devices.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM devices WHERE status='up'")
    up_count = c.fetchone()[0]
    conn.close()
    return up_count

@app.route('/')
def index():
    devices = get_devices()
    up_count = get_up_device_count()
    return render_template('index.html', devices=devices, up_count=up_count)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
