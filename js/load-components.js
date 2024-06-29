document.addEventListener('DOMContentLoaded', function() {
    function loadComponent(url, elementId) {
        fetch(url)
            .then(response => response.text())
            .then(data => {
                document.getElementById(elementId).innerHTML = data;
            })
            .catch(error => console.error('Error loading component:', error));
    }

    loadComponent('components/navbar-component.html', 'navbar-placeholder');
    loadComponent('components/footer-component.html', 'footer-placeholder');
});