
function on_signIn_click(){

    if("[@authfield:Admin]" == "Yes"){
        window.location = "Admin_Panel.html";
        }
        else if ("[@authfield:User]" == "Yes"){
        window.location = "user_profile.html";
        }
        else{
        window.location = "sign_up.html";
        }
}
