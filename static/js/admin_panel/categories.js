function delete_category(cid) {

    document.getElementById('delete_modal').style.display = 'flex'
    document.getElementById('rm-button').setAttribute('onclick', `confirm_delete_cat(${cid})`)

}


function confirm_delete_cat(cid) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', `/admin_panel/categories/delete`, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.responseType = 'json';

    xhr.onload = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {

            document.getElementById(`delete_modal`).style.display = 'none'
            document.getElementById(`c-${cid}`).remove()

        }
    }

    xhr.send(`cid=${cid}`)
}




function do_main_cat(cid){
    if (document.getElementById(`ca-${cid}`).checked) {
        let xhr = new XMLHttpRequest();
        xhr.open('POST', `/admin_panel/categories/do_main`, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.responseType = 'json';
        xhr.onload = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 220){
            document.getElementById(`ca-${cid}`).checked = false
            }
        else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200){
            document.getElementById(`td-${cid}`).innerHTML = '<a class="edit" href="/admin_panel/categories/edit/' + cid + '"><i class="material-icons-outlined">edit</i></a><button class="delete" onclick="delete_category(' + cid +')"><i class="material-icons-outlined">delete</i></button>'
            }
        }
        xhr.send(`cid=${cid}`)

    }
    else{
        let xhr = new XMLHttpRequest();
        xhr.open('POST', `/admin_panel/categories/do_common`, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.responseType = 'json';
        xhr.send(`cid=${cid}`)
        xhr.onload = () => {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200){
                document.getElementById(`td-${cid}`).innerHTML = '<button class="delete" onclick="delete_category(' + cid +')"><i class="material-icons-outlined">delete</i></button>'
        }}
        }
    }




