from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_connection

app = Flask(__name__)
CORS(app)

# -------------------------
# CREATE TASK
# -------------------------
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    title = data.get("title")
    description = data.get("description", "")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO tasks (title, description, status) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, description, "pending"))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Task created"}), 201


# -------------------------
# GET ALL TASKS
# -------------------------
@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(tasks), 200


# -------------------------
# UPDATE TASK
# -------------------------
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    task = cursor.fetchone()

    if not task:
        cursor.close()
        conn.close()
        return jsonify({"error": "Task not found"}), 404

    title = data.get("title", task["title"])
    description = data.get("description", task["description"])
    status = data.get("status", task["status"])

    update_query = """
        UPDATE tasks
        SET title=%s, description=%s, status=%s
        WHERE id=%s
    """
    cursor.execute(update_query, (title, description, status, task_id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Task updated"}), 200


# -------------------------
# DELETE TASK
# -------------------------
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM tasks WHERE id = %s", (task_id,))
    task = cursor.fetchone()

    if not task:
        cursor.close()
        conn.close()
        return jsonify({"error": "Task not found"}), 404

    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Task deleted"}), 200


# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
