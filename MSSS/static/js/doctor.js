//Doctors form
document.addEventListener("DOMContentLoaded", function () {
	// Function to handle form submission
function handleFormSubmit(event) {
	event.preventDefault(); // Prevent the default form submission
	        
// Get form data
const form = event.target;
	const formData = new FormData(form);

// Send a POST request to the server to save the doctor data
fetch('/path/to/save/doctor/data/', {
	method: 'POST',
	body: formData,
})
	.then(response => {
		if (response.ok) {
			console.log('Doctor data saved successfully');
// Optionally, redirect to another page after successful submission
window.location.href = '/path/to/success/page/';
		} else {
			console.error('Error saving doctor data:', response.statusText);
// Optionally, display an error message to the user
}
})
	.catch(error => {
		console.error('Error saving doctor data:', error);
// Optionally, display an error message to the user
});
}

// Add form submission event listener
const form = document.querySelector('#doctor-form');
    form.addEventListener('submit', handleFormSubmit);
});
