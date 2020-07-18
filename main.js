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

window.onload = function() {
    console.log("Test");
    fetchJSONFile('https://www.reddit.com/r/buildapcsales/top.json?t=day', function(data) {
        console.log(data);
        dh = new DataHandler(data);
    });
}