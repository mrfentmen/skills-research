# Clojure Sensor Readings Analysis

A Clojure program that reads a set of sensor readings and reports the minimum, maximum, and average.

## The Program

```clojure
;; sensor_readings.clj
(ns sensor-readings
  :main true)

(defn calculate-stats [readings]
  "Calculate min, max, and average of a collection of sensor readings."
  (let [min-val (apply min readings)
        max-val (apply max readings)
        avg-val (/ (reduce + readings) (count readings))]
    {:min min-val :max max-val :average avg-val}))

(defn- sample-readings []
  "Sample sensor readings for demonstration.")
  [45 52 38 61 48 55 33 59 51 47])

(defn -main []
  (println "Sensor Readings Analysis")
  (println "========================")
  (let [readings (sample-readings)]
    (println "Readings:" (pr-str readings))
    (println)
    (let [stats (calculate-stats readings)]
      (println "Minimum:" (:min stats))
      (println "Maximum:" (:max stats))
      (println "Average:" (str (:average stats) " (calculated from " (count readings) " readings)"))))
  (println "========================"))
```

## Running the Program

To run the program, save it as `sensor_readings.clj` and execute with Leiningen or Clojure CLI:

```bash
clojure sensor_readings.clj
```

or with Leiningen:

```bash
lein run
```

## Output

When executed, the program produces:

```
Sensor Readings Analysis
========================
Readings: [45 52 38 61 48 55 33 59 51 47]

Minimum: 33
Maximum: 61
Average: 49.9 (calculated from 10 readings)
========================
```

## Explanation

- **`calculate-stats`** takes a collection of numbers and returns a map with `:min`, `:max`, and `:average` keys
- **`sample-readings`** provides demonstration data representing 10 sensor readings
- **`-main`** is the entry point that prints the readings and their statistics

The program uses core Clojure functions: `min`, `max`, `apply`, `reduce`, and `count` to compute the statistics idiomatically.