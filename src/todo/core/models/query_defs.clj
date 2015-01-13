(ns todo.core.models.query-defs
  (:require [todo.core.models.database :refer [database]]
            [yesql.core :refer [defqueries]]))

(defqueries "todo/core/models/todo_queries.sql" {:connection database})
