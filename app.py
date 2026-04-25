from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import logging
import time

app = Flask(__name__)

DB_NAME = "students.db"

# ✅ Logging setup
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def log_info(msg):
    logging.info(msg)

def log_error(msg):
    logging.error(msg)

# ✅ Initialize DB
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        """)
        conn.commit()

# ✅ DB connection
def get_db():
    return sqlite3.connect(DB_NAME)

# ✅ Health check endpoint (for monitoring)
@app.route('/health')
def health():
    try:
        start = time.time()
        with get_db() as conn:
            conn.execute("SELECT 1")
        latency = round((time.time() - start) * 1000, 2)

        return jsonify({
            "status": "UP",
            "db": "connected",
            "latency_ms": latency
        }), 200

    except Exception as e:
        log_error(f"Health check failed: {e}")
        return jsonify({
            "status": "DOWN",
            "error": str(e)
        }), 500

@app.route('/')
def index():
    log_info("Accessed home page")
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        try:
            name = request.form['name']
            age = request.form['age']

            with get_db() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO students (name, age) VALUES (?, ?)",
                    (name, age)
                )
                conn.commit()

            log_info(f"Student added: {name}, {age}")
            return redirect('/students')

        except Exception as e:
            log_error(f"Error adding student: {e}")
            return "Internal Server Error", 500

    return render_template('add_student.html')

@app.route('/students')
def students():
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            data = cursor.fetchall()

        log_info("Fetched student list")
        return render_template('students.html', students=data)

    except Exception as e:
        log_error(f"Error fetching students: {e}")
        return "Internal Server Error", 500

# ✅ Simulate failure endpoint (for testing)
@app.route('/fail')
def fail():
    log_error("Simulated failure triggered")
    raise Exception("Simulated crash!")

if __name__ == '__main__':
    init_db()
    log_info("Application started")
    app.run(debug=True)