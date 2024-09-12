from flask import Flask, request, jsonify, render_template
from model_loader import lazy_load_model_parts, inference, unload_model_parts
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variable to store the loaded model parts
model_parts = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/load_model", methods=["POST"])
def load_model():
    global model_parts
    try:
        model_paths = request.json.get("model_paths", [])
        if not model_paths:
            return jsonify({"error": "No model paths provided"}), 400

        # Unload previous model parts if they exist
        if model_parts:
            unload_model_parts(model_parts)

        model_parts = lazy_load_model_parts(model_paths)
        return jsonify({"message": "Model loaded successfully"}), 200
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        return jsonify({"error": f"Failed to load model: {str(e)}"}), 500

@app.route("/inference", methods=["POST"])
def perform_inference():
    global model_parts
    try:
        if model_parts is None:
            return jsonify({"error": "Model not loaded"}), 400

        input_data = request.json.get("input_data")
        if input_data is None:
            return jsonify({"error": "No input data provided"}), 400

        result = inference(model_parts, input_data)
        return jsonify({"result": result}), 200
    except Exception as e:
        logger.error(f"Error during inference: {str(e)}")
        return jsonify({"error": f"Inference failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
