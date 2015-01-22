(ns todo.core.handler
  (:require [compojure.route              :as route]
            [todo.core.models.query-defs  :as query]
            [compojure.core               :refer :all]
            [todo.core.routes.todo-routes :refer [todo-routes]]
            [ring.middleware.defaults     :refer [wrap-defaults
                                                  site-defaults]]))

(defn init []
  (query/create-todos-table-if-not-exists!))

(defroutes app-routes
  (route/not-found "Not Found"))

(def app
  (-> (routes todo-routes app-routes)
      (wrap-defaults (assoc-in site-defaults [:security :anti-forgery] false))))
