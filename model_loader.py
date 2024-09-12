import safetensors
import numpy as np
import mmap
import os

def memory_map_file(file_path):
    with open(file_path, 'rb') as f:
        return mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

def lazy_load_model_parts(model_paths):
    """
    Lazy load multiple .safetensor model parts using memory mapping.
    """
    model_parts = []
    for path in model_paths:
        mapped_file = memory_map_file(path)
        model_parts.append(safetensors.safe_open(mapped_file, framework="pt", device="cpu"))
    return model_parts

def get_model_part(model_parts, part_index, tensor_name="model"):
    """
    Get a specific part of the model on demand.
    """
    return model_parts[part_index].get_tensor(tensor_name)

def inference(model_parts, input_data):
    """
    Perform inference using the lazy-loaded model parts and input data.
    This is a placeholder function - replace with actual inference logic for your model.
    """
    # Convert input_data to appropriate format (e.g., numpy array)
    input_array = np.array(input_data)
    
    # Perform inference (this is a simplified example, replace with actual inference logic)
    result = np.zeros_like(input_array)
    for part in model_parts:
        model_tensor = part.get_tensor("model")
        result += np.dot(model_tensor, input_array)
    
    return result.tolist()

def unload_model_parts(model_parts):
    """
    Unload model parts and free up memory.
    """
    for part in model_parts:
        part.unload()
