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
   [:div.container
    [:div.row
     [:div.col-lg-12
      [:h1 "Todo"]]
      [:div.row
       [:div.col-sm-3
        [:form {:action "/add-todo" :method "post"}
        [:input.form-control {:type "text" :name "todo" :placeholder "Todo"}]
         [:button.btn.btn-primary {:type "submit"} "Add Todo"]
  body]]]]]]))
