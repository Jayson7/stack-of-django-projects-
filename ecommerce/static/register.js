// modalc pop up config

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

button = document.getElementById("u");

// When the user activates the modal
var error = btn.innerHTML.search("WTF");
var success = btn.innerHTML.search(
    "Your account has been created successfully!"
);
if (error) {
    modal.style.display = "block";
}
if (success) {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

// ends