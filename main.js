/*
    Author: Noah Rose
    Description: Main JavaScript program for running the RedditDeals website
*/

// Parses a JSON file and sends it to a callback function
// Takes file location and callback function as arguments
function fetchJSONFile(path, callback) {
    let httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === 4) {
            if (httpRequest.status === 200) {
                let data = JSON.parse(httpRequest.responseText);
                if (callback) callback(data);
            }
        }
    };
    httpRequest.open('GET', path);
    httpRequest.send();
}

// When the DOM is loaded this creates a new DataHandler object and initializes default data
window.onload = function() {
    let sub = document.getElementById("Subreddit");
    sub = sub.options[sub.selectedIndex].value;
    
    let time = document.getElementById("Time");
    time = time.options[time.selectedIndex].value;

    link = 'https://www.reddit.com/' + sub + '/top.json?t=' + time;
    
    fetchJSONFile(link, function(data) {
        dh = new DataHandler(data);
    });
}