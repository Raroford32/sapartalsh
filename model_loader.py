import safetensors
import numpy as np

def load_model_parts(model_paths):
    """
    Load multiple .safetensor model parts and combine them into a single model.
    """
    model_parts = []
    for path in model_paths:
        with safetensors.safe_open(path, framework="pt", device="cpu") as f:
            model_parts.append(f.get_tensor("model"))
    
    # Combine model parts (this is a simplified example, adjust based on your specific model architecture)
    combined_model = np.concatenate(model_parts, axis=0)
    return combined_model

def inference(model, input_data):
    """
    Perform inference using the loaded model and input data.
    This is a placeholder function - replace with actual inference logic for your model.
    """
    # Convert input_data to appropriate format (e.g., numpy array)
    input_array = np.array(input_data)
    
    # Perform inference (this is a simplified example, replace with actual inference logic)
    result = np.dot(model, input_array)
    
    return result.tolist()
