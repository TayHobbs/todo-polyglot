(ns todo.core)

(def next-id (atom 1))
(def todos (atom {}))
(defn next-action [])

(defn add-todo []
  (println "Enter Todo Name")
  (let [todo (read-line)]
    (swap! todos assoc @next-id {:name todo :completed false} ))
  (swap! next-id inc)
  (next-action))

(defn next-action []
  (println "----------------------------")
  (println "Current Todos: " (seq @todos))
  (println "What would you like to do now?")
  (println "Add new Todo - 'add'; Quit - q")
  (let [input (.toLowerCase (read-line))]
    (if (= "add" input)
      (add-todo))))

(defn -main [& args]
    (next-action))