document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();
    var registroInscripcion = document.querySelector("#registro_inscripcion").value;
    var verificacion = document.querySelector("#verificacion").checked;
    var necesidad = document.querySelector("#necesidad").value;
    var validacion = document.querySelector("#validacion").checked;
    var costo = document.querySelector("#costo").value;
    var entrega = document.querySelector("#entrega").checked;
  
    if (registroInscripcion == "") {
      alert("Debes ingresar un registro de inscripción");
      return;
    }
  
    if (necesidad == "") {
      alert("Debes ingresar una necesidad");
      return;
    }
  
    if (costo == "") {
      alert("Debes ingresar un costo");
      return;
    }
  
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/cajero");
    xhr.onload = function() {
      if (xhr.status >= 200 && xhr.status < 300) {
        alert("El formulario se ha enviado correctamente.");
      } else {
        alert("Hubo un error al enviar el formulario.");
      }
    };
    xhr.send(JSON.stringify({
      registro_inscripcion: registroInscripcion,
      verificacion: verificacion,
      necesidad: necesidad,
      validacion: validacion,
      costo: costo,
      entrega: entrega
    }));
  });