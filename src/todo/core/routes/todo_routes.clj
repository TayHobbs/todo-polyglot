(ns todo.core.routes.todo-routes
  (:require [compojure.core :refer [defroutes GET POST]]))


(defn add-todo [request]
  (let [posted (get-in request [:params :todo])]
    (str "You submitted: " posted)))

(defroutes todo-routes
  (GET "/" [] "TODO")
  (POST "/add-todo" [] add-todo))
