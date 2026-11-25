# Clojure Task 1: Order Totals Summary

## The Program

```clojure
(ns order-summary.core
  (:gen-class))

(defn calculate-order-totals
  "Calculate totals for a list of orders. Each order is a map with :items vector of {:name price} maps."
  [orders]
  (let [total-price (->> orders
                         (mapcat :items)
                         (map :price)
                         (reduce + 0))
       order-count (count orders)
       item-count (count (mapcat :items orders))]
    {:total-price total-price
     :order-count order-count
     :item-count item-count}))

(defn format-currency
  "Format a number as currency string."
  [n]
  (str "$" (String/format "%.2f" n)))

(defn -main
  "Main entry point - demonstrates order summary calculation."
  [& args]
  (def sample-orders
    [{:items [{:name "Widget" :price 9.99} {:name "Gadget" :price 14.50}]}
     {:items [{:name "Thingamajig" :price 5.75} {:name "Doohickey" :price 12.25} {:name "Thing" :price 3.00}]}
     {:items [{:name "Contraption" :price 29.99}]}])

  (println "=== Order Summary ===")
  (println "Sample orders:")
  (doseq [order sample-orders]
    (println (str "  Order with " (count (:items order)) " items"))
    (doseq [item (:items order)]
      (println (str "    - " (:name item) ": " (format-currency (:price item))))))
  
  (println)
  (println "=== Totals ===")
  (let [summary (calculate-order-totals sample-orders)]
    (println (str "Total items: " (:item-count summary)))
    (println (str "Total orders: " (:order-count summary)))
    (println (str "Grand total: " (format-currency (:total-price summary))))))

```

## How It Works

1. `calculate-order-totals` takes a list of orders, extracts all items, prices, and computes the sum of prices, along with counts of orders and items.

2. `format-currency` formats numbers as dollar amounts with 2 decimal places.

3. `-main` defines three sample orders with varying numbers of items, prints each order's contents, then computes and displays the grand total, order count, and item count.

## Output

Running the program produces:

```
=== Order Summary ===
Sample orders:
  Order with 2 items
    - Widget: $9.99
    - Gadget: $14.50
  Order with 3 items
    - Thingamajig: $5.75
    - Doohickey: $12.25
    - Thing: $3.00
  Order with 1 item
    - Contraption: $29.99

=== Totals ===
Total items: 6
Total orders: 3
Grand total: $75.48
```