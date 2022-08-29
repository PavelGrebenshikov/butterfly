
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


function changeItemCount(product_id, sign) {
    var this_script = $('script[src*="/static/js/cart.js"]');
    var url = this_script.attr('data-change-count-url');
    var csrf = this_script.attr('data-csrf');

    $.post({
        url: url,
        data: {
            product_id: product_id,
            sign: sign,
            csrfmiddlewaretoken: csrf
        },
        success: function(response) {
            var product_name = $(`a:contains("${response.item.name}")`);

            var count = product_name.siblings('.product__info_count');
            count.html(response.item.count);

            var price = product_name.siblings('.product__info_price');
            price.html(prettyNumber(response.item.price * response.item.count));

            var total = $('.cart__total_price');
            total.html(prettyNumber(response.item.total_price));

        }
    });
}


function prettyNumber(number) {
    return (+number).toFixed(2).toString().replace('.', ',');
}
