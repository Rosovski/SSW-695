var mysql = require("mysql");
var inquirer = require("inquirer");
var numItems;

// Initialize MySQL connection
var connection = mysql.createConnection({
    host: "localhost",

    // Your port; if not 3306
    port: 3306,

    // Your username
    user: "root",

    // Your password
    password: "",
    database: "local_DB"
});

// Start the MySQL connection
connection.connect(function(err) {
    if (err) throw err;
    runStore();
});

// Function to display the customer-facing store items
function runStore() {
    connection.query(
        "SELECT item_id, item_name, price FROM products;",

        // logic to pull out and print out the item id, name nd price
        function(err, res) {
            if (err) throw err;
            else {
                numItems = res.length;
                for (i = 0; i < res.length; i++) {
                    console.log(res[i].item_id + ") " + res[i].item_name + " | $" + res[i].price);
                }
                console.log("\n0) Exit\n");
                ask();
            }
        }
    )
};

// Inquirer prompt to ask customer for info on item to purchase
function ask() {
    inquirer
    // Ask item to purchase
        .prompt({
            name: "id",
            type: "input",
            message: "Please give the ID of the item you would like to purchase:",
            validate: function(value) {
                if (isNaN(value) === false) {
                    return true;
                }
                return false;
            }
        })
        .then(function(answer1) {
            // Validate the input
            if (answer1.id < 0 || answer1.id > numItems) {
                console.log("\nPlease give a proper input.\n");
                runStore();
            }
            // Exit program if 0 selected
            else if (answer1.id == 0) {
                connection.end();
            }
            // Ask quantity of item to purchase
            else {
                inquirer.prompt({
                        name: "quantity",
                        type: "input",
                        message: "How many of this item would you like to purchase:",
                        validate: function(value) {
                            if (isNaN(value) === false) {
                                return true;
                            }
                            return false;
                        }
                    })
                    .then(function(answer2) {
                        // MySQL SELECT call for item that matches the ID
                        connection.query(
                            "SELECT * FROM products WHERE ?", { item_id: answer1.id },
                            function(err, res) {
                                if (err) throw err;
                                else {
                                    // Validate the quantity input
                                    if (res[0].stock_quantity < parseInt(answer2.quantity)) {
                                        console.log("\nInsufficient quantity. Please order an smaller amount.\n");
                                        runStore(ask);
                                    } else {
                                        var total = parseInt(answer2.quantity) * res[0].price;
                                        // MySQL UPDATE call to update inventory and product sales of the item
                                        connection.query(
                                            "UPDATE products SET ? WHERE ?", [{
                                                    stock_quantity: res[0].stock_quantity - parseInt(answer2.quantity),
                                                    product_sales: total
                                                },
                                                {
                                                    item_id: answer1.id
                                                }
                                            ],
                                            function(err, res) {
                                                if (err) throw err;
                                                // Display the total cost for the purchased items
                                                else {
                                                    console.log("\nThe total cost for your order is $" + total.toFixed(2) + ".\n\nWould you like to order more?\n");
                                                }
                                            }
                                        );
                                        // Call the runStore function again
                                        runStore(ask);
                                    }
                                }
                            }
                        )
                    });
            }
        });
};