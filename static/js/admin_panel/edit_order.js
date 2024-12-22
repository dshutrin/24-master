function plus_product(id){
    let count = parseInt(document.getElementById('pcount-' + id).innerHTML)
    let xhr = new XMLHttpRequest();
        xhr.open('POST', `/admin_panel/upcount`, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.responseType = 'json';

        xhr.onload = () => {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                const price = parseFloat(xhr.response['price'])
                let pr = parseFloat(document.getElementById('p_t_price-' + id).innerHTML)
                document.getElementById('p_t_price-' + id).innerHTML = '' + (pr + price) + '₽'
                document.getElementById('pcount-' + id).innerHTML = '' + (count + 1)
                let tprice = parseFloat(document.getElementById('tprice').innerHTML)
                document.getElementById('tprice').innerHTML = '' + (tprice + price) + '₽'
            }
        }

        xhr.send('id=' + id)
}


function minus_product(id){
    let count = parseInt(document.getElementById('pcount-' + id).innerHTML)
    let xhr = new XMLHttpRequest();
        xhr.open('POST', `/admin_panel/downcount`, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.responseType = 'json';

        xhr.onload = () => {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                const price = parseFloat(xhr.response['price'])
                let pr = parseFloat(document.getElementById('p_t_price-' + id).innerHTML)
                document.getElementById('p_t_price-' + id).innerHTML = '' + (pr - price) + '₽'
                document.getElementById('pcount-' + id).innerHTML = '' + (count - 1)
                let tprice = parseFloat(document.getElementById('tprice').innerHTML)
                document.getElementById('tprice').innerHTML = '' + (tprice - price) + '₽'
            }
        }

        xhr.send('id=' + id)
}
