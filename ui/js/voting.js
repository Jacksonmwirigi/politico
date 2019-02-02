


            var currentTab = 0; // Current tab is set to be the first tab (0)
            showTab(currentTab); // Display the crurrent tab
            
            function showTab(n) {
              // This function will display the specified tab of the form...
              var x = document.getElementsByClassName("tabview");
              x[n].style.display = "block";
              //... and fix the Previous/Next buttons:
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
              //... and run a function that will display the correct step indicator:
              fixStepIndicator(n)
            }

// var currentTab = 0;
// displayTabs(currentTab);
// function displayTabs(n) {
//     x = document.getElementsByClassName("tabview")
//     x[n].style.display = "block";

//     if (n == 0) {
//         document.getElementById("prevBtn").style.display = "none";
//     }
//     else {
//         //if tabs are not finished  the previous button moves to prevnext tab are set to display.
//         document.getgetElementByIdElementsByName("prevBtn").style.display = "inline";
//     }

//     if (n == (x.length - 1))  {
//         document.getElementById("nextBtn").innerHTML = "Submit";
//     }

//     else {
//         document.getElementById("nextBtn").innerHTML = "Next";
//     }
//     fixStepIndicator(n)
// }

// function nextPrev(n) {
//     var x = document.getElementsByClassName("tabview");
//     if (n == 1 && !validateForm()) return false;
//     x[currentTab].style.display = "none";

//     currentTab = currentTab + 1;

//     if (currentTab >= x.length) {

//         document.getElementById("tab_form").submit();
//         return false;
//     }

//     displayTabs(currentTab);
// }
function nextPrev(n) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tabview");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form...
    if (currentTab >= x.length) {
      // ... the form gets submitted:
      document.getElementById("tab_form").submit();
      return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
  }

// function nextPrev(n) {

//     var x = document.getElementsByClassName("tab");
//     if (n == 1 && !validateForm()) return false;
//     x[currentTab].style.display = "none";
//     currentTab = currentTab + n;
//     if (currentTab >= x.length) {

//       document.getElementById("regForm").submit();
//       return false;
//     }

//     showTab(currentTab);
//   }

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

// function fixStepIndicator(n) {
//     var i, x = document.getElementsByClassName("steps");

//     for (i = 0; i < x.length; i++) {

//         x[i].className = x[i].className.replace("active", "");

//     }

//     x[n].className += " active";

// }

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("steps");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace("active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}
