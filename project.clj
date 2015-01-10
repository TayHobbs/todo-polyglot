(defproject todo "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :min-lein-version "2.5.0"

  :ring {:handler todo.core.handler/app}

  :dependencies   [[org.clojure/clojure   "1.6.0"]
                   [compojure             "1.2.0"]
                   [ring/ring-defaults    "0.1.2"]
                   [hiccup                "1.0.5"]
                   [org.clojure/java.jdbc "0.3.5"]
                   [postgresql/postgresql "9.1-901-1.jdbc4"]
                   [yesql                 "0.5.0-beta2"]
                   [environ               "1.0.0"]]

  :plugins        [[lein-ring             "0.8.13"]
                   [lein-environ          "1.0.0"]]

  :profiles {:test-local {:dependencies [[midje                     "1.6.3"]
                                         [javax.servlet/servlet-api "2.5"]
                                         [ring-mock                 "0.1.5"]]

                           :plugins     [[lein-midje                "3.1.3"]]}

             ;; Set these in ./profiles.clj
             :test-env-vars {}
             :dev-env-vars  {}

             :test [:test-local :test-env-vars]
             :dev  [:dev-env-vars]})
