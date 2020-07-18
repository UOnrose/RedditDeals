class DataHandler {
    constructor(data) {
        this.data = data;
        this.DrawData();
    }
    
    DrawData() {
        for (let i = 0; i < this.data['data']['children'].length; i++) {
            let child = this.data['data']['children'][i];
            
            var div = document.createElement("DIV");
            
            var text = document.createElement("A");
            text.innerHTML = child['data']['title'];
            text.setAttribute("href", child['data']['url'])
            
            div.appendChild(text);

            document.body.appendChild(div);
        }
    }
}