(ns todo.core)

(def next-id (atom 1))
(def todos (atom {}))

(defn add-todo []
  (let [todo (read-line)]
    (swap! todos assoc @next-id {:name todo :completed false} ))
  (swap! next-id inc))

(defn -main [& args]
  (add-todo)
  (println @todos)
  (add-todo)
  (println @todos))