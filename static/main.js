document.addEventListener('DOMContentLoaded', function () {
    const loginButton = document.getElementById('loginButton');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');

    loginButton.addEventListener('click', function () {
        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        if (email === '' || password === '') {
            alert('Please fill in all fields.');
        } else {
            // Here, you can add code to send the login data to the server for authentication.
            // For this example, we'll just display a success message.
            alert('Login successful!');
        }
    });
});
