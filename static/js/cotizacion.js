document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();
    var insumo = document.querySelector("#insumo").value;
    var porcentaje = document.querySelector("#porcentaje").value;
    var cantidad = document.querySelector("#cantidad").value;
    var control = document.querySelector("#control").checked;
    var precio = document.querySelector("#precio").value;
    var total = document.querySelector("#total").value;
  
    if (insumo == "") {
      alert("Debes ingresar un insumo");
      return;
    }
  
    if (porcentaje == "") {
      alert("Debes ingresar un porcentaje");
      return;
    }
  
    if (cantidad == "") {
      alert("Debes ingresar una cantidad");
      return;
    }
  
    if (precio == "") {
      alert("Debes ingresar un precio");
      return;
    }
  
    if (total == "") {
      alert("Debes ingresar un total");
      return;
    }
  
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/cotizacion");
    xhr.onload = function() {
      if (xhr.status >= 200 && xhr.status < 300) {
        alert("La cotización se ha enviado correctamente.");
      } else {
        alert("Hubo un error al enviar la cotización.");
      }
    };
    xhr.send(JSON.stringify({
      insumo: insumo,
      porcentaje: porcentaje,
      cantidad: cantidad,
      control: control,
      precio: precio,
      total: total
    }));
  });