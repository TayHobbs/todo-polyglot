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

(defn delete-todo []
  (println (newline) "Which todo would you like to delete? (Enter the id)")
  (let [input (read-line)]
    (swap! todos dissoc (read-string input))
    (next-action)))

(defn complete-todo []
  (println (newline) "Which todo would you like to complete/incomplete? (Enter the id)")
  (let [input (read-line)]
    (let [todo (@todos (read-string input))]
      (swap! todos dissoc (read-string input))
      (swap! todos assoc (read-string input) {:name (todo :name) :completed (not (todo :completed))})))
  (next-action))

(defn next-action []
  (println "----------------------------")
  (println "Current Todos: " @todos)
  (println "----------------------------")
  (println (newline) "What would you like to do now?")
  (println "Add new Todo - 'add'; Delete todo - 'delete'; Mark todo complete/incomplete - 'complete'; Quit - 'q'")
  (let [input (.toLowerCase (read-line))]
    (if (= "add" input)
      (add-todo)
      (if (= "delete" input)
        (delete-todo)
        (if (= "complete" input)
          (complete-todo))))))

(defn -main [& args]
    (next-action))
