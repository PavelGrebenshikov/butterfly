function addProduct(product_id) {
    var this_script = $('script[src*="/static/js/cart.js"]');
    var url = this_script.attr('data-url');
    var csrf = this_script.attr('data-csrf');

    $.post({
        url: url,
        data: {
            product_id: product_id,
            csrfmiddlewaretoken: csrf
        },
        success: function(response) {
            console.log(response);
        }
    });
}
