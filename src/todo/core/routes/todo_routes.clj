(ns todo.core.routes.todo-routes
  (:require [ring.util.response          :as response]
            [compojure.core              :refer [defroutes GET POST]]
            [todo.core.views.todo-layout :refer [common-layout
                                                 read-todo]]
            [todo.core.models.query-defs :as query]))

(defn index [request]
  (common-layout
    (for [todo (query/all-todos)]
      (read-todo todo))))

(defn add-todo [request]
  (let [todo (get-in request [:params :todo])]
    (query/insert-todos<! {:name todo})
      (response/redirect "/")))

(defroutes todo-routes
  (GET  "/"         [] index)
  (POST "/add-todo" [] add-todo))
