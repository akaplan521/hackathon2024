document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("form");
    var input = document.getElementById("entry");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        var query = input.value;
        console.log("Search Query:", query);
        var entries = {
            text: query,
        };

        console.log("Search Query:", query);

        // Using AJAX to send data to flask
        $.ajax({
            type: "POST",
            url: "/test", // route to Flask search
            contentType: "application/json",
            headers: {                                  
                'Accept': 'application/json',
                'Content-Type': 'application/json' 
            }, 
            data: JSON.stringify(entries),
            success: function(response) {
                console.log(response); // print resulting html to console
                displayResults(response); // display results using display function
            },
            error: function(xhr, status, error) {
                console.error(error);    
            }
        });
    });

    //function to display the results
    function displayResults(data) {
        var searchResultsDiv = document.getElementById("search-results");
        searchResultsDiv.innerHTML = ""; // Clear previous results
        
        data.forEach(function(row) {
            console.log(row)
            var smithBox = document.createElement("div");
            smithBox.classList.add("smith-box");
            var id = row[0]


            // Create and append profile image
            var anchor = document.createElement("a");
            anchor.href = `http://localhost:8097/${id}`;
            anchor.target = "_blank";
            var image = document.createElement("img");
            image.src = "static/img/pfp.jpg";
            image.alt = "Smith";
            anchor.appendChild(image);
            smithBox.appendChild(anchor);

            //create and append learn more button
            var learnMoreButton = document.createElement("a");
            learnMoreButton.href = `http://localhost:8097/${id}`;
            var button = document.createElement("button");
            button.classList.add("button");
            button.textContent = "Learn More";
            learnMoreButton.appendChild(button);
            smithBox.appendChild(learnMoreButton);
            searchResultsDiv.appendChild(smithBox);
        });
    }
});

