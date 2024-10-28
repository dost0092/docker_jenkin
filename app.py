import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

# Configuration for the PostgreSQL database connection
DB_CONFIG = {
    'host': 'host.docker.internal',
    'database': 'Zones',
    'user': 'postgres',
    'password': 'dost'
}

def connect_pdb():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

# Home endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the City API"}), 200

# Endpoint to get a paginated list of cities
@app.route("/cities", methods=["GET"])
def get_all_cities():
    page = request.args.get("page", default=1, type=int)
    limit = request.args.get("limit", default=10, type=int)
    offset = (page - 1) * limit

    conn = connect_pdb()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM cities_data;")
        total_cities = cursor.fetchone()[0]
        total_pages = (total_cities + limit - 1) // limit

        cursor.execute("SELECT id, name FROM cities_data LIMIT %s OFFSET %s;", (limit, offset))
        cities = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        return jsonify({
            "page": page,
            "limit": limit,
            "total_pages": total_pages,
            "total_cities": total_cities,
            "cities": cities
        })

    except Exception as e:
        print(f"Database query error: {e}")
        return jsonify({"error": "Database query failed"}), 500




# Endpoint to get cities modified after a specific date
@app.route("/cities_modified_after", methods=["GET"])
def get_cities_modified_after():
    date = request.args.get("date")
    page = request.args.get("page", default=1, type=int)
    limit = request.args.get("limit", default=10, type=int)
    offset = (page - 1) * limit

    conn = connect_pdb()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM cities_data WHERE date_modified > %s;", (date,))
        total_cities = cursor.fetchone()[0]
        total_pages = (total_cities + limit - 1) // limit

        cursor.execute(
            "SELECT id, name FROM cities_data WHERE date_modified > %s LIMIT %s OFFSET %s;",
            (date, limit, offset)
        )
        cities = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        return jsonify({
            "page": page,
            "limit": limit,
            "total_pages": total_pages,
            "total_cities": total_cities,
            "cities": cities
        })

    except Exception as e:
        print(f"Database query error: {e}")
        return jsonify({"error": "Database query failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)
