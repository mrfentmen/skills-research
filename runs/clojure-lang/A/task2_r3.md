# Clojure Sensor Readings Analysis

A Clojure program that reads a set of sensor readings and reports the minimum, maximum, and average.

## The Program

```clojure
;; sensor-readings.clj

(defn calculate-stats [readings]
  "Calculate min, max, and average of a collection of sensor readings."
  (let [min-val (apply min readings)
        max-val (apply max readings)
        avg-val (/ (reduce + readings) (count readings))]
    {:min min-val :max max-val :average avg-val}))

(defn -main []
  (println "Sensor Readings Analysis")
  (println "========================")

  ;; Example sensor readings (e.g., temperature readings in Celsius)
  (def readings [23.5 24.1 22.8 25.3 21.9 24.7 23.2])

  (println "Readings:" (pr-str readings))
  (println)

  (let [stats (calculate-stats readings)]
    (println "Minimum:" (:min stats))
    (println "Maximum:" (:max stats))
    (println "Average:" (:average stats))))

;; Run the main function
(-main)
```

## How It Works

1. **`calculate-stats`** function takes a collection of readings and returns a map with `:min`, `:max`, and `:average` keys.
2. **`-main`** function defines example sensor readings and calls `calculate-stats`, then prints the results.
3. The program uses core Clojure functions: `min`, `max`, `apply`, `reduce`, and `count`.

## Example Output

```
Sensor Readings Analysis
========================

Readings: [23.5, 24.1, 22.8, 25.3, 21.9, 24.7, 23.2]

Minimum: 21.9
Maximum: 25.3
Average: 23.757142857142858
```

## Running the Program

Save as `sensor-readings.clj` and run with Clojure:

```bash
clojure sensor-readings.clj
```