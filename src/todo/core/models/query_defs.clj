(ns todo.core.models.query-defs
  (:require [environ.core :refer [env]]
            [yesql.core :refer [defqueries]]))

(defqueries "todo/core/models/todo_queries.sql" {:connection (env :database-url)})
