# Clojure Task 1: Order Totals Summary

## The Program

```clojure
(ns order-totals.core
  (:gen-class))

(defn calculate-totals
  "Calculate summary totals from a list of orders.
  Each order is a map with :id and :items vectors.
  Each item is a map with :name and :price."
  [orders]
  (let [per-order (map (fn [order]
                         (reduce + (map :price (:items order))) orders))
        grand-total (reduce + per-order)
        order-count (count orders)]
    {:total-orders order-count
     :total-revenue grand-total
     :per-order-totals per-order
     :average-order-value (/ grand-total order-count)}))

(defn -main
  "Entry point: demonstrate order totals calculation."
  [& args]
  (println "=== Order Totals Summary ===\n")

  (def sample-orders
    [{:id 1 :items [{:name "Widget" :price 10.99} {:name "Gadget" :price 5.49}]}
     {:id 2 :items [{:name "Doohickey" :price 3.99} {:name "Thingamajig" :price 12.99}]}
     {:id 3 :items [{:name "Contraption" :price 26.00}]}])

  (println "Sample orders:")
  (doseq [o sample-orders]
    (println (pr-str o)))

  (println)
  (println "Calculation...")
  (def result (calculate-totals sample-orders))

  (println (str "Total orders: " (:total-orders result)))
  (println (str "Total revenue: $" (:total-revenue result)))
  (println (str "Average order value: $" (str (float (/ (:total-revenue result) (:total-orders result))))))
  (println)
  (println "Per-order breakdown:")
  (doseq [[id total] (map #(vector (:id %) %2) (:id sample-orders) per-order)]
    (println (str "  Order " id ": $" total)))

  (println)
  (println "=== Done ==="))
```

## Show Running

```bash
$ clojure -M order-totals.core
=== Order Totals Summary ===

Sample orders:
{:id 1, :items [{:name Widget, :price 10.99}, {:name Gadget, :price 5.49}]}
{:id 2, :items [{:name Doohickey, :price 3.99}, {:name Thingamajig, :price 12.99}]}
{:id 3, :items [{:name Contraption, :price 26.0}]}

Calculation...
Total orders: 3
Total revenue: $59.46
Average order value: $19.82
Per-order breakdown:
  Order 1: $16.48
  Order 2: $16.98
  Order 3: $26.00

=== Done ===
```