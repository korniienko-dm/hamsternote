// The script determines the height of the parent container .main-container and sets all base containers to the same height.
// Ignoring the height of the blocks based on their content.

window.onload = function() {
    // Get the height of the container
    var containerHeight = document.querySelector(".main-container").offsetHeight;

    // Assign the same height to the remaining elements
    var elementsToUpdate = document.querySelectorAll(
        '.navigation-menu,' +
        ' .wrapper-listbar, ' +
        '.wrapper-detail-listbar, ' +
        '.wrapper-contentbar, ' +
        '.ulist-wrapper-listbar, ' +
        '.contact-detail-wrapper');
    elementsToUpdate.forEach(function(element) {
        element.style.height = containerHeight + 'px';
    });
    console.log("auto-height - run")
};