# DBT Basics with Python

This repo is a lightweight intro to **dbt (data build tool)** concepts using Python.  
Instead of complex warehouse configs, we’ll keep it simple with **pandas DataFrames** to mimic how dbt models transform data.

## What’s inside
- 📂 Python scripts showing how dbt works conceptually
- 🗂️ DataFrames as sources, staging, and final models
- 🧪 Simple tests and validations
- 📊 Example transformations

## Why this repo
dbt is usually tied to big data warehouses (Snowflake, Redshift, BigQuery, Postgres). But before all that, it helps to understand the **core idea**:  
➡️ You define transformations in code (SQL in dbt, Python here).  
➡️ dbt builds a dependency graph (lineage).  
➡️ Each model is reproducible and testable.
