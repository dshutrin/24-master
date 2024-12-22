function delete_role(rid) {
        document.getElementById('delete_modal').style.display = 'flex'
        let tr = document.getElementById(`r-${rid}`)
        let name = tr.childNodes[1].innerText

        document.getElementById('rm-modal-h').innerText = `Вы действительно хотите удалить эту роль?`
        document.getElementById('rm-button').setAttribute('onclick', `delete_role_ok(${rid})`)
}

function delete_role_ok(rid){
        let xhr = new XMLHttpRequest();
        xhr.open('POST', `/admin_panel/delete_role/${rid}`, true);
        xhr.onload = () => {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                document.getElementById('delete_modal').style.display = 'none'
                document.getElementById(`r-${rid}`).remove()

            }
        }
        xhr.send();
}
