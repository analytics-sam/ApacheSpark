# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS club (
# MAGIC   club_id VARCHAR(10),
# MAGIC   club_name VARCHAR(50)
# MAGIC );
# MAGIC 
# MAGIC 
# MAGIC CREATE TABLE IF NOT EXISTS department (
# MAGIC   dept_id VARCHAR(10),
# MAGIC   dept_name VARCHAR(50)
# MAGIC );
# MAGIC 
# MAGIC CREATE TABLE IF NOT EXISTS employee
# MAGIC (
# MAGIC   empcode VARCHAR(10),
# MAGIC   firstname VARCHAR(50),
# MAGIC   lastname VARCHAR(50),
# MAGIC   dept_id VARCHAR(10),
# MAGIC   club_id VARCHAR(10)
# MAGIC );
# MAGIC 
# MAGIC CREATE TABLE meal
# MAGIC (
# MAGIC   meal_id VARCHAR(10),
# MAGIC   meal_name VARCHAR(50)
# MAGIC );
# MAGIC CREATE TABLE drink
# MAGIC (
# MAGIC   drink_id VARCHAR(10),
# MAGIC   drink_name VARCHAR(50)
# MAGIC );

# COMMAND ----------

# MAGIC %python
# MAGIC print('Preparing tables...')
# MAGIC print('Success: table club created')
# MAGIC print('Success: table department created')
# MAGIC print('Success: table employee created')
# MAGIC print('Success: table meal created')
# MAGIC print('Success: table drink created')

# COMMAND ----------

# MAGIC %sql
# MAGIC TRUNCATE TABLE club;
# MAGIC TRUNCATE TABLE department;
# MAGIC TRUNCATE TABLE employee;
# MAGIC TRUNCATE TABLE meal;
# MAGIC TRUNCATE TABLE drink;

# COMMAND ----------

# MAGIC %python
# MAGIC print('Success: table club truncated')
# MAGIC print('Success: table department truncated')
# MAGIC print('Success: table employee truncated')
# MAGIC print('Success: table meal truncated')
# MAGIC print('Success: table drink truncated')

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO club
# MAGIC (club_id, club_name)
# MAGIC VALUES
# MAGIC ('C1', 'Cricket'),
# MAGIC ('C2', 'Football'),
# MAGIC ('C3', 'Golf'),
# MAGIC ('C4', 'Wildlife & Nature'),
# MAGIC ('C5', 'Photography'),
# MAGIC ('C6', 'Art & Music');
# MAGIC 
# MAGIC INSERT INTO department
# MAGIC (dept_id, dept_name)
# MAGIC VALUES
# MAGIC ('DEP001', 'IT'),
# MAGIC ('DEP002', 'Marketing'),
# MAGIC ('DEP003', 'Finance'),
# MAGIC ('DEP004', 'BI'),
# MAGIC ('DEP005', 'Admin'),
# MAGIC ('DEP006', 'HR');
# MAGIC 
# MAGIC INSERT INTO employee
# MAGIC (empcode, firstname, lastname, dept_id, club_id)
# MAGIC VALUES
# MAGIC ('EMP001', 'Albert', 'Einstein', 'DEP001', 'C1'),
# MAGIC ('EMP002', 'Isaac', 'Newton', 'DEP001', 'C1'),
# MAGIC ('EMP003', 'Elvis', 'Bose', 'DEP001', 'C2'),
# MAGIC ('EMP004', 'Jose', 'Baldwin', 'DEP001', 'C3'),
# MAGIC ('EMP005', 'Christian', 'Baldwin', 'DEP002', 'C1'),
# MAGIC ('EMP006', 'Stephenie', 'Margarete', 'DEP002', 'C3'),
# MAGIC ('EMP007', 'P.K', 'Chand', 'DEP003', 'C1'),
# MAGIC ('EMP008', 'Eric', 'Clapton', 'DEP004', 'C6'),
# MAGIC ('EMP009', 'Eric', 'Jhonson', 'DEP001', 'C9'),
# MAGIC ('EMP010', 'Martand', 'Singh', 'DEP010', 'C3'),
# MAGIC ('EMP011', 'Rajiv', 'Singh', 'DEP0010', 'C31'),
# MAGIC ('EMP012', 'Jose', 'Peter', 'DEP0011', 'C1');

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC INSERT INTO meal
# MAGIC (meal_id, meal_name)
# MAGIC VALUES
# MAGIC ('M001', 'Pizza'),
# MAGIC ('M002', 'Burger'),
# MAGIC ('M003', 'Sandwich'),
# MAGIC ('M004', 'Pasta');
# MAGIC 
# MAGIC INSERT INTO drink
# MAGIC (drink_id, drink_name)
# MAGIC VALUES
# MAGIC ('D001', 'Coke'),
# MAGIC ('D002', 'Pepsi'),
# MAGIC ('D003', 'Beer'),
# MAGIC ('D004', 'Water');

# COMMAND ----------

print('Success: demo tables are ready.')
