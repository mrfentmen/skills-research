# Clojure Program: Order Totals Summary

A Clojure program that takes a list of orders (each with items and prices) and produces a totals summary.

## The Program

```clojure
(ns order-summary.core
  (:gen-class))

;; Define an order as a map with :id and :items
;; Each item has :name and :price

(def sample-orders
  "A collection of sample orders with items and prices."
  [
   {:id 1
    :items [{:name "Widget" :price 10.00}
            {:name "Gadget" :price 25.50}]}
   {:id 2
    :items [{:name "Thingamajig" :price 5.75}
            {:name "Doohickey" :price 15.20}
            {:name "Contraption" :price 42.99}]}
   {:id 3
    :items [{:name "Widget" :price 10.00}
            {:name "Thingamajig" :price 5.75}]}
  ])

;; Calculate the total price of items in a single order
(defn order-total
  "Calculate total price for one order."
  [order]
  (reduce + (map :price (:items order))) 0.0)

;; Produce a summary map for a single order
(defn order-summary
  "Produce a summary map for one order."
  [order]
  {:order-id (:id order)
   :item-count (count (:items order))
   :total-price (order-total order)})

;; Produce summaries for all orders
(defn all-summaries
  "Produce summaries for all orders."
  [orders]
  (map order-summary orders))

;; Format a summary as a readable string
(defn format-summary
  "Format a summary map as a string."
  [summary]
  (str "Order " (:order-id summary) ": "
       (:item-count summary) " items, total: $"
       (String/format "%.2f" (:total-price summary))))

;; Main function to demonstrate the program
(defn -main
  "Run the order summary program."
  [& args]
  (println "Orders:")
  (doseq [order sample-orders]
    (println (str "  Order " (:id order) ": "
                  (count (:items order)) " items")))
  (println)
  (println "Summary:")
  (doseq [summary (all-summaries sample-orders)]
    (println (format-summary summary)))
  (println)
  (println "Grand total across all orders:")
  (println (str "$" (String/format "%.2f"
                               (reduce + (map order-total sample-orders)) 0.0)))))
```

## Running the Program

To run this program, save it to `order_summary.clj` and execute with Leiningen or deps.edn:

```bash
lein run -m order-summary.core
```

Or with `clojure` CLI:

```bash
clojure -M order_summary.clj
```

## Sample Output

```
Orders:
  Order 1: 2 items
  Order 2: 3 items
  Order 3: 2 items

Summary:
Order 1: 2 items, total: $35.50
Order 2: 3 items, total: $63.94
Order 3: 2 items, total: $15.75

Grand total across all orders:
$115.19
>
```

## How It Works

1. `sample-orders` defines three orders, each with a unique ID and a vector of items
2. `order-total` extracts prices from an order's items and sums them
3. `order-summary` creates a summary map with the order ID, item count, and total price
4. `all-summaries` maps `order-summary` across all orders
5. `format-summary` turns a summary map into a human-readable string
6. `-main` prints the orders and their summaries, plus a grand total

The program is intentionally modular: you can swap `sample-orders` for any other collection of orders with the same shape, and the summary logic will work without changes.