from flask import Flask, request, render_template
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# DB 초기화
def init_db():
    if not os.path.exists('attendance.db'):
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

@app.route('/attend')
def attend():
    name = request.args.get('name', '이름없음')
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("INSERT INTO attendance (name, timestamp) VALUES (?, ?)", (name, now))
    conn.commit()
    conn.close()

    return render_template("index.html", name=name, timestamp=now)

@app.route('/admin')
def admin():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("SELECT * FROM attendance")
    rows = c.fetchall()
    conn.close()

    html = "<h1>출석 명단</h1><ul>"
    for row in rows:
        html += f"<li>{row[1]} - {row[2]}</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)