window.onload = function() {
    var btnEditar = document.querySelectorAll(".btn-primary");
        
        btnEditar.forEach(function(boton) {
        boton.addEventListener("click", function() {

            var formulario = this.parentNode.parentNode;

            formulario.querySelector("#nombre").disabled = false;
            formulario.querySelector("#dni").disabled = false;
            formulario.querySelector("#mascota").disabled = false;
            formulario.querySelector("#fecha_nacimiento").disabled = false;
            formulario.querySelector("#tipo").disabled = false;
            formulario.querySelector("#raza").disabled = false;
            formulario.querySelector(".btn-success").style.display = "inline-block";

            this.style.display = "none";
        });
    });
}

function ordenarRegistro() {
    $(document).ready(function() {
    $('#ordenar-form').submit(function(event) {
        event.preventDefault();
        $.ajax({
        url: "{{ url_for('ordenar_registro') }}",
        data: $(this).serialize(),
        type: 'POST',
        success: function(response) {
            $('#clientes-table tbody').html(response);
        },
        error: function(error) {
            console.log(error);
        }
        });
    });
    });
}