/**
 * Loads the contents of the page at the specified URL without reloading the page.
 *
 * @param {Event} event - The event object that caused the page to load.
 * @param {string} url - URL of the page to be loaded.
 * @returns {void}
 */

function loadPage(event, url) {
    event.preventDefault(); // Preventing default link behavior

    var xhr = new XMLHttpRequest(); // Create a new XMLHttpRequest object

    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                // If the request is successful, update the page content
                document.body.innerHTML = xhr.responseText;
            } else {
                // Обработка ошибки
                console.error('Ошибка при загрузке страницы:', xhr.status);
            }
        }
    };

    xhr.open('GET', url, true); // Open a GET request to the specified URL
    xhr.send(); // Sending a request
}