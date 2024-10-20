

# Rule Engine with Abstract Syntax Tree (AST) Documentation

# Table of Contents
1. Introduction
2. Prerequisites
3. Installation
4. Running the Application
5. Database Setup
6. Using the Application
- Creating a Rule
- Combining Rules
- Evaluating Rules
7. Accessing the Database
8. Using the SQL Dump File
9. Conclusion
  
# Introduction
The Rule Engine application allows users to dynamically create and evaluate rules based on attributes such as age, department, salary, and experience using an Abstract Syntax Tree (AST). This documentation provides guidance on how to set up and use the application, including database interactions.

# Prerequisites
Before you start, ensure you have the following installed:

# Python 3.x
Streamlit: Install via pip
pip install streamlit
MySQL Connector: Install via pip
pip install mysql-connector-python
MySQL Server: Ensure you have MySQL server running locally or remotely.
# Installation
# Clone the repository (if applicable):
git clone https://github.com/Kamal-Rathore/Rule-Engine-with-AST.git

cd Rule-Engine-with-AST

# Install necessary libraries:

pip install -r requirements.txt

Set up MySQL database (if not using Docker or Podman).

# Running the Application
- Open your terminal or command prompt.
- Navigate to the project directory.
- Run the Streamlit application:
- streamlit run main.py
- Open your browser and go to http://localhost:8501.

# Database Setup
# Using Docker or Podman
To run your MySQL database in a Docker or Podman container:
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=rule_engine_db -p 3306:3306 -d mysql:latest
# Manual Setup
Access MySQL Workbench or use command line.
# Create a new database:
- CREATE DATABASE rule_engine_db;
Create the necessary table for storing rules:

CREATE TABLE rules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rule_text VARCHAR(255) NOT NULL,
    ast TEXT NOT NULL
);

# Using the Application
# Creating a Rule
- Enter a rule string in the provided input box (e.g., age > 30 AND department == 'Sales').
- Click on the Create Rule button.
- The generated AST will be displayed, and the rule will be stored in the database.
# Combining Rules
- Enter multiple rules, one per line, in the provided text area.
- Select the operator to combine rules (AND/OR).
- Click the Combine Rules button.
The combined AST will be displayed.
# Evaluating Rules
- Enter user data in JSON format (e.g., {"age": 35, "department": "Sales", "salary": 60000}).
- Click on the Evaluate Rule button.
- The evaluation result will be displayed.
# Accessing the Database
To see the data stored in your database:

- Open MySQL Workbench or your preferred MySQL client.
- Connect to the MySQL server.
- Select the rule_engine_db database.
# Run the query:
- SELECT * FROM rules;
This will display all the stored rules.
# Using the SQL Dump File
To restore or share your database using the .sql file you created:

- Open MySQL Workbench.
- Go to Server in the top menu.
- Select Data Import.
- Choose the option Import from Self-Contained File.
- Select the .sql file you created (e.g., Dump20241020.sql).
- Choose the target database (or create a new one).
- Click Start Import.
This will execute all commands in the .sql file, creating the tables and inserting the data.

# Conclusion
This documentation provides a comprehensive guide on setting up and using the Rule Engine application. By following these steps, users can easily create and evaluate rules based on various attributes, as well as manage the underlying database.
