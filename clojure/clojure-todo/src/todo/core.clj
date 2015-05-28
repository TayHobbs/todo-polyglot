(ns todo.core)

(def todos (atom [{:id 0}]))

(defn next-id []
  (inc ((apply max-key :id @todos) :id)))

(defn -main [& args])