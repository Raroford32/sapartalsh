import torch
from safetensors.torch import load_file
from model import SimpleModel

class DeepSpeedWrapper:
    # ... (previous code remains unchanged)

    def process(self, input_data):
        if self.model is None:
            raise RuntimeError("Model is not initialized. Please call initialize_model() first.")

        device = self.get_device()
        input_tensor = torch.tensor(input_data).float().to(device)
        
        with torch.no_grad():
            if self.use_deepspeed and self.engine is not None:
                output = self.engine(input_tensor)
            else:
                output = self.model(input_tensor)
        return output.cpu().tolist()

    # ... (rest of the code remains unchanged)
