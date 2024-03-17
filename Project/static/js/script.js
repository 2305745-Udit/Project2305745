function toggleFanLight(id) {
    fetch('/toggle_fan_light/' + id, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            console.log('Toggle successful');
            // Update UI as needed
        } else {
            console.error('Toggle failed');
            // Handle error
        }
    })
    .catch(error => console.error('Error:', error));
}