let CONTACT_METHODS = ['telegram', 'discord', 'whatsapp'];

function addEmail() {
    var email_element = $('#email-footer4-f');
    var email = email_element.val();

    // add the email via ajax
    if (email.length > 0)
    {
        $.ajax({
              type: 'POST',
              // THIS WILL NEED TO BE CHANGED!!!
              url: "http://127.0.0.1:5000/add_lead",
              data: JSON.stringify(
                {
                    'email': email
                }),
              success: function (response) {
                // reset the email element
                email_element.val('');
                console.log(response);
              },
              error: function () {
                alert('error getting data');
              }
        });
    }
}

function addTextField(element)
{

  var additionalContactTemplate = $('#additionalContactTemplate').html();
  var additionalPlatforms = $('#additionalPlatforms');

  var additionalText = {
    method: element.innerHTML
  }

  additionalPlatforms.append(Mustache.render(additionalContactTemplate, additionalText));

}


// add a submission reaction
$('#contactForm').submit(function(e) {
  e.preventDefault();

  // load in the data
  var name = $('#nameField').val();
  var phoneNumber = $('#phoneField').val();
  var email = $('#emailField').val();
  var subject = $('#subjectField').val();
  var message = $('messageField').val();

  // get an array of added platforms
  var addedPlatforms = $('input[label="additionalPlatform"]').map(function(i,el) {
    var username = $(el).val();
    var platform = $(el).attr('placeholder');
    var new_platform = {
      username: username,
      platform: platform
    }

    return new_platform;
    }).get();

  console.log(addedPlatforms);

});

