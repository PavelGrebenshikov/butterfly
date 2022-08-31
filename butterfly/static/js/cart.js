
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
        success: function (response) {
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
        success: function (response) {
            var product_name = $(`a:contains("${response.item.name}")`);

            var count = product_name.siblings('.product__info_count');
            count.html(response.item.count);

            var price = product_name.siblings('.product__info_price');
            price.html(prettyNumber(response.item.price * response.item.count));

            var total = $('.cart__total_price');
            total.html(prettyNumber(response.total_price));

        }
    });
}


function deleteItem(product_id) {
    var this_script = $('script[src*="/static/js/cart.js"]');
    var url = this_script.attr('data-delete-url');
    var csrf = this_script.attr('data-csrf');

    $.post({
        url: url,
        data: {
            product_id: product_id,
            csrfmiddlewaretoken: csrf
        },
        success: function (response) {
            var product_name = $(`a:contains("${response.item.name}")`);

            product_name.parents('.product__info').remove();

            var total = $('.cart__total_price');
            total.html(prettyNumber(response.total_price));

            if ($('.product__info').length == 0) {
                $('.cart__total').remove();
                $('.cart__products').html('Ваша корзина пока что пуста...');
            }
        }
    });
}


function prettyNumber(number) {
    return (+number).toFixed(2).toString().replace('.', ',');
}
