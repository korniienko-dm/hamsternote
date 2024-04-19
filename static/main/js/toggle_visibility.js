 /**
 * Toggles the visibility of an HTML element based on its ID.
 *
 * @param {string} clickedId - The ID of the HTML element that triggers the visibility change.
 * @param {string} targetId - The ID of the HTML element whose visibility will be toggled.
 * @returns {void}
 */
function toggleVisibility(clickedId, targetId) {
    // Get the target HTML element
    var targetElement = document.getElementById(targetId);

    // Get the element that triggered the visibility change
    var clickedElement = document.getElementById(clickedId);

    // Check if the target element was previously hidden
    var isVisible = targetElement.style.display === 'block';

    // Toggle the visibility of the target element
    targetElement.style.display = isVisible ? 'none' : 'block';

    // If the target element is currently hidden, display it with fadeIn animation
    if (!isVisible) {
        targetElement.style.animation = 'fadeIn 0.5s';
        // Scroll the page to show the target element
        targetElement.scrollIntoView({ behavior: 'smooth' });
    } else { // Otherwise, hide the element with fadeOut animation
        targetElement.style.animation = 'fadeOut 0.5s';
        // Delay hiding the element to allow time for the animation to complete
        setTimeout(function() {
            // Scroll the page to the element that triggered the visibility change
            clickedElement.scrollIntoView({ behavior: 'smooth' });
        }, 500); // Duration of the fadeIn/fadeOut animation
    }

    // Save the visibility state to sessionStorage
    sessionStorage.setItem(targetId, isVisible ? 'hidden' : 'visible');
}

// Restore the visibility state of the target element on page load
window.onload = function() {
    // Iterate through all elements with the 'div' class
    document.querySelectorAll('.div2').forEach(function(element) {
        // Check if the element's visibility state is stored in sessionStorage
        var visibilityState = sessionStorage.getItem(element.id);
        if (visibilityState === 'visible') {
            // If the element was visible, display it
            element.style.display = 'block';
        }
    });
};