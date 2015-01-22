(ns todo.core.todo-tests
  (:use midje.sweet)
  (:require [clojure.test :refer :all]
            [ring.mock.request :as mock]
            [todo.core.handler :refer :all]
            [todo.core.models.query-defs :as query]))

(facts "Example GET and POST tests"
  (with-state-changes [(before :facts (query/create-todos-table-if-not-exists!))
                       (after  :facts (query/drop-todos-table!))]

  (fact "Test GET"
    (query/insert-todos<! {:name "Todo"})
    (let [response (app (mock/request :get "/"))]
      (:status response) => 200
      (:body response) => (contains "Todo")))

  (fact "Test POST"
    (count (query/all-todos)) => 0
    (let [response (app (mock/request :post "/add-todo" {:todo "Todo"}))]
      (:status response) => 302
      (count (query/all-todos)) => 1))))
