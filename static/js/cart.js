// update cart functionality

let cart = [];
let cartLocal;
let quantity = 0;
let currentUrl;

$(document).ready(function(){
    currentUrl = $(location).attr('href');
    // cart from localstorage
    cartLocal = getFromLocal('cart');
    if (cartLocal != null){
        cart = cartLocal.length>0 ? cartLocal : cart;
    }
    if (cartLocal){
        $('#cart-total').text(cartLocal.length);
    }
    else{
        $('#cart-total').text(0);
    }

    // cart update buttons
    $(".update-cart").on('click', function(e){
    let thisElem = $(this);
        updateCart(e, thisElem);
    });


    // product quantity
    quantity = getProductQuantity(cartLocal);
    $('#item-quantity').text(quantity);

    // local cart total
    let total = getCartTotal(quantity, cartLocal);
    $("#item-total").text(' $'+total);

    // if cart page
    if (isCartPage(currentUrl)){
        populateCartItems($, 'dynamic-cart-items', cartLocal);
        // when delete item is clicked
        $('.cart-delete').on('click', function(){
            let thisElem = $(this);
           deleteLocal('cart', thisElem);
        });
    }

    // if checkout page
    if (isCheckoutPage(currentUrl)){
        populateCheckoutItems($, 'cart-row-container', cartLocal);
        populateItemAndTotalElem($, 'summary-container', cartLocal);
        populateCartField($, 'cart-field', cartLocal);
    }
});

function updateCart(e, thisElem){
    let productId = thisElem.data('product');
    let productPrice = thisElem.data('price');
    let imageUrl = thisElem.data('image');
    let name = thisElem.data('name');
    let action = thisElem.data('action');

    let product = {
        'id': productId,
        'price': productPrice,
        'image': imageUrl,
        'name': name,
        'action': action
    };
    let exist = false;
    if (action === 'add-once'){
        cart.forEach(function(item){
            if (item.id === product.id){
                exist = true;
                return false;
            }
        });
        if (!exist){
            cart.push(product);
            $("#cart-total").text(cart.length);
            saveToLocal('cart', cart);
        }
    }
    console.log(cart);
}

function saveToLocal(key, value){
    value = JSON.stringify(value);
    localStorage.setItem(key, value);
    console.log(value);
}

function getFromLocal(key){
    let storage = localStorage.getItem(key);
    if (storage){
        storage = JSON.parse(storage);
    }
    return storage;
}


function deleteLocal(key, thisElem){
    // var filtered = someArray.filter(function(el) { return el.Name != "Kristian"; });
    let cartLocal = getFromLocal(key);
    let toDelete = thisElem.data('id');
    let filtered = cartLocal.filter(function (el) {
       return el.id != toDelete;
    });
    saveToLocal(key, filtered);
    // reload the page
    location.reload();
}


function getProductQuantity(cart){
    let quantity = 0;
    if(cart){
        quantity = cart.length;
    }
    return quantity;
}

function getCartTotal(quantity, cart){
    let total = 0;
    if (quantity && cart){
        cart.forEach(function(item){
            total += parseFloat(item.price);
        });
    }
    return total;
}

function isCartPage(currentUrl){
    let currentUrlArr = currentUrl.split("/");
    let check = currentUrlArr[currentUrlArr.length-2];
    check = (check === 'cart') ?  true :  false;
    return check;
}

function isCheckoutPage(currentUrl){
    let currentUrlArr = currentUrl.split("/");
    let check = currentUrlArr[currentUrlArr.length-2];
    check = (check === 'checkout') ?  true :  false;
    return check;
}

function populateCartItems($, domId, cart){
    cart.forEach(function(item){
        let htm = `<tr>
                  <th scope="row"><img src="${item.image}" width="45px"></img></th>
                  <td>${item.name}</td>
                  <td>$${item.price}</td>
                  <td>1</td>
                  <td><button data-id="${item.id}" class="cart-delete btn btn-sm btn-danger">delete</button></td>
                </tr>`;
        $(`#${domId}`).append(htm);
    });
}

function populateCheckoutItems($, domId, cart){
    // let quantity = cart.length;
    cart.forEach(function(item){
        let htm = `<div class="cart-row">
                        <div style="flex:1"><img class="row-image" src="${item.image}" width="45px"></div>
                        <div style="flex:2"><p>${item.name}</p></div>
                        <div style="flex:1"><p>$${item.price}</p></div>
                        <div style="flex:1"><p>x1</p></div>
                    </div>`;
        $(`#${domId}`).append(htm);
    });
}

function populateItemAndTotalElem($, domId, cart){
    let totalItems = cart.length;
    let total = 0;
    cart.forEach(function(item){
        total += parseFloat(item.price);
    });
    let htm = `<h5>Items:   ${totalItems}</h5>
                <h5>Total:   $${total}</h5>`;
    $(`#${domId}`).html(htm);
}

// for sending to backend
function populateCartField($, domId, cart){
    cartArr = [];
    cart.forEach(function(item){
        let itemToSend = {
            id: item.id,
            quantity: 1,
        };
        cartArr.push(itemToSend);
    });
    let cartString = JSON.stringify(cartArr);
    // replace double quotes so the string does not break unexpectedly
    cartString = cartString.replaceAll("\"", "'");
    let htm = `<input name="cart" type="hidden" value="${cartString}">`;
    $(`#${domId}`).html(htm);
}