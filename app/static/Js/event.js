const myFunction = document.getElementById("myFunction");
const myPopup = document.getElementById("myPopup");
myFunction.addEventListener("click", (e) => {
	myPopup.innerHTML = `
	<!-- this is the popup text -->
	<h4>Destiny Number 8</h4>

	<P>
		Lorem Ipsum is simply dummy text of the printing and typesetting industry.
		Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
		when an unknown printer took a galley of type and scrambled it to make a type specimen book.
	</P>
	
	<hr>
	<!-- this is the popup text ending-->`
	
	myPopup.classList.toggle("show");
});