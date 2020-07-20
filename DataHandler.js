/*
    Author: Noah Rose
    Description: The DataHandler class handles all of the JSON data and displays it on the RedditDeals website
*/

class DataHandler {

    // Constructor calls DrawData to display the default data and creates an event listener for the selections
    constructor(data) {
        this.data = data;
        let that  = this;
        
        this.DrawData();

        // Event listener that activates when the user presses the search button
        document.getElementById("Search").addEventListener("click", function(){
            let sub = document.getElementById("Subreddit");
            sub = sub.options[sub.selectedIndex].value;
            
            let time = document.getElementById("Time");
            time = time.options[time.selectedIndex].value;

            that.UpdateData(that.GenerateLink(sub, time));
        });
    }
    

    // Display the current class data on the page
    DrawData() {
        for (let i = 0; i < this.data['data']['children'].length; i++) {
            let child = this.data['data']['children'][i];
            
            let div = document.createElement("DIV");
            div.setAttribute("Class", "entry");

            let text = document.createElement("A");
            text.innerHTML = child['data']['title'];
            text.setAttribute("href", child['data']['url']);
            
            div.appendChild(text);

            document.body.appendChild(div);
        }
    }


    // Update data with a given link
    UpdateData(link) {
        let that = this;
        fetchJSONFile(link, function(data) {
            that.data = data;
            document.querySelectorAll(".entry").forEach(e => e.remove());
            that.DrawData();
        });
    }


    // Generate a link to the JSON data given a subreddit and timerange
    GenerateLink(sub, time) {
        return 'https://www.reddit.com/' + sub + '/top.json?t=' + time;
    }
}