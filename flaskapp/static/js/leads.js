// get important attributes of the html
var passwordForm = $('#passwordForm');
var passwordField = $('#passwordField');
var apiRoot = 'http://127.0.0.1:5000/api';

// hide the table at first, display a password text box
var leadTable = $('#lead-table');
leadTable.hide();

// allow password show
function showPassword() {
  var x = document.getElementById("passwordField");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

// create a function that removes the leads from the database
function removeLead(id) {
    $.ajax({
        type: "DELETE",
        url: apiRoot + '/JobScrapeLead',
        data: JSON.stringify({
            leadId: id
        }),
        success: function (result) {
            // remove the lead from the page
            $('tr#' + id.toString()).remove();
        },
        failure: function (msg) {
            alert(msg);
        }
    });
}

// create a function to verify the password --> bind to submit form (use case: lead_login)
passwordForm.submit(function(e) {
    e.preventDefault();
    var enteredPassword = passwordField.val();
    var companyContactTemplate = $('#company-contact-template').html();

    // submit the request with ajax
    $.ajax({
        type: "POST",
        // THIS WILL NEED TO BE CHANGED UPON RELEASE
        url: apiRoot + "/VerifyPassword",
        data: JSON.stringify(
            {
                use_case: 'lead_login',
                password: enteredPassword
            }),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
            // unhide the table
            leadTable.show(1000);
            passwordForm.hide(1000);

            // populate the table
            $.ajax({
                type: "GET",
                // THIS WILL NEED TO BE CHANGED UPON RELEASE
                url: apiRoot + "/JobScrapeLead",
                success: function (data) {
                    var openLeads = data.open_leads;

                    // iterate through all of the open leads and fill the table
                    for (i = 0; i < openLeads.length; i++) {
                        lead = openLeads[i];

                        // add it to the potential players
                        leadTable.append(Mustache.render(companyContactTemplate, lead));

                      }
                },
                failure: function (msg) {
                    alert(msg);
                }
            });


        },
        failure: function (msg) {
            alert(msg);
        },
        complete: function (msg, status) {
            if (status == 403)
            {
                console.log('Incorrect password');
            }
        }
        });
    passwordField.val('');
});

