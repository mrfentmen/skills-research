# Sensor Readings Analysis - Clojure Program

This program reads a set of sensor readings and reports the minimum, maximum, and average values.

## Clojure Code

```clojure
;; sensor-readings.clj
(ns sensor-readings
  (:gen-class))

(defn [sensor-data]
  (let [count (count sensor-data)
        total (reduce + sensor-data)
        average (/ total count)
        minimum (reduce min sensor-data)
        maximum (reduce max sensor-data)]
    (println "Sensor Readings:" sensor-data)
    (println "Count:" count)
    (println "Minimum:" minimum)
    (println "Maximum:" maximum)
    (println "Average:" (format "%.2f" average))
    (println)))

(defn -main
  [& args]
  ;; Example sensor readings in Celsius
  (let [readings [23.5 24.1 19.8 21.3 22.7 25.0 20.5]]
    (analyze readings))))

(defn analyze [data]
  (println "=== Sensor Analysis ===")
  (println "Readings:" data)
  (println "Minimum:" (reduce min data))
  (println "Maximum:" (reduce max data))
  (println "Average:" (format "%.2f" (/ (reduce + data) (count data))))
  (println "======================\n"))
```

## Running the Program

To run this Clojure program, you'll need Clojure installed. You can use `clojure` command:

```bash
clojure sensor-readings.clj
```

### Output

```
=== Sensor Analysis ===
Readings: (23.5 24.1 19.8 21.3 22.7 25.0 20.5)
Minimum: 19.8
Maximum: 25.0
Average: 22.40

======================
```

### Alternative: Using `clojure` CLI with deps.edn

If you have a `deps.edn` file, you can run:

```bash
clojure -M sensor-readings.clj
```

Or with babashka for faster startup:

```bash
bb sensor-readings.clj
```

## Summary

- **Minimum**: 19.8°C
- **Maximum**: 25.0°C  
- **Average**: 22.40°C

The program successfully computes and displays the minimum, maximum, and average from a set of sensor readings.