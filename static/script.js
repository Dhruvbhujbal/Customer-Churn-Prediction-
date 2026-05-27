document.getElementById('churn-form').addEventListener('submit', function(e) {
    e.preventDefault();

    // UI Elements
    const submitBtn = document.getElementById('submit-btn');
    const btnText = document.getElementById('btn-text');
    const btnSpinner = document.getElementById('btn-spinner');
    const resultBox = document.getElementById('result-box');
    const gaugeFill = document.getElementById('gauge-fill');
    const gaugeText = document.getElementById('gauge-text');
    
    // 1. Trigger Loading State
    submitBtn.disabled = true;
    btnText.innerText = "Analyzing Risk...";
    btnSpinner.classList.remove('hidden');
    resultBox.classList.add('hidden'); 

    // Reset gauge for cool re-animation
    gaugeFill.style.width = '0%';
    gaugeText.innerText = '0%';

    // 2. Gather data
    const data = {
        tenure: document.getElementById('tenure').value,
        monthly_charges: document.getElementById('monthly_charges').value,
        contract: document.getElementById('contract').value,
        internet_service: document.getElementById('internet_service').value,
        payment_method: document.getElementById('payment_method').value
    };

    // 3. Send to Flask Backend 
    setTimeout(() => {
        fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            // Restore Button
            submitBtn.disabled = false;
            btnText.innerText = "Run Prediction Engine";
            btnSpinner.classList.add('hidden');

            // Display Results
            const resultTitle = document.getElementById('result-title');
            const resultText = document.getElementById('result-text');

            resultBox.classList.remove('hidden');
            
            // Animate the gauge
            gaugeText.innerText = `${data.probability}%`;
            
            // Delay slightly so CSS animation triggers properly
            setTimeout(() => {
                gaugeFill.style.width = `${data.probability}%`;
            }, 50);

            // Set Text and Colors
            if (data.churn_risk === 1) {
                resultBox.className = "danger";
                resultTitle.innerHTML = "<i class='fa-solid fa-fire'></i> HIGH FLIGHT RISK";
                resultText.innerText = "This account requires immediate intervention.";
            } else {
                resultBox.className = "safe";
                resultTitle.innerHTML = "<i class='fa-solid fa-shield'></i> SAFE ACCOUNT";
                resultText.innerText = "This customer shows high loyalty indicators.";
            }
        })
        .catch(error => {
            console.error('Error:', error);
            submitBtn.disabled = false;
            btnText.innerText = "Run Prediction Engine";
            btnSpinner.classList.add('hidden');
            alert("Error connecting to the AI model.");
        });
    }, 800); // 800ms artificial delay for the loading animation
});