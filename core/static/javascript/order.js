function finish_order(){
	if(confirm("Finish the order?")){
		return alert("Your order has been successfully completed.");
	}
	else{
		return false;
	}
}