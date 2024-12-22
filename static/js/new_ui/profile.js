function update_contacts() {
	let email = document.getElementById('email').value
	let phone_number = document.getElementById('phone_number').value

	let xhr = new XMLHttpRequest()
    xhr.open('POST', `/update_contacts`, true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = "json"

    xhr.onload = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {

			let btn = document.getElementById('save_contacts')
	        document.getElementById('contacts-list').style.backgroundColor = 'lightgreen'

	        btn.innerText = 'Данные обновлены!'

	        setTimeout(() => {
				document.getElementById('contacts-list').style.backgroundColor = 'rgba(136, 136, 136, 0.1)'
				btn.innerText = 'Сохранить'
	        }, 2000)

        } else {
			let btn = document.getElementById('save_contacts')
	        document.getElementById('contacts-list').style.backgroundColor = 'indianred'

	        btn.innerText = 'Ошибка!'

	        setTimeout(() => {
				document.getElementById('contacts-list').style.backgroundColor = 'rgba(136, 136, 136, 0.1)'
				btn.innerText = 'Сохранить'
	        }, 2000)
        }
    };

    xhr.send(`email=${email}&phone_number=${phone_number}`);
}
