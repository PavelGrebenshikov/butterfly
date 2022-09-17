
function addProduct(product_id, event) {
    var this_script = $('script[src*="/static/js/cart.js"]');
    var url = this_script.attr('data-url');
    var csrf = this_script.attr('data-csrf');
    var button = event.target;

    $.post({
        url: url,
        data: {
            product_id: product_id,
            csrfmiddlewaretoken: csrf
        },
        success: function (_) {
            $(button)
                .html(isFullButton(button) ? 'Перейти в кoрзину' : 'В КOРЗИНЕ')
                .removeAttr('onclick')
                .attr('href', '/cart/');

            if (!isFullButton(button)) {
                $(button).addClass('disabled');
            }
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
            var item = product_name.parent().parent().parent()

            var count = item.find('.count__items');
            count.html(response.item.count);

            var price = item.find('.item__price p');
            price.html(prettyNumber(response.item.price * response.item.count));

            var total = $('.total__price');
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

            product_name.parents('.cart__products').remove();

            var total = $('.total__price');
            total.html(prettyNumber(response.total_price));

            if ($('.cart__products').length == 0) {
                $('.cart').remove();
                $('.container').append('<div>Ваша корзина пока что пуста...</div>');
                $('.anonym-warning').remove();
            }
        }
    });
}


function prettyNumber(number) {
    return (+number).toFixed(2).toString().replace('.', ',');
}


function isFullButton(button) {
    return $(button).hasClass('add-to-basket__button');
}
