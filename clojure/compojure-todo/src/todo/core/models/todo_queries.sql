-- name: all-todos
-- Selects all todos
SELECT id
       ,name
FROM todos;

-- name: insert-todos<!
-- Queries a single todos
INSERT INTO todos (name)
    VALUES (:name);

-- name: drop-todos-table!
-- drop the todos table
DROP TABLE todos;

-- name: create-todos-table-if-not-exists!
-- create the todos table if it does not exist
CREATE TABLE IF NOT EXISTS todos (
   id serial PRIMARY KEY,
   name VARCHAR (20) NOT NULL);

-- name: update-todos<!
-- Update a single todos
UPDATE todos SET name = :name
    WHERE id = :id;

-- name: delete-todos<!
-- Deletes a single todos
DELETE FROM todos
    WHERE id = :id;
