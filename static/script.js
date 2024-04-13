document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("form");
    var input = document.getElementById("entry");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        var query = input.value;

        var entries = {
            text: query,
        };

        // Using AJAX to send data to flask
        $.ajax({
            type: "POST",
            url: "/reemail", // route to Flask search
            contentType: "application/json",
            data: JSON.stringify(entries),
            success: function(response) {
                console.log(response); // print resulting html to console
                //displayResults(response); // display results using display function
            },
            error: function(xhr, status, error) {
                console.error(error);    
            }
        });
    });
});

