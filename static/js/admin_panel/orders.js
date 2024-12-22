function delete_order(oid) {
    document.getElementById('delete_modal').style.display = 'flex'
    let tr = document.getElementById(`o-${oid}`)
    let name = tr.childNodes[1].innerText

    document.getElementById('rm-modal-h').innerText = `Вы действительно хотите удалить заказ с серийным номером ${name}?`
    document.getElementById('rm-button').setAttribute('onclick', `confirm_delete_order(${oid})`)
}


function confirm_delete_order(oid) {

    let xhr = new XMLHttpRequest();
    xhr.open('POST', `/admin_panel/delete_order`, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.responseType = 'json';

    xhr.onload = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {

            document.getElementById(`delete_modal`).style.display = 'none'
            document.getElementById(`o-${oid}`).remove()

        }
    }

    xhr.send(`oid=${oid}`)

}
