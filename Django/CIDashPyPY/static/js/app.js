'use strict';

$(document).ready(function() {

  let tooglePasswordVisibility = function(event) {

    event.preventDefault();
    
    let inputField = document.getElementById('password');

    if (inputField.type === 'text') {
      inputField.type = 'password';
    } else {
      inputField.type = 'text';
    }

  }
  
  $('#toggle-password-visibility').click(tooglePasswordVisibility);

});