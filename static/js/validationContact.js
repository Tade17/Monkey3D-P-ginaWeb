document.addEventListener('DOMContentLoaded', function () {
    function showNotification(message, type = 'success') {
        const container = document.getElementById('notification-container');
        const notification = document.createElement('div');
        notification.className = `mb-4 p-4 rounded-lg shadow-lg transform transition-all duration-300 translate-x-full`;

        if (type === 'success') {
            notification.classList.add('bg-green-500', 'text-white');
        } else if (type === 'error') {
            notification.classList.add('bg-red-500', 'text-white');
        }

        notification.textContent = message;
        container.appendChild(notification);

        setTimeout(() => {
            notification.classList.remove('translate-x-full');
        }, 100);

        setTimeout(() => {
            notification.classList.add('translate-x-full', 'opacity-0');
            setTimeout(() => {
                container.removeChild(notification);
            }, 300);
        }, 5000);
    }

    // Función para validar email
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Función para mostrar error
    function setError(input, message) {
        // Limpiar error previo si existe
        clearError(input);

        const errorElement = document.createElement('p');
        errorElement.classList.add('text-red-500', 'text-sm', 'mt-1');
        errorElement.textContent = message;
        errorElement.id = `${input.id}-error`;

        input.classList.add('border-red-500');
        input.parentNode.appendChild(errorElement);
    }

    // Función para limpiar error
    function clearError(input) {
        const existingError = document.getElementById(`${input.id}-error`);
        if (existingError) {
            existingError.remove();
        }
        input.classList.remove('border-red-500');
    }

    // Función para limpiar todos los errores
    function clearAllErrors() {
        const inputs = [nameInput, emailInput, messageInput];
        inputs.forEach(input => clearError(input));
    }

    // Obtener elementos del formulario
    const form = document.getElementById('contactForm');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const messageInput = document.getElementById('message');

    // Validación en tiempo real
    const inputs = [nameInput, emailInput, messageInput];
    inputs.forEach(input => {
        input.addEventListener('input', () => {
            clearError(input);
        });
    });

    // Manejar envío del formulario
    form.addEventListener('submit', async function (event) {
        event.preventDefault();
        clearAllErrors();

        let isValid = true;

        // Validar nombre
        if (nameInput.value.trim() === '') {
            setError(nameInput, 'Su nombre es obligatorio pa');
            isValid = false;
        } else if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(nameInput.value.trim())) {
            setError(nameInput, 'El nombre solo puede contener letras y espacios');
            isValid = false;
        }

        // Validar email
        if (emailInput.value.trim() === '') {
            setError(emailInput, 'El email es obligatorio pa');
            isValid = false;
        } else if (!isValidEmail(emailInput.value.trim())) {
            setError(emailInput, 'El correo no es válido');
            isValid = false;
        }

        // Validar mensaje
        if (messageInput.value.trim() === '') {
            setError(messageInput, 'El mensaje es obligatorio pa');
            isValid = false;
        }

        if (isValid) {
            try {
                // Aquí iría tu llamada al backend
                const response = await simulateApiCall({
                    name: nameInput.value.trim(),
                    email: emailInput.value.trim(),
                    message: messageInput.value.trim()
                });

                if (response.success) {
                    showNotification('¡Mensaje enviado con éxito!', 'success');
                    form.reset();
                } else {
                    showNotification('Error al enviar el mensaje. Por favor, intente nuevamente.', 'error');
                }
            } catch (error) {
                showNotification('Error de conexión. Por favor, verifique su conexión a internet.', 'error');
            }
        }
    });

    // Simulación de llamada al backend (reemplazar con tu llamada real)
    function simulateApiCall(data) {
        return new Promise((resolve) => {
            setTimeout(() => {
                const success = Math.random() < 0.9;
                resolve({ success });
            }, 1000);
        });
    }
});