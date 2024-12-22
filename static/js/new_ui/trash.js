function update_uitp_count_(uid, pid) {
    let new_value = document.getElementById(`p-${pid}`).value

    let xhr = new XMLHttpRequest()
    xhr.open('POST', `/update_uitp_count_`, true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = "json"

    xhr.onload = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {

			document.getElementById('ts').innerText = `Общая стоимость: ${xhr.response['sm']} ₽`

        }
    };

    xhr.send(`uid=${uid}&pid=${pid}&val=${new_value}`);
}

function rm_prd(pid) {
	let xhr = new XMLHttpRequest()
    xhr.open('POST', `/remove_product_from_trash`, true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = "json"

    xhr.onload = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {

			document.getElementById(`tp-${pid}`).remove()
            document.getElementById('ts').innerText = `Общая стоимость: ${xhr.response['sm']} ₽`

        }
    };

    xhr.send(`pid=${pid}`);
}

function add_order(uid) {
	let xhr = new XMLHttpRequest()
    xhr.open('POST', `/add_order`, true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = "json"

    xhr.onload = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {

			window.location.reload()

        }
    };

    xhr.send(`uid=${uid}`);
}