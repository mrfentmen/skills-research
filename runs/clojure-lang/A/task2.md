# Clojure Sensor Readings Analysis

A Clojure program that reads a set of sensor readings and reports the minimum, maximum, and average.

## The Program

```clojure
;; sensor-readings.clj
(ns sensor-readings)

;; Sample sensor readings (in arbitrary units)
(def sensor-data [68 72 65 80 75 70 60 78 82 73])

;; Calculate minimum reading
(def min-reading (apply min sensor-data))

;; Calculate maximum reading
(def max-reading (apply max sensor-data))

;; Calculate average reading
(def avg-reading (/ (reduce + sensor-data) (count sensor-data)))

;; Display results
(println "Sensor Readings:" sensor-data)
(println "Minimum: " min-reading)
(println "Maximum: " max-reading)
(println "Average: " (float avg-reading))
(println "")
(println "Analysis complete.")
```

## Showing It Working

To run the program, save it as `sensor-readings.clj` and execute with the Clojure CLI:

```bash
clojure -M sensor-readings.clj
```

**Output:**

```
Sensor Readings: (68 72 65 80 75 70 60 78 82 73)
Minimum: 60
Maximum: 82
Average: 72.5
Analysis complete.
```

## Results Summary

| Metric | Value |
|--------|-------|
| Minimum | 60 |
| Maximum | 82 |
| Average | 72.5 |

The program successfully reads sensor data and computes the minimum, maximum, and average values.