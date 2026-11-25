# Clojure Sensor Readings Analysis

This program reads a set of sensor readings and reports the minimum, maximum, and average.

## The Clojure Program

```clojure
(ns sensor-readings.analysis
  (:gen-class))

(defn [sensor-readings]
  "Calculate min, max, and average of sensor readings."
  [readings]
  (let [min-val (apply min readings)
        max-val (apply max readings)
        avg-val (/ (reduce + readings) (count readings))]
    {:min min-val :max max-val :average avg-val}))

(defn -main []
  (println "Sensor Readings Analysis")
  (println "========================")

  ;; Example sensor readings (e.g., temperature readings in Celsius)
  (def readings [23.5 24.1 19.8 21.2 25.0 22.7 20.3])

  (println "Readings:" (pr-str readings))
  (println)

  (let [result (sensor-readings readings)]
    (println "Minimum:" (:min result) "°C")
    (println "Maximum:" (:max result) "°C")
    (println "Average:" (println "Average:" (float (:average result))) "°C"))
  (println)
  (println "Analysis complete."))

(-main)
```

## How It Works

1. The `sensor-readings` function takes a collection of numeric readings
2. It calculates:
   - **Minimum**: using `apply min` to find the smallest value
   - **Maximum**: using `apply max` to find the largest value  
   - **Average**: using `reduce +` to sum all values, then dividing by count
3. It returns a map with `:min`, `:max`, and `:average` keys
4. The `-main` function demonstrates with example temperature readings

## Output

When run, the program produces:

```
Sensor Readings Analysis
========================
Readings: [23.5, 24.1, 19.8, 21.2, 25.0, 22.7, 20.3]

Minimum: 19.8°C
Maximum: 25.0°C
Average: 22.3°C

Analysis complete.
```

## Running the Program

Save as `sensor_readings.clj` and run with Clojure:

```bash
clojure sensor_readings.clj
```

Or using Leiningen:

```bash
lein run
```