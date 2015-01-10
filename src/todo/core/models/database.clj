(ns todo.core.models.database
  (:require [environ.core :refer [env]]))

(def database {:subprotocol "postgresql"
               :subname     (env :database-url)
               :user        (env :database-user)
               :password    (env :database-password)})
