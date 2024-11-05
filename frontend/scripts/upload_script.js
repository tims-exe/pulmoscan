function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function() {
        var output = document.getElementById('preview');
        output.src = reader.result;
        output.style.display = 'block';
    }
    reader.readAsDataURL(event.target.files[0]);
}

async function uploadImage() {
    const form = document.getElementById('upload-form');
    const formData = new FormData(form);
    const fileInput = form.elements[0];
    const file = fileInput.files[0]; 

    if (file) {
        const reader = new FileReader();
        reader.onloadend = function() {
            localStorage.setItem('uploadedImage', reader.result); // Save image to localStorage
        };
        reader.readAsDataURL(file);
    }

    try {
        const response = await fetch('http://127.0.0.1:8000/model1/', {
            method: 'POST',
            body: formData,
        });
        console.log(response);
        if (response.ok) {
            const data = await response.json();
            //alert(`Prediction: ${data.prediction}`);
            localStorage.setItem("model2Prediction", JSON.stringify(data));
            window.location.href = 'results.html';
        } else {
            alert('Error uploading image.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during upload.');
    }
}