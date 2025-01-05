document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const passwordConfirmationInput = document.getElementById('password_confirmation');

    form.addEventListener('submit', function (event) {
        let isValid = true;

        // Limpiar errores previos
        clearErrors();

        // Validar nombre (no vacío y solo letras y espacios)
        if (nameInput.value.trim() === '') {
            setError(nameInput, 'El nombre es obligatorio.');
            isValid = false;
        } else if (!/^[a-zA-Z\s]+$/.test(nameInput.value)) {
            setError(nameInput, 'El nombre solo puede contener letras y espacios.');
            isValid = false;
        }

        // Validar correo electrónico (formato válido)
        if (emailInput.value.trim() === '') {
            setError(emailInput, 'El correo electrónico es obligatorio.');
            isValid = false;
        } else if (!isValidEmail(emailInput.value)) {
            setError(emailInput, 'El correo electrónico no es válido.');
            isValid = false;
        }

        // Validar contraseña (longitud mínima, al menos una mayúscula, un número y un carácter especial)
        if (passwordInput.value.trim() === '') {
            setError(passwordInput, 'La contraseña es obligatoria.');
            isValid = false;
        } else if (passwordInput.value.length < 8) {
            setError(passwordInput, 'La contraseña debe tener al menos 8 caracteres.');
            isValid = false;
        } else if (!/(?=.*[A-Z])/.test(passwordInput.value)) {
            setError(passwordInput, 'La contraseña debe tener al menos una letra mayúscula.');
            isValid = false;
        } else if (!/(?=.*\d)/.test(passwordInput.value)) {
            setError(passwordInput, 'La contraseña debe tener al menos un número.');
            isValid = false;
        } 

        // Validar coincidencia de contraseñas
        if (passwordConfirmationInput.value.trim() === '') {
            setError(passwordConfirmationInput, 'La confirmación de contraseña es obligatoria.');
            isValid = false;
        } else if (passwordInput.value !== passwordConfirmationInput.value) {
            setError(passwordConfirmationInput, 'Las contraseñas no coinciden.');
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault();
        }
    });

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    function setError(input, message) {
        const errorElement = document.createElement('p');
        errorElement.classList.add('text-red-500', 'text-sm', 'mt-1');
        errorElement.textContent = message;

        // Agregar un identificador único al mensaje de error basado en el id del input
        errorElement.id = input.id + "-error";

        input.classList.add('border-red-500');
        input.parentNode.insertBefore(errorElement, input.nextSibling);

    }
    function clearErrors(){
        const errorElements = document.querySelectorAll('.text-red-500');
        errorElements.forEach(error => error.remove());
        nameInput.classList.remove('border-red-500');
        emailInput.classList.remove('border-red-500');
        passwordInput.classList.remove('border-red-500');
        passwordConfirmationInput.classList.remove('border-red-500');
    }
});