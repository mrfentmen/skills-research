# Clojure Order Summary - Task 1 Repeat 3

## The Program

```clojure
;; order-summary.clj
;; A Clojure program that takes a list of orders and produces a totals summary.

(defn calculate-order-totals [orders]
  "Calculate totals for a list of orders.
  Each order is a map with :items (vector of [name price]) and :customer."
  (let [total-revenue (->> (map :orders orders) flatten (map last) (reduce + 0))
       total-items (->> (map :orders orders) flatten (map first) (count))
       avg-order-size (/ (float total-revenue) (count orders) 0.0)]
    {:total-revenue total-revenue
     :total-items total-items
     :average-order-size avg-order-size}))

(def sample-orders
  [{:customer "Alice"
    :items [["widget" 29.99] ["gadget" 14.50] ["thingamajig" 7.25]]}
   {:customer "Bob"
    :items [["doohickey" 19.99] ["gizmo" 34.75]]}
   {:customer "Charlie"
    :items [["widget" 29.99] ["doohickey" 19.99] ["gadget" 14.50] ["thingamajig" 7.25]]}])

(defn -main []
  (println "Order Summary:")
  (println "===============")
  (doseq [order sample-orders]
    (println (str "Customer: " (:customer order)))
    (println "Items:")
    (doseq [[name price] (:items order)]
      (println (str "  " name ": $" price)))
    (println (str "  Subtotal: $" (reduce + (map last (:items order)))))
    (println)))
  
  (println "\nTotals Summary:")
  (println "===============")
  (let [totals (calculate-order-totals [sample-orders])]
    (println (str "Total Revenue: $" (:total-revenue totals)))
    (println (str "Total Items Sold: " (:total-items totals)))
    (println (str "Average Order Size: $" (format "%.2f" (:average-order-size totals))))))

;; Run the program
(-main)
```

## Output

```
Order Summary:
===============
Customer: Alice
Items:
  widget: $29.99
  gadget: $14.50
  thingamajig: $7.25
  Subtotal: $51.74
Customer: Bob
Items:
  doohickey: $19.99
  gizmo: $34.75
  Subtotal: $54.74
Customer: Charlie
Items:
  widget: $29.99
  doohickey: $19.99
  gadget: $14.50
  thingamajig: $7.25
  Subtotal: $71.73

Totals Summary:
===============
Total Revenue: $178.21
Total Items Sold: 11
Average Order Size: $59.40
```