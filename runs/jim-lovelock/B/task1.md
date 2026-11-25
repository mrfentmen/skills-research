# jim-lovelock arm B task 1: Reservoir and Water Supply System Analysis

## System Overview

The city's reservoir and water supply system functions as a self-regulating feedback loop with multiple interacting components:

- **Reservoir**: Primary storage basin with capacity constraints
- **Inflow**: River flow, groundwater recharge, precipitation capture
- **Outflow**: Municipal distribution, agricultural allocation, environmental releases
- **Demand**: Population consumption, industrial use, emergency reserves
- **Control mechanisms**: Dam operations, gate adjustments, pump scheduling

## Stability Factors

### What Keeps the System Stable

1. **Buffer capacity** – The reservoir acts as a thermal and volumetric buffer, dampening short-term fluctuations in inflow and demand. Seasonal storage provides memory that prevents high-frequency perturbations from propagating downstream.

2. **Proportional feedback control** – Dam release rates are typically adjusted in proportion to the difference between current storage and target level. This negative feedback mechanism reduces overshoot and maintains homeostasis.

3. **Multiple inflow sources** – Diversification across river flow, groundwater, and precipitation spreads risk. When one source dips, others can compensate, reducing systemic variance.

4. **Demand management** – Tiered pricing, leak detection, and seasonal restrictions flatten demand peaks, reducing the amplitude of the inflow-outflow mismatch.

5. **Safety margins** – Operating below maximum capacity ensures that extreme events (floods, droughts) can be absorbed without triggering emergency releases or rationing.

### Homeostatic Loop

```
Storage level → Release adjustment → Downstream inflow → Replenishment → Storage level
         ↑                                                       ↓
     Target level <─────────────────────────────────────────────
```

## Tipping Points

### Potential Collapse Scenarios

1. **Chronic under-fill** – Prolonged drought combined with growing demand can push storage below the minimum operating level. Once the reservoir loses its buffering capacity, small inflow variations cause large storage swings, creating a feedback loop of ever-more-restrictive releases.

2. **Infrastructure failure** – Dam gate malfunction, spillway capacity exceeded, or pump failure can cause abrupt shifts. If releases exceed the channel's conveyance capacity, catastrophic downstream flooding may result.

3. **Contamination event** – A pollutant influx without adequate dilution or treatment capacity can render the supply unusable, forcing immediate drastic reductions in withdrawal that cascade through the system.

4. **Demand surge** – Sudden population growth or economic expansion can outpace infrastructure upgrades, pushing the system into chronic deficit mode where stability depends on heroic conservation measures.

5. **Climate non-stationarity** – Shifts in precipitation patterns and increased evaporation rates can move the system's operating point outside the range for which the control architecture was designed, effectively breaking the feedback gains.

### Early Warning Signals

- Rising variance in storage levels
- Increasing autocorrelation at lag-1
- Skewing of the storage distribution toward low-storage states
- Critical slowing down: system recovery time from small perturbations lengthens

## Monitoring Strategy

### What to Watch

| Variable | Frequency | Rationale |
|----------|-----------|-----------|
| Reservoir storage (% capacity) | Hourly | Primary state variable; earliest indicator of deficit/surplus |
| Inflow rate (river + groundwater) | Hourly | Drives system; detecting trends early gives lead time |
| Outflow rate | Hourly | Controls drainage; mismatched inflow/output signals imbalance |
| Demand consumption | Daily | Can shift rapidly; tracking helps anticipate release adjustments |
| Precipitation (watershed) | Event-based | External forcing; pattern changes predict inflow shifts |
| Water quality metrics (turbidity, contaminants) | Hourly | Early detection of contamination events |
| Downstream stage/flow | Hourly | Validates release impacts; detects channel capacity issues |

### Visualization & Alerts

- **Storage duration curve**: Plot percentage of time storage falls below each percentile. Upward trend = increasing deficit risk.
- **Inflow-storage scatter**: Reveals the system's operating envelope; shifting cloud shape indicates changing climate or land-use conditions.
- **Control effort metric**: `|actual release - target release|` normalized by target. Rising values suggest the feedback is losing effectiveness.
- **Anomaly detection**: Statistical flags on any variable departing >3σ from rolling baseline.

### Warning Thresholds

- **Yellow alert**: Storage < 30% median for 30 consecutive days → review release schedule, communicate conservation appeal.
- **Orange alert**: Storage < 20% median + inflow < 50% of seasonal average → activate mandatory restrictions, evaluate emergency options.
- **Red alert**: Storage < 10% median + demand > 90% of capacity → implement emergency rationing, seek external supply.

### Feedback Loop Closure

Monitoring data should feed directly into the control algorithm:

1. Automated analytics compute the "system health index" from the above variables.
2. When the index crosses thresholds, predefined release adjustment protocols trigger.
3. Human operators review and approve or override before implementation.
4. Post-action, the system logs the deviation, rationale, and outcome for learning.

---

## Summary

The reservoir-water supply system is stable as long as buffering capacity exceeds demand variability, feedback gains are appropriately tuned, and multiple inflow sources provide redundancy. Tipping points emerge when chronic deficit erodes the buffer, when infrastructure constraints are breached, or when climate non-stationarity moves the operating point beyond the control design envelope. A monitoring regime focused on storage-inflow-demand dynamics, with automated early-warning and clear escalation thresholds, is essential for pre-emptive management.