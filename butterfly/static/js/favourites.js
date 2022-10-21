
function addProductToFavourites(product_id) {
    const this_script = $('script[src*="/static/js/favourites.js"]');
    const url = this_script.attr('data-add-product-url');
    const csrf = this_script.attr('data-csrf');

    $.post({
        url: url,
        data: {
            product_id: product_id,
            csrfmiddlewaretoken: csrf
        },
        success: function (response) {
            var product_name = $(`a:contains("${response.product.name}")`);

            product_name.parents('.cart__products').remove();

            var total = $('.total__price');
            total.html(prettyNumber(response.cart_total_price));

            if ($('.cart__products').length == 0) {
                $('.cart').remove();
                $('.container').append('<div>Ваша корзина пока что пуста...</div>');
                $('.anonym-warning').remove();
            }
        }
    });
}
