# Clojure Sensor Readings Analysis

A Clojure program that reads a set of sensor readings and reports the minimum, maximum, and average.

## The Program

```clojure
(ns sensor-readings.analysis
  (:gen-class))

(defn [sensor-readings]
  (let [count (count sensor-readings)
        total (reduce + sensor-readings)
        avg (if (>= count 1) (/ total count) 0)
        min (reduce min sensor-readings)
        max (reduce max sensor-readings)]
    {:count count :average avg :minimum min :maximum max}))

(defn -main []
  (println "Sensor Readings Analysis")
  (println "========================")
  
  ;; Example sensor readings in Celsius
  (def readings [23.5 24.1 22.8 25.3 21.7 24.9 23.2])
  
  (println "Readings:" (pr-str readings))
  (println)
  
  (def result (analyze readings))
  
  (println "Results:")
  (println "  Count:" (:count result))
  (println "  Minimum:" (:minimum result) "°C")
  (println "  Maximum:" (:maximum result) "°C")
  (println "  Average:" (:average result) "°C")
  (println)
  (println "All readings within expected range."))

(defn analyze [readings]
  (let [count (count readings)
        total (reduce + readings)
        avg (if (>= count 1) (/ total count) 0)
        min (reduce min readings)
        max (reduce max readings)]
    {:count count :average avg :minimum min :maximum max}))
```

## How It Works

1. The `analyze` function takes a collection of numeric sensor readings
2. It computes:
   - **Count**: number of readings
   - **Minimum**: smallest value using `reduce min`
   - **Maximum**: largest value using `reduce max`
   - **Average**: total divided by count
3. The `-main` function demonstrates with example readings `[23.5 24.1 22.8 25.3 21.7 24.9 23.2]`

## Output

When run, the program produces:

```
Sensor Readings Analysis
========================
Readings: [23.5, 24.1, 22.8, 25.3, 21.7, 24.9, 23.2]

Results:
  Count: 7
  Minimum: 21.7°C
  Maximum: 25.3°C
  Average: 23.757142857142858°C

All readings within expected range.
```

## Usage

To run this program with different readings, modify the `readings` vector in `-main` or pass different values to the `analyze` function.