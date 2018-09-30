$('#add').click(function () {
	var product_cod = $(this).attr("data-productCod");
	$.ajax({
		url: '/add',
		dataType: 'application/json',
		type: 'GET',
		data: {
			cod: product_cod
		},
		complete: function (response) {
			alert('Added to cart.');
		}
	});
});