document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Get the input values
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Get the error message element
    const errorMessage = document.getElementById('error-message');

    // Check if the password and confirm password match
    if (password !== confirmPassword) {
        errorMessage.textContent = 'Passwords do not match';
        return;
    }

    // Simple email validation (for demonstration purposes)
    if (!validateEmail(email)) {
        errorMessage.textContent = 'Invalid email address';
        return;
    }

    // Check if the username is too short
    if (username.length < 3) {
        errorMessage.textContent = 'Username must be at least 3 characters long';
        return;
    }

    // Check if the password is too short
    if (password.length < 6) {
        errorMessage.textContent = 'Password must be at least 6 characters long';
        return;
    }

    // If validation passes, you can proceed with the form submission (e.g., send data to the server)
    // Here we simply log the data to the console
    console.log('Registration successful:', { email, username, password });
    errorMessage.textContent = 'Registration successful!'; // For demonstration purposes
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}
