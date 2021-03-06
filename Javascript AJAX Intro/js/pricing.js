/**
 * Created by Ati on 9/3/15.
 */


    //function getNodeValue(obj, tag) {                   // Gets content from XML
    //    return obj.getElementsByTagName(tag)[0].firstChild.nodeValue;
    //}


/////////////////////////////////////////////////////////////////////
var inventory = document.getElementById("inventory");
var material, price;

var materials = [
    ];

function Product(name, stock, price) {
    this.checked = false;
    this.name = name;
    this.stock = stock;
    this.price = price;

    this.adjustStock = function (num) {
        this.stock -= num;
    };

    this.inStock = function () {
        return this.stock > 0;
    };
}

//populateInventoryDOM();

function populateInventoryDOM() {

    for (var i = 0; i < materials.length; i++) {
        var newProdRow = document.createElement('tr');
        var checkboxcell = document.createElement('td');
        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = materials[i].checked;
        checkboxcell.appendChild(checkbox);
        newProdRow.appendChild(checkboxcell);

        // Name Column
        var nameCol = document.createElement('td');
        var nameText = document.createTextNode(materials[i].name);
        nameCol.appendChild(nameText);
        newProdRow.appendChild(nameCol);

        // Price Column
        var priceCol = document.createElement('td');
        var priceText = document.createTextNode('$' + materials[i].price);
        priceCol.appendChild(priceText);
        newProdRow.appendChild(priceCol);

        // Stock Column
        var stockCol = document.createElement('td');
        stockCol.className = materials[i].inStock();
        var stockText = document.createTextNode(materials[i].stock);
        stockCol.appendChild(stockText);
        newProdRow.appendChild(stockCol);

        inventory.appendChild(newProdRow);
    }
}

function populateInventory() {
    // Loop through materials
    // Add a row for ech line item
    // Make sure that stock class reflects inStock
    // Make sure that checkbox status reflects checked
    var newRow = "";

    for (var i = 0; i < materials.length; i++) {
        newRow = "<tr>";
        newRow += "<td><input type='checkbox'/></td>";
        newRow += "<td>" + materials[i].name + '</td>';
        newRow += '<td>$' + materials[i].price + '</td>';
        //if (materials[i].inStock()) {
        //    newRow += '<td class="true">Yes</td>';
        //}
        //else {
        //    newRow += '<td class="false">No</td>';
        //}
        newRow += '<td>' + materials[i].stock + '</td>';
        newRow += '</tr>';
        inventory.innerHTML += newRow;
        rows = inventory.getElementsByTagName('tr');
        lastCheckboxList = rows[rows.length - 1].getElementsByTagName('input');
        lastCheckboxList[0].checked = materials[i].checked;
    }
}

function checkAll(checkbox) {
    var inputs = inventory.getElementsByTagName('input');
    if (checkbox.checked) {
        for (var i = 0; i < inputs.length; i++) {
            inputs[i].checked = true;
//            inputs[i].setAttribute('checked', '');
        }
    }
    else {
        for (var i = 0; i < inputs.length; i++) {
            inputs[i].checked = false;
//            inputs[i].removeAttribute('checked');
        }
    }
}

function removeStock() {
    var rows = inventory.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs.length > 0) {
            if (inputs[0].type == 'checkbox') {
                if (inputs[0].checked) {
                    var stock = rows[i].lastElementChild;
                    //stock.className = 'false';
                    //stock.textContent = 'No';
                    //inputs[0].checked = false;
                }
            }
        }
    }
}

function addStock() {
    var rows = inventory.getElementsByTagName('tr');
    for (var i = 0; i < rows.length; i++) {
        console.log(rows);
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs.length > 0) {
            if (inputs[0].type == 'checkbox') {
                if (inputs[0].checked) {
                    var stock = rows[i].lastElementChild;
                    console.log(stock.textContent);
                    console.log(materials);
                    newStock = materials[i].stock + 1;
                    materials[i].stock = newStock;
                    stock.innerHTML = '<td>' + newStock.toString() + '</td>';
                    //stock.className = 'true';
                    //stock.textContent = 'Yes';
                    //inputs[0].checked = false;
                }
            }
        }
    }
}

function addNewStock() {

    material = document.getElementById("material").value;
    price = document.getElementById("price").value;

    if (material == "" || price == "" || isNaN(price)) {
        return;
    }

    var newProdRow = document.createElement('tr');
    var checkboxcell = document.createElement('td');
    var checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = false;
    checkboxcell.appendChild(checkbox);
    newProdRow.appendChild(checkboxcell);

    // Name Column
    var nameCol = document.createElement('td');
    var nameText = document.createTextNode(material);
    nameCol.appendChild(nameText);
    newProdRow.appendChild(nameCol);

    // Price Column
    var priceCol = document.createElement('td');
    var priceText = document.createTextNode('$' + price);
    priceCol.appendChild(priceText);
    newProdRow.appendChild(priceCol);

    // Stock Column
    var stockCol = document.createElement('td');
    stockCol.className = true;
    var stockText = document.createTextNode('10');
    stockCol.appendChild(stockText);
    newProdRow.appendChild(stockCol);

    // Clear material input box
    var materialBox = document.getElementById('material');
    materialBox.value = '';

    // Clear price input box
    var priceBox = document.getElementById('price');
    priceBox.value = '';

    // Add new inventory table row to webpage
    inventory.appendChild(newProdRow);

    // Store new inventory item in list
    materials.push(new Product(material, 10, parseInt(price)));

}

// Make AJAX call to get data from server
var xhr = new XMLHttpRequest();     // Create XMLHTTPRequest object

xhr.onload = function () {              // When response has loaded
    // The following conditional check will not work locally - only on a server
    if (xhr.status === 200) {             // If server status was ok

        // THIS PART IS DIFFERENT BECAUSE IT IS PROCESSING XML NOT HTML
        var response = xhr.responseXML;                     // Get XML from the server

        console.log(response);

        var items = response.getElementsByTagName('item'); // Find <item> elements
        console.log(items);
        for (var i = 0; i < items.length; i++) {            // Loop through them
            var product = new Product(
                items[i].getAttribute('name'),
                items[i].getElementsByTagName('numInStock')[0].textContent,
                items[i].getAttribute('price')
            )
            console.log(items[i].getAttribute('name'));
            console.log(items[i].getAttribute('price'));
            console.log(items[i].getElementsByTagName('numInStock')[0].textContent);
            materials.push(product);
        }
        populateInventoryDOM();

    };
    // THE FINAL PART IS THE SAME AS THE HTML EXAMPLE BUT IT REQUESTS AN XML FILE
};

    xhr.open('GET', 'data/stock.xml', true);            // Prepare the request
    xhr.send(null);                                     // Send the request


