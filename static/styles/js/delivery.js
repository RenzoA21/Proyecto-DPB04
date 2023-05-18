document.querySelector("#form").addEventListener("submit", function(event) {
  event.preventDefault();
  var direccion = document.querySelector("#direccion").value;
  var vehiculo = document.querySelector("#vehiculo").value;
  var placa = document.querySelector("#placa").value;
  var metodo_pago = document.querySelector("#metodo_pago").value;
  var hora_entrega = document.querySelector("#hora_entrega").value;
  var image_pedido = document.querySelector("#image_pedido").files[0];
  if (direccion == "") {
    alert("Debes ingresar una dirección");
    return;
  }

  if (vehiculo == "") {
    alert("Debes ingresar un vehículo");
    return;
  }

  if (placa == "") {
    alert("Debes ingresar una placa");
    return;
  }

  if (metodo_pago == "") {
    alert("Debes ingresar un método de pago");
    return;
  }

  if (hora_entrega == "") {
    alert("Debes ingresar una hora de entrega");
    return;
  }

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/delivery");
  xhr.onload = function() {
    if (xhr.status == 200) {
      alert("El formulario se ha enviado correctamente,200");
    } else {
      alert("Hubo un error al enviar el formulario,300");
    }
  };
  xhr.send(JSON.stringify({
    direccion: direccion,
    vehiculo: vehiculo,
    placa: placa,
    metodo_pago: metodo_pago,
    hora_entrega: hora_entrega,
    image_pedido: image_pedido
  }));
});
