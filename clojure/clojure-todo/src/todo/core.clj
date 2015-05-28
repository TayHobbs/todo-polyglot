(ns todo.core)

(def todos (atom {0 {}}))

(defn add-todo []
  (let [todo (read-line)]
    (swap! todos assoc 1 {:name todo :completed false} )))

(defn -main [& args]
  (add-todo)
  (println @todos))