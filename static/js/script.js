document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('inputForm');
    const resultDiv = document.getElementById('result');
    const gpuInfoDiv = document.getElementById('gpuInfo');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const inputData = document.getElementById('inputData').value;
        
        // Convert input string to array of numbers
        const inputArray = inputData.split(',').map(num => parseFloat(num.trim()));

        fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({input_data: inputArray}),
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<h3>Result:</h3><p>${JSON.stringify(data.result)}</p>`;
        })
        .catch((error) => {
            console.error('Error:', error);
            resultDiv.innerHTML = `<h3>Error:</h3><p>${error}</p>`;
        });
    });

    // Fetch GPU info on page load
    fetch('/gpu_info')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                gpuInfoDiv.innerHTML = `<h3>GPU Info:</h3><p>${data.error}</p>`;
            } else {
                gpuInfoDiv.innerHTML = `
                    <h3>GPU Info:</h3>
                    <p>GPU Count: ${data.gpu_count}</p>
                    <p>Current Device: ${data.current_device}</p>
                    <p>Device Name: ${data.device_name}</p>
                `;
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            gpuInfoDiv.innerHTML = `<h3>Error:</h3><p>${error}</p>`;
        });
});
