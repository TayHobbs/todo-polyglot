(ns todo.core.views.todo-layout
  (:require [hiccup.core :refer [html h]]
            [hiccup.page :refer [html5
                                 include-css]]))


(defn common-layout [& body]
  (html5
  [:head
   [:title "Todo"]
   (include-css "/css/node_modules/todomvc-app-css/index.css")]
  [:body
   [:div#todoapp
     [:div#header
      [:h1 "Todo"]]
        [:form {:action "/add-todo" :method "post"}
        [:input#new-todo {:type "text" :name "todo" :placeholder "Todo"}]
         [:button#hide-button {:type "submit"} "Add Todo"]]
  body]]))

(defn read-todo [todo]
  (html
    [:div.todo
      [:div.todo-text
       [:form {:action (str "/edit-todo/" (:id todo)) :method "post"}
        [:input {:type "hidden" :name "id" :value (h (:id todo))}]
        [:input {:type "text" :name "todo" :value (h (:name todo))}]
        [:button {:type "Submit"} "Update"]]]
       [:form {:action (str "/delete-todo/" (:id todo)) :method "post"}
        [:input {:type "hidden" :name "id" :value (h (:id todo))}]
        [:button {:type "Submit"} "Delete"]]
      [:div.clear-row]]))
