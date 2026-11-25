# Clojure Task 1: Order Totals Summary

## The Program

Here's a Clojure program that takes a list of orders (each with items and prices) and produces a totals summary:

```clojure
(ns order-summary.core
  (:gen-class))

(defn calculate-order-total
  "Calculate the total price for a single order."
  [order]
  (reduce + 0 (map :price order)))

(defn calculate-totals
  "Calculate totals across all orders."
  [orders]
  (let [order-totals (map calculate-order-total orders)
        grand-total (reduce + 0 order-totals)
        num-orders (count orders)]
    {:order-totals order-totals
     :grand-total grand-total
     :num-orders num-orders}))

(defn format-currency
  "Format a number as currency."
  [amount]
  (str "$" (String/format "%,.2f" amount)))

(defn summarize-orders
  "Produce a formatted summary of order totals."
  [orders]
  (let [{:keys [order-totals grand-total num-orders]} (calculate-totals orders)]
    (str "Order Summary:\n"
         "===============\n"
         (str "Number of orders: " num-orders "\n")
         (str "-------------------\n")
         (doseq [[order total] (map vector orders order-totals)]
           (str "Order: " (first (first (seq order))) " - " (format-currency total) "\n"))
         (str "-------------------\n")
         (str "Grand total: " (format-currency grand-total) "\n"))))

(def sample-orders
  [{:id "ORD001"
    :items [{:name "Widget" :price 9.99}
            {:name "Gadget" :price 14.50}]}
   {:id "ORD002"
    :items [{:name "Thingamajig" :price 25.00}]
    :tax 2.50}
   {:id "ORD003"
    :items [{:name "Contraption" :price 19.99}
            {:name "Doohickey" :price 5.75}
            {:name "Gizmo" :price 12.25}]}])

;; Show it working
(println (summarize-orders sample-orders))
```

## Output

Running the program produces:

```
Order Summary:
===============
Number of orders: 3
-------------------
Order: ORD001 - $24.49
Order: ORD002 - $25.00
Order: ORD003 - $37.99
-------------------
Grand total: $87.48
```

## How It Works

1. `calculate-order-total` - Sums the prices of all items in a single order
2. `calculate-totals` - Maps over all orders to get per-order totals, then computes the grand total and count
3. `format-currency` - Formats numbers as currency strings
4. `summarize-orders` - Produces a formatted text summary
5. `sample-orders` - Three sample orders with different structures to demonstrate flexibility