document.querySelector("form").addEventListener("submit", function(event) {
  event.preventDefault();
  var medicamento = document.querySelector("#medicamento").value;
  var tipo_de_toma = document.querySelector("#tipo_de_toma").value;
  var cantidad = document.querySelector("#cantidad").value;
  var unidad_medida = document.querySelector("#unidad_medida").value;
  var porcentaje = document.querySelector("#porcentaje").value;
  var ml_g = document.querySelector("#ml_g").value;

  if (medicamento == "") {
    alert("Debes ingresar un medicamento");
    return;
  }

  if (tipo_de_toma == "") {
    alert("Debes ingresar un tipo de toma");
    return;
  }

  if (cantidad == "") {
    alert("Debes ingresar una cantidad");
    return;
  }

  if (unidad_medida == "") {
    alert("Debes ingresar una unidad de medida");
    return;
  }

  if (porcentaje == "") {
    alert("Debes ingresar un porcentaje");
    return;
  }

  if (ml_g == "") {
    alert("Debes ingresar ml/g");
    return;
  }

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/receta");
  xhr.onload = function() {
    if (xhr.status >= 200 && xhr.status < 300) {
      alert("La receta se ha enviado correctamente.");
    } else {
      alert("Hubo un error al enviar la receta.");
    }
  };
  xhr.send(JSON.stringify({
    medicamento: medicamento,
    tipo_de_toma: tipo_de_toma,
    cantidad: cantidad,
    unidad_medida: unidad_medida,
    porcentaje: porcentaje,
    ml_g: ml_g
  }));
});
