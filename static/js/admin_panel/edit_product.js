function update_tag(tid) {
    let pid = document.getElementById('product_id').value
    let tag_block = document.getElementById(`tag-${ tid }-block`)

    if (tag_block.childNodes[3].checked) {

        let xhr = new XMLHttpRequest();
        xhr.open('POST', `/admin_panel/add_tag`, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.responseType = 'json';

        xhr.onload = () => {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                tag_block.classList.remove('tag')
                tag_block.classList.add('tag-selected')
            }
        }

        xhr.send(`pid=${pid}&tid=${tid}`)

    } else {

        let xhr = new XMLHttpRequest();
        xhr.open('POST', `/admin_panel/remove_tag`, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.responseType = 'json';

        xhr.onload = () => {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                tag_block.classList.add('tag')
                tag_block.classList.remove('tag-selected')
            }
        }

        xhr.send(`pid=${pid}&tid=${tid}`)

    }

}

function update_cat(cid) {
    let pid = document.getElementById('product_id').value
    let tag_block = document.getElementById(`cat-${ cid }-block`)

    if (tag_block.childNodes[3].checked) {

        let xhr = new XMLHttpRequest();
        xhr.open('POST', `/admin_panel/add_cat`, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.responseType = 'json';

        xhr.onload = () => {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                tag_block.classList.remove('cat')
                tag_block.classList.add('cat-selected')
            }
        }

        xhr.send(`pid=${pid}&cid=${cid}`)

    } else {

        let xhr = new XMLHttpRequest();
        xhr.open('POST', `/admin_panel/remove_cat`, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.responseType = 'json';

        xhr.onload = () => {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                tag_block.classList.add('cat')
                tag_block.classList.remove('cat-selected')
            }
        }

        xhr.send(`pid=${pid}&cid=${cid}`)

    }
}



