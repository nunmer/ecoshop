// document.addEventListener('DOMContentLoaded', function() {
// 	const signUpButton = document.getElementById('signup');
// 	const signInButton = document.getElementById('signIn');
// 	const container = document.getElementById('container');

// 	signUpButton.addEventListener('click', () => {
// 		container.classList.add("right-panel-active");
// 	});

// 	signInButton.addEventListener('click', () => {
// 		container.classList.remove("right-panel-active");
// 	});
// });

$('.purchase_product').click(function(){
	var productId = $(this).data('product-id');
            
	$.ajax({
		type: 'POST',
		url: '/products/purchase/' + productId,
		data: {
			csrfmiddlewaretoken: '{{ csrf_token }}'
		},
		success: function(data){
			// Handle success response
			console.log(data);
			if (data.success) {
				// Show Toastr message
				toastr.success(data.message);
				// Redirect to products page after a delay
				setTimeout(function(){
					window.location.href = '/products';
				}, 2000); // Redirect after 2 seconds (adjust as needed)
			} else {
				toastr.error('Failed to purchase product.');
			}
		},
		error: function(xhr, textStatus, errorThrown){
			// Handle error
			console.log(xhr.responseText);
			toastr.error('Failed to purchase product.');
		}
	});
})