document.addEventListener("DOMContentLoaded", function() {
    const button = document.getElementById("dropdown-button");
    const dropdownMenu = document.getElementById("dropdown-menu");

    if (button && dropdownMenu) {
        button.addEventListener("click", function(event) {
            event.stopPropagation(); // Prevent the click event from propagating to the document
            dropdownMenu.classList.toggle("hidden");
        });

        document.addEventListener("click", function(event) {
            if (!dropdownMenu.contains(event.target)) {
                dropdownMenu.classList.add("hidden");
            }
        });
    } else {
        console.error("Button or dropdown menu not found.");
    }
});
