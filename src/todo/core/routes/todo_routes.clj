(ns todo.core.routes.todo-routes
  (:require [ring.util.response          :as response]
            [compojure.core              :refer [defroutes GET POST]]
            [todo.core.models.query-defs :as query]
            [todo.core.views.todo-layout :refer [common-layout]]))

(defn index [request]
  (common-layout))

(defn add-todo [request]
  (let [todo (get-in request [:params :todo])]
    (query/insert-todo {:name todo}
      (response/redirect "/"))))

(defroutes todo-routes
  (GET  "/"         [] index)
  (POST "/add-todo" [] add-todo))
