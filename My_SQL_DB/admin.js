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
    ask();
});

// Inquirer prompt to ask the user which command
function ask() {
    inquirer
        .prompt({
            name: "action",
            type: "list",
            message: "What would you like to do?",
            choices: [
                "View Products for Sale",
                "View Low Inventory",
                "Add to Inventory",
                "Add New Product",
                "Exit"
            ]
        })
        .then(function(answer) {
            // Switch case to call specific command functions
            switch (answer.action) {
                case "View Products for Sale":
                    viewProducts();
                    break;

                case "View Low Inventory":
                    lowInventory();
                    break;

                case "Add to Inventory":
                    addInventory();
                    break;

                case "Add New Product":
                    addProduct();
                    break;

                case "Exit":
                    connection.end();
                    break;
            }
        });
};

// Function to display inventory and info
function viewProducts() {
    // MySQL SELECT call to get the columns associated with the item info
    connection.query(
        "SELECT item_id, item_name, price, stock_quantity FROM products",
        function(err, res) {
            if (err) throw err;
            else {
                console.log("\n");
                for (i = 0; i < res.length; i++) {
                    console.log(res[i].item_id + ") " + res[i].item_name + " | $" + res[i].price + " | " + res[i].stock_quantity);
                }
                console.log("\n");
                ask();
            }
        }
    );
};

// Function to display items that have a quantity lower than 5
function lowInventory() {
    console.log("The following items have a quantity lower than 5:\n");
    connection.query(
        // MySQL SELECT call to get the items with quantity lower than 5
        "SELECT item_name, stock_quantity FROM products WHERE stock_quantity < 5",
        function(err, res) {
            if (err) throw err;
            else {
                // If no items have a quantity lower than 5, display 'None'
                if (res.length == 0) {
                    console.log("None.\n");
                    ask();
                }
                // Otherwise, display the items
                else {
                    for (i = 0; i < res.length; i++) {
                        console.log(res[i].item_name + " | " + res[i].stock_quantity);
                    }
                    console.log("\n");
                    ask();
                }
            }
        }
    );
};

// Function to add more quantity to an item in the inventory
function addInventory() {
    // Make an array to store each items quantities
    var quants = [];
    // MySQL SELECT call to display all items
    connection.query(
        "SELECT item_id, item_name, stock_quantity FROM products",
        function(err, res) {
            if (err) throw err;
            else {
                numItems = res.length;
                for (i = 0; i < numItems; i++) {
                    console.log(res[i].item_id + " | " + res[i].item_name + " | " + res[i].stock_quantity);
                    quants.push(parseInt(res[i].stock_quantity));
                }
                console.log("\n");
                // Inquirer prompt to ask ID for item to add quantity to
                inquirer.prompt({
                    name: "id",
                    type: "input",
                    message: "Please give the ID of the item you want to add quantity to:",
                    validate: function(value) {
                        if (isNaN(value) === false) {
                            return true;
                        }
                        return false;
                    }
                }).then(function(answer1) {
                    // Validate ID input
                    if (answer1.id < 0 || answer1.id > numItems) {
                        console.log("\nPlease give a proper input.\n");
                        ask();
                    } else {
                        // Inquirer prompt to ask the quantity to add
                        inquirer.prompt({
                            name: "quantity",
                            type: "input",
                            message: "Please give the quantity you want to add:",
                            validate: function(value) {
                                if (isNaN(value) === false) {
                                    return true;
                                }
                                return false;
                            }
                        }).then(function(answer2) {
                            // MySQL UPDATE call to update the stock quantity
                            connection.query(
                                "UPDATE products SET ? WHERE ?", [{ stock_quantity: parseInt(answer2.quantity) + quants[answer1.id - 1] }, { item_id: answer1.id }],
                                function(err, res) {
                                    if (err) throw err;
                                    else {
                                        console.log("\nQuantity updated!\n");
                                        ask();
                                    }
                                }
                            );
                        });
                    }
                });
            }
        }
    );
};

// Function to add a new product to the inventory
function addProduct() {
    console.log("\nPlease enter the information of the product you want to add:\n");
    // Inquirer prompt to ask the Name, Department, Price, and Quantity of the new item to add
    inquirer.prompt(
        [{
                name: "name",
                type: "input",
                message: "Name of the product:",
            },
            {
                name: "dept",
                type: "input",
                message: "Department of the product:",
            },
            {
                name: "price",
                type: "input",
                message: "Price of the product:",
                validate: function(value) {
                    if (isNaN(value) === false) {
                        return true;
                    }
                    return false;
                }
            },
            {
                name: "quantity",
                type: "input",
                message: "Quantity of the product:",
                validate: function(value) {
                    if (isNaN(value) === false) {
                        return true;
                    }
                    return false;
                }
            }
        ]
    ).then(function(answer) {
        // Validate the price of the item
        if (parseInt(answer.price < 0.01)) {
            console.log("\nPlease enter a valid price for the product.\n");
            addProduct();
        }
        // Validate the quantity to add to the inventory
        else if (parseInt(answer.quantity) < 0) {
            console.log("\nPlease enter a valid quantity for the product.\n");
            addProduct();
        } else {
            // MySQL INSERT INTO call to add a new item entry to the database table
            connection.query(
                "INSERT INTO products (item_name, department_name, price, stock_quantity) VALUES ('" + answer.name + "', '" + answer.dept + "', " + answer.price + ", " + answer.quantity + ");",
                function(err, res) {
                    if (err) throw err;
                    else {
                        console.log("\nProduct added successfully!\n");
                        ask();
                    }
                }
            )
        }
    });
};