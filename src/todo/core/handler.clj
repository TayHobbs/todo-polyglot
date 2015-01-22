(ns todo.core.handler
  (:require [compojure.core :refer :all]
            [compojure.route :as route]
            [ring.middleware.defaults :refer [wrap-defaults site-defaults]]
            [todo.core.models.query-defs :as query]
            [todo.core.routes.todo-routes :refer [todo-routes]]))

(defn init []
  (query/create-todos-table-if-not-exists!))

(defroutes app-routes
  (route/not-found "Not Found"))

(def app
  (-> (routes todo-routes app-routes)
      (wrap-defaults (assoc-in site-defaults [:security :anti-forgery] false))))
