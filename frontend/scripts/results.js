function result_data() {

    const modelPred1 = JSON.parse(localStorage.getItem("model1Prediction"));
    const modelPred2 = JSON.parse(localStorage.getItem("model2Prediction"));
    const storedImage = localStorage.getItem('uploadedImage');
    const imageContainer = document.getElementById('img-container');

    if (storedImage) {
        const img = document.createElement('img');
        img.src = storedImage;
        imageContainer.appendChild(img);
    } else {
        imageContainer.innerHTML = 'No image found in localStorage.'; 
    }

    var pred = '';

    if (modelPred2.prediction == "Normal") {
        pred = "Model Prediction : Normal"
    }
    else{
        pred = "Model Prediction : Malignant"
    }

    document.getElementById("pred").textContent = pred;
}