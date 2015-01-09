(ns todo.core.views.todo-layout
  (:require [hiccup.page :refer [html5 include-css]]
           [hiccup.core :refer [html h]]))


(defn common-layout [& body]
  (html5
  [:head
   [:title "Todo"]
   (include-css "/css/todo.css")
   (include-css "//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css")]
  [:body
   [:div.content
    [:div.row
     [:div.col-lg-12
      [:h1 "Todo"]
  body]]]]))

