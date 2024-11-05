document.getElementById("symptomForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    // Collect form data
    const age = document.getElementById("age").value;
    const gender = document.getElementById("gender").value;

    // Collect selected symptoms and map to required values
    const symptoms = {
        GENDER: parseInt(gender === "male" ? 1 : 0),
        AGE: parseInt(age),
        SMOKING: document.getElementById("smoking").checked ? 1 : 0,
        YELLOW_FINGERS: document.getElementById("yellow_fingers").checked ? 2 : 0,
        ANXIETY: document.getElementById("anxiety").checked ? 2 : 0,
        PEER_PRESSURE: document.getElementById("peer_pressure").checked ? 1 : 0,
        CHRONIC_DISEASE: document.getElementById("chronic_disease").checked ? 1 : 0,
        FATIGUE: document.getElementById("fatigue").checked ? 2 : 0,
        ALLERGY: document.getElementById("allergy").checked ? 1 : 0,
        WHEEZING: document.getElementById("wheezing").checked ? 2 : 0,
        ALCOHOL_CONSUMING: document.getElementById("alcohol_consuming").checked ? 2 : 0,
        COUGHING: document.getElementById("coughing").checked ? 2 : 0,
        SHORTNESS_OF_BREATH: document.getElementById("shortness_of_breath").checked ? 2 : 0,
        SWALLOWING_DIFFICULTY: document.getElementById("swallowing_difficulty").checked ? 2 : 0,
        CHEST_PAIN: document.getElementById("chest_pain").checked ? 2 : 0,
    };

    
    fetch("http://127.0.0.1:8000/model2/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(symptoms)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok " + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        //alert("Prediction Result: " + data.prediction);
        localStorage.setItem("model1Prediction", JSON.stringify(data))
        console.log(data)
        window.location.href = 'upload.html'
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred: " + error.message);
    });
});


function clear_storage() {
    localStorage.clear();
    console.log('local storage cleared')
}