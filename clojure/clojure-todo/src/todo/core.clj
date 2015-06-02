(ns todo.core)

(def next-id (atom 1))

(def todos (atom {}))

(declare next-action)

(defn add-todo []
  (println "Enter Todo Name")
  (let [todo (read-line)]
    (swap! todos assoc @next-id {:name todo :completed false}))
  (swap! next-id inc)
  (next-action))

(defn next-action []
  (println "----------------------------")
  (println "Current Todos: " @todos)
  (println "----------------------------")
  (println (newline) "What would you like to do now?")
  (println "Add new Todo - 'add'; Delete todo - 'delete'; Quit - 'q'")
  (let [input (.toLowerCase (read-line))]
    (if (= "add" input)
      (add-todo))))

(defn -main [& args]
    (next-action))