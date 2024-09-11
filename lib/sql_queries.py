# Example query (replace with your queries)
select_all_female_bears_return_name_and_age = """
  SELECT
    bears.name,
    bears.age
  FROM bears
  WHERE sex='F';
"""

# Add similar queries for other tests in select_test.py

# Select all bears' names and order them alphabetically
select_all_bears_names_and_orders_in_alphabetical_order = """
  SELECT
    bears.name
  FROM bears
  ORDER BY name ASC;
"""

# Select names and ages of alive bears, ordered youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
  SELECT
    bears.name,
    bears.age
  FROM bears
  WHERE alive = True
  ORDER BY age ASC;
"""

# Select the oldest bear (by age) and return name and age
select_oldest_bear_and_returns_name_and_age = """
  SELECT
    bears.name,
    bears.age
  FROM bears
  ORDER BY age DESC
  LIMIT 1;
"""

# Select the youngest bear (by age) and return name and age
select_youngest_bear_and_returns_name_and_age = """
  SELECT
    bears.name,
    bears.age
  FROM bears
  ORDER BY age ASC
  LIMIT 1;
"""