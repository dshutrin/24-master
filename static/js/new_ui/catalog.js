function update_uitp_count(uid, pid) {
	let new_value = document.getElementById(`p-${pid}`).value

	let xhr = new XMLHttpRequest()
    xhr.open('POST', `/update_uitp_count`, true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = "json"

    xhr.onload = () => {
		if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
		}
	};

    xhr.send(`uid=${uid}&pid=${pid}&val=${new_value}`);
}

function add_product_to_trash(uid, pid) {

	let xhr = new XMLHttpRequest()
    xhr.open('POST', `/add_product_to_trash`, true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = "json"

    xhr.onload = () => {
		if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {

			let div = document.getElementById(`dp-${pid}`)
			div.innerHTML = `<input id="p-${pid}" onchange="update_uitp_count(${uid}, ${pid})" class="catalog-product-count" value="1" type="number">`

		}
	};

    xhr.send(`pid=${pid}`);

}
