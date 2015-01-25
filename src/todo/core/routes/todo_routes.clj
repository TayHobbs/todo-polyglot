(ns todo.core.routes.todo-routes
  (:require [ring.util.response          :as response]
            [todo.core.models.query-defs :as query]
            [compojure.core              :refer [defroutes GET POST]]
            [todo.core.views.todo-layout :refer [common-layout
                                                 read-todo]]))

(defn index [request]
  (common-layout
    (for [todo (reverse (query/all-todos))]
      (read-todo todo))))

(defn add-todo [request]
  (let [todo (get-in request [:params :todo])]
    (query/insert-todos<! {:name todo})
      (response/redirect "/")))

(defn edit-todo [request]
  (let [id   (get-in request [:params :id])
        name (get-in request [:params :todo])]
    (query/update-todos<! {:name name :id (Integer. id)})
    (response/redirect "/")))

(defn delete-todo [request]
  (let [id (get-in request [:params :id])]
    (query/delete-todos<! {:id (Integer. id)})
    (response/redirect "/")))

(defroutes todo-routes
  (GET  "/"                     [] index)
  (POST "/add-todo"             [] add-todo)
  (GET  "/edit-todo/:todo-id"   [] index)
  (POST "/edit-todo/:todo-id"   [] edit-todo)
  (POST "/delete-todo/:todo-id" [] delete-todo))
