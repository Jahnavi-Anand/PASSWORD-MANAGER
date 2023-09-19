// index.js

const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const app = express();
const port = process.env.PORT || 5500; 

// Create a MySQL connection
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'ROOT',
    database: 'password_manager',
});

// Connect to the database
db.connect(err => {
    if (err) {
        console.error('Database connection failed: ' + err.stack);
        return;
    }
    console.log('Connected to the database');
});

// Middleware to parse JSON
app.use(bodyParser.json());

// Define API endpoints for CRUD operations (Create, Read, Update, Delete)

// Example: Get all password entries
app.get('/api/passwords', (req, res) => {
    const sql = 'SELECT * FROM passwords';
    db.query(sql, (err, results) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json({ passwords: results });
    });
});

// Add more endpoints for CRUD operations as needed
// Function to create a new password entry
function createPasswordEntry(platform, username, password) {
    fetch('/api/passwords', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ platform, username, password }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error creating password entry');
            }
            return response.json();
        })
        .then(data => {
            // Handle successful creation (e.g., display a success message)
            console.log('Password entry created:', data);
            displayPasswordEntries();
        })
        .catch(error => console.error('Error creating password entry:', error));
}

// Function to update an existing password entry
function updatePasswordEntry(id, platform, username, password) {
    fetch(`/api/passwords/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ platform, username, password }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error updating password entry');
            }
            return response.json();
        })
        .then(data => {
            // Handle successful update (e.g., display a success message)
            console.log('Password entry updated:', data);
            displayPasswordEntries();
        })
        .catch(error => console.error('Error updating password entry:', error));
}

// Function to delete an existing password entry
function deletePasswordEntry(id) {
    fetch(`/api/passwords/${id}`, {
        method: 'DELETE',
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error deleting password entry');
            }
            return response.json();
        })
        .then(data => {
            // Handle successful deletion (e.g., display a success message)
            console.log('Password entry deleted:', data);
            displayPasswordEntries();
        })
        .catch(error => console.error('Error deleting password entry:', error));
}

// Example: Add event listeners for create, update, and delete actions

// Event listener for creating a new password entry
document.getElementById('create-button').addEventListener('click', function () {
    const platform = prompt('Enter the platform:');
    const username = prompt('Enter the username/email:');
    const password = prompt('Enter the password:');
    
    if (platform && username && password) {
        createPasswordEntry(platform, username, password);
    } else {
        // Handle invalid input or cancellation
    }
});

// Event listener for updating an existing password entry (assuming you have a UI for selecting an entry to update)
document.getElementById('update-button').addEventListener('click', function () {
    const id = prompt('Enter the ID of the entry to update:');
    const platform = prompt('Enter the updated platform:');
    const username = prompt('Enter the updated username/email:');
    const password = prompt('Enter the updated password:');
    
    if (id && platform && username && password) {
        updatePasswordEntry(id, platform, username, password);
    } else {
        // Handle invalid input or cancellation
    }
});

// Event listener for deleting an existing password entry (assuming you have a UI for selecting an entry to delete)
document.getElementById('delete-button').addEventListener('click', function () {
    const id = prompt('Enter the ID of the entry to delete:');
    
    if (id) {
        deletePasswordEntry(id);
    } else {
        // Handle invalid input or cancellation
    }
});
// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
