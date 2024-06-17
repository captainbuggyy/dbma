document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Predefined username and password
    const correctUsername = 'farmer';
    const correctPassword = 'password123';

    // Get the input values
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Get the error message element
    const errorMessage = document.getElementById('error-message');

    // Check if the username and password are correct
    if (username === correctUsername && password === correctPassword) {
        // Redirect to the home page or perform successful login actions
        window.location.href = '/home';
    } else {
        // Show the error message
        errorMessage.textContent = 'Wrong username or password';
    }
});
