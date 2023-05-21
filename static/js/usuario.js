document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
      event.preventDefault();

      const nombre = document.getElementById('nombre').value;
      const apellido = document.getElementById('apellido').value;
      const fechaNacimiento = document.getElementById('fecha_nacimiento').value;
      const rol = document.getElementById('rol').value;
      const email = document.getElementById('email').value;
      const contrasena = document.getElementById('contrasena').value;
      const sexo = document.getElementById('sexo').value;
      const telefono = document.getElementById('telefono').value;

      if (nombre.trim() === '') {
        alert('Por favor, ingresa tu nombre.');
        return;
      }

      if (apellido.trim() === '') {
        alert('Por favor, ingresa tu apellido.');
        return;
      }

      if (fechaNacimiento.trim() === '') {
        alert('Por favor, ingresa tu fecha de nacimiento.');
        return;
      }

      if (rol.trim() === '') {
        alert('Por favor, ingresa tu rol.');
        return;
      }

      if (!validateEmail(email)) {
        alert('Por favor, ingresa un correo electrónico válido.');
        return;
      }

      if (contrasena.trim() === '') {
        alert('Por favor, ingresa tu contraseña.');
        return;
      }

      if (sexo.trim() === '') {
        alert('Por favor, selecciona tu sexo.');
        return;
      }

      if (!validatePhone(telefono)) {
        alert('Por favor, ingresa un número de teléfono válido.');
        return;
      }

      const usuario = {
        nombre: nombre,
        apellido: apellido,
        fechaNacimiento: fechaNacimiento,
        rol: rol,
        email: email,
        contrasena: contrasena,
        sexo: sexo,
        telefono: telefono
      };

      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/");
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
          alert("El usuario se registró exitosamente.");
          form.reset();  // Reset the form only after successful registration.
        } else {
          alert("Hubo un error en el registro de usuario.");
        }
      };
      xhr.send(JSON.stringify(usuario));
    });

    function validateEmail(email) {
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(String(email).toLowerCase());
    }

    function validatePhone(phone) {
      var re = /^\d{9}$/;
      return re.test(String(phone));
    }
});