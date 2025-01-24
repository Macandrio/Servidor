document.addEventListener('DOMContentLoaded', function () {
    const selectRol = document.getElementById('id_rol'); // Campo select de rol
    const codigoGerente = document.getElementById('id_codijo_gerente'); // Campo de código de gerente

    // Función para mostrar u ocultar el campo de código gerente
    function toggleCodigoGerente() {
        if (selectRol.value === 'Gerente') { // Verifica si el valor seleccionado es "Gerente"
            codigoGerente.parentElement.style.display = 'block'; // Muestra el campo
        } else {
            codigoGerente.parentElement.style.display = 'none'; // Oculta el campo
        }
    }

    // Inicializa la visibilidad al cargar la página
    toggleCodigoGerente();

    // Agrega un evento al selector para escuchar los cambios
    selectRol.addEventListener('change', toggleCodigoGerente);
});
