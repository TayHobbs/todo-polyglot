(ns todo.core.routes.todo-routes
  (:require [compojure.core :refer [defroutes GET POST]]
            [todo.core.views.todo-layout :refer [common-layout]]))

(defn index [request]
  (common-layout))

(defn add-todo [request]
  (let [posted (get-in request [:params :todo])]
    (common-layout
      (str "You submitted: " posted))))

(defroutes todo-routes
  (GET "/"          [] index)
  (POST "/add-todo" [] add-todo))
