// get method
function fetchData(){
    const apiURL = 'http://127.0.0.1:8000/data/'

    fetch(apiURL)
        .then(response => {
            if (!response.ok){
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const dataContainer = document.querySelector('.data');
            dataContainer.innerHTML = `<p>Name : ${data.name}<br>Roll No : ${data.roll_no}`
        })
        .catch(error => {
            console.error('Problem with fetching data : ', error);
        });
}

// post method
function submitButton(){
    //console.log(document.querySelector('.text-input').value);
    const apiURL = 'http://127.0.0.1:8000/input/'

    const textInputValue = document.querySelector('.text-input').value;

    const data = {
        'text': textInputValue 
    }

    fetch(apiURL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(data => {
        const dataContainer = document.querySelector('.input-result');
        dataContainer.innerHTML = `<p>${data.pswd}</p>`
    })
    .catch(error => {
        console.error('Error:', error);
    });

}

// call fetch function when page loads

window.onload = fetchData

