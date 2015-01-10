(ns todo.core.views.todo-layout
  (:require [hiccup.page :refer [html5 include-css]]
           [hiccup.core :refer [html h]]))


(defn common-layout [& body]
  (html5
  [:head
   [:title "Todo"]
   (include-css "/css/todo.css")]
  [:body
   [:div#todoapp
     [:div#header
      [:h1 "Todo"]]
        [:form {:action "/add-todo" :method "post"}
        [:input#new-todo {:type "text" :name "todo" :placeholder "Todo"}]
         [:button#hide-button {:type "submit"} "Add Todo"]
  body]]]))
