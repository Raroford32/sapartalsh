document.addEventListener('DOMContentLoaded', () => {
    const loadModelForm = document.getElementById('loadModelForm');
    const inferenceForm = document.getElementById('inferenceForm');
    const resultDiv = document.getElementById('result');

    loadModelForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const modelPaths = document.getElementById('modelPaths').value.split(',').map(path => path.trim());
        
        try {
            const response = await fetch('/load_model', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ model_paths: modelPaths }),
            });
            
            const data = await response.json();
            
            if (response.ok) {
                resultDiv.textContent = data.message;
            } else {
                resultDiv.textContent = `Error: ${data.error}`;
            }
        } catch (error) {
            resultDiv.textContent = `Error: ${error.message}`;
        }
    });

    inferenceForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const inputData = document.getElementById('inputData').value.split(',').map(Number);
        
        try {
            const response = await fetch('/inference', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ input_data: inputData }),
            });
            
            const data = await response.json();
            
            if (response.ok) {
                resultDiv.textContent = `Inference result: ${JSON.stringify(data.result)}`;
            } else {
                resultDiv.textContent = `Error: ${data.error}`;
            }
        } catch (error) {
            resultDiv.textContent = `Error: ${error.message}`;
        }
    });
});
