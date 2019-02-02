var currentTab = 0;
showTab(currentTab);

function showTab(n) {

    var x = document.getElementsByClassName("tabview");
    x[n].style.display = "block";

    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "Submit";
    } else {
        document.getElementById("nextBtn").innerHTML = "Next";
    }

    fixStepIndicator(n)
}

function nextPrev(n) {

    var x = document.getElementsByClassName("tabview");

    if (n == 1 && !validateForm()) return false;
    // Hides the current tab:
    x[currentTab].style.display = "none";

    currentTab = currentTab + n;

    if (currentTab >= x.length) {
        //  if the form reaches the end it gets submitted:
        document.getElementById("tab_form").submit();
        return false;
    }
   
    showTab(currentTab);
}


function validateForm() {
    //this valodation checks inputs fields for data if not does not validate. 
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tabview");
    y = x[currentTab].getElementsByTagName("input");

    for (i = 0; i < y.length; i++) {

        if (y[i].value == "") {

            y[i].className += " invalid";

            valid = false;
        }
    }

    if (valid) {
        document.getElementsByClassName("steps")[currentTab].className += " finish";
    }
    return valid;
}

function fixStepIndicator(n) {
    
    var i, x = document.getElementsByClassName("steps");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace("active", "");
    }

    x[n].className += " active";
}
