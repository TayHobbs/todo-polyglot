(ns todo.core.todo-tests
  (:use midje.sweet)
  (:require [clojure.test :refer :all]
            [ring.mock.request :as mock]
            [todo.core.handler :refer :all]))

(facts "GET and POST tests"

  (fact "Test GET"
    (let [response (app (mock/request :get "/"))]
      (:status response) => 200
      (:body response) => "TODO"))

  (fact "Test POST"
    (let [response (app (mock/request :post "/add-todo" {:todo "TODO"}))]
      (:status response) => 200
      (:body response) => "You submitted: TODO"))

  (testing "Invalid Route"
    (let [response (app (mock/request :get "/invalid"))]
      (:status response) => 404)))
