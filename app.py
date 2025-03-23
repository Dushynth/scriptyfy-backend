from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/generate-script', methods=['POST'])
def generate_script():
    try:
        data = request.get_json()
        print("Received data:", data)

        # Placeholder script generation
        input1 = data.get('input1', '')
        input2 = data.get('input2', '')
        generated_script = f"Script generated using: {input1} and {input2}"

        return jsonify({"script": generated_script}), 200

    except Exception as e:
        print("Error generating script:", e)
        return jsonify({"error": "Failed to generate script"}), 500

if __name__ == '__main__':
    app.run(debug=True)


