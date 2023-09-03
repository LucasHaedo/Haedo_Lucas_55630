form.addEventListener('submit', event => {
    event.preventDefault(); // Agregar esta línea
    const peliculaId = form.action.split('/').pop();
    const data = new FormData(form);
    fetch(`/peliculas/${peliculaId}/valorar/`, {
        method: 'POST',
        body: data,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Mostrar el mensaje de éxito
        alert(data.message);
        // Actualizar los datos de la película
        const peliculaElement = form.closest('li');
        peliculaElement.querySelector('.promedio').textContent = data.promedio;
        peliculaElement.querySelector('.cantidad').textContent = data.cantidad;

        
    });
});