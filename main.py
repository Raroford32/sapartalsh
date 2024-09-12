from flask import Flask, render_template, jsonify, request
from deepspeed_utils import DeepSpeedWrapper

app = Flask(__name__)

# Initialize DeepSpeed wrapper
try:
    ds_wrapper = DeepSpeedWrapper()
except Exception as e:
    print(f"Error initializing DeepSpeedWrapper: {e}")
    ds_wrapper = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if ds_wrapper is None:
        return jsonify({"error": "DeepSpeed wrapper is not initialized."}), 500

    input_data = request.json.get("input_data")
    if not input_data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        # Process input data using DeepSpeed
        result = ds_wrapper.process(input_data)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/gpu_info")
def gpu_info():
    if ds_wrapper is None:
        return jsonify({"error": "DeepSpeed wrapper is not initialized."}), 500
    return jsonify(ds_wrapper.get_gpu_info())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Note: This implementation is designed for deployment in multi-GPU environments.
# It may not fully utilize GPU capabilities in the current Replit environment due to lack of GPU support.
# The multi-GPU functionality should be thoroughly tested in the target deployment environment.
