
const API_publicKey = "FLWPUBK-cd569e78021ef697fb6869e584f37431-X";  //"FLWPUBK-3e6695d9ccccf54ea70a8c26b258fcbb-X"; 
//test// FLWPUBK-cd569e78021ef697fb6869e584f37431-X


function payWithRave() {
	var email = document.getElementById('email').value;
	var amount = document.getElementById('amount').value;
	var x = getpaidSetup({
		PBFPubKey: API_publicKey,
		customer_email: email,
		amount: amount,
		customer_phone: "234099940409",
		currency: "NGN",
		txref: "rave-123456",
		meta: [{
			metaname: "flightID",
			metavalue: "AP1234"
		}],
		onclose: function() {},
		callback: function(response) {
			var txref = response.tx.txRef; // collect txRef returned and pass to a 					server page to complete status check.
			var amount = response.tx.amount;
			
			console.log("This is the response returned after a charge", response);
			if (
				response.tx.chargeResponseCode == "00" ||
				response.tx.chargeResponseCode == "0"
			) {
				// redirect to a success page 
				window.location.replace("http://127.0.0.1:5000/paysuccess?resp="+amount);
				
			} else {
				// redirect to a failure page.
				window.location.replace("http://127.0.0.1:5000/payfailed");
			}

			x.close(); // use this to close the modal immediately after payment.
		}
	});
}

