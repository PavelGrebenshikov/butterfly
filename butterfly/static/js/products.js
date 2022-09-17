function sendGetFormData(form_name, event) {
    var form_elements = document.forms[form_name].elements;
    var new_params = new URLSearchParams(location.search);

    for (let i = 0; i < document.forms[form_name].length; i++) {
        if (form_elements[i].type != 'submit') {
            new_params.set(form_elements[i].name, form_elements[i].value);
        }

    }

    location.search = new_params;
    event.preventDefault();
}
