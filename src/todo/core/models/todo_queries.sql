-- name: all-todos
-- Selects all todos
SELECT * FROM todos;

-- name: insert-todo
-- Adds a todo
INSERT INTO todos (name)
    VALUES (:name);
