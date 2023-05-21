// Obtener referencia al formulario
const formularioUsuario = document.querySelector('form');

// Agregar el evento de envío al formulario
formularioUsuario.addEventListener('submit', handlingSubmit);

function handlingSubmit(e) {
  e.preventDefault();

  // Obtener los valores del formulario
  const nombreInput = document.querySelector('#nombre');
  const apellidoInput = document.querySelector('#apellido');
  const rolInput = document.querySelector('#rol');
  const contrasenaInput = document.querySelector('#contrasena');
  const sexoInput = document.querySelector('#sexo');
  const fechaNacimientoInput = document.querySelector('#fecha_nacimiento');
  const telefonoInput = document.querySelector('#telefono');
  const emailInput = document.querySelector('#email');

  const nombre = nombreInput.value;
  const apellido = apellidoInput.value;
  const rol = rolInput.value;
  const contrasena = contrasenaInput.value;
  const sexo = sexoInput.value;
  const fechaNacimiento = fechaNacimientoInput.value;
  const telefono = telefonoInput.value;
  const email = emailInput.value;

  // Crear el objeto de datos a enviar
  const datosUsuario = {
    nombre: nombre,
    apellido: apellido,
    rol: rol,
    contrasena: contrasena,
    sexo: sexo,
    fecha_nacimiento: fechaNacimiento,
    telefono: telefono,
    email: email
  };

  // Realizar la solicitud POST al endpoint
  fetch('/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(datosUsuario)
  })
    .then(function(response) {
      if (response.ok) {
        // Redirigir al usuario a otra página o mostrar un mensaje de éxito
        window.location.href = '/registro_exitoso';
      } else {
        // Mostrar un mensaje de error
        console.error('Error en la solicitud:', response.status);
      }
    })
    .catch(function(error) {
      console.error('Error:', error);
    });
}