// Espera a que el documento esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {

    // Obtiene el formulario por su ID
    var form = document.getElementById('myForm');
  
    // Añade un evento de escucha para el envío del formulario
    form.addEventListener('submit', function(event) {
  
      // Obtiene los valores de los campos del formulario
      var name = document.getElementById('name').value;
      var email = document.getElementById('email').value;
  
      // Valida los campos del formulario
      if(name === "" || email === "") {
        alert("Por favor, rellena todos los campos del formulario.");
        event.preventDefault(); // Previene el envío del formulario
      } else {
        // Aquí puedes añadir el código para manejar el envío del formulario
        // Por ejemplo, podrías enviar los datos a un servidor con AJAX
        console.log("Formulario enviado con éxito.");
      }
    });
  });
  