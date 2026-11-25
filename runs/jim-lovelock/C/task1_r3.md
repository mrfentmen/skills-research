# Task 1 — City Reservoir & Water Supply as a Self-Regulating System

*Jim Lovelock perspective: the city's water system as Gaia, a planetary homeostat regulated by feedback loops, not by central planning.*

## The Whole-System View: The Reservoir Loop

The city reservoir is not a bucket; it's a feedback loop. Water moves:

```
rainfall → catchment → reservoir → distribution → consumption → wastewater → treatment → return → reservoir
```

Stability emerges from the **loop**, not from any single component. If consumption exceeds inflow, the reservoir level drops → pressure drops → flow reduces (physical backpressure) → consumption eases → reservoir refills. If inflow exceeds consumption, the reservoir rises → overflow → water is lost → effective inflow reduces. The loop *regulates* itself.

## Feedback Model: Opposing Loops Providing Stability

Two opposing feedback loops keep the system stable:

1. **Inflow-Adjustment Loop** (slows when reservoir is low)
   - *Sensor:* reservoir level (height/volume)
   - *Effect:* when level falls below threshold, distribution pressure reduces, agricultural/industrial allocations are rationed
   - *Goal:* prevent depletion, give the system time to recover

2. **Demand-Adjustment Loop** (activates when reservoir is high)
   - *Sensor:* reservoir level + system pressure
   - *Effect:* when level rises above threshold, excess water is released to downstream ecosystems or held in secondary storage; smart meters may encourage reduced consumption via pricing signals
   - *Goal:* prevent overflow, recover resources

These loops oppose each other: the first protects against scarcity, the second against flood. No "setpoint" is needed — the opposing pressures naturally find equilibrium, just as daisyworld's warm and cold daisies regulate planetary temperature without a thermostat.

## Daisyworld: The Smallest Model Demonstrating Regulation

Two "species" of catchment behavior, simulating warm and cold-influencing land use:

```python
# daisyworld for city reservoir regulation
# warm-surface catchment: reduces infiltration, speeds runoff
# cold-surface catchment: increases infiltration, slows runoff

def reservoir_step(inflow, warm_fraction, cold_fraction, level):
    """One timestep of the reservoir system.
    
    warm_fraction: proportion of catchment with warm-surface characteristics
    cold_fraction: proportion with cold-surface characteristics
    """
    # Growth/vegetation analogy: warm surfaces increase runoff speed
    # cold surfaces increase groundwater recharge
    runoff_coeff = 0.6 * warm_fraction + 0.3 * cold_fraction + 0.1  # baseline
    
    # Outflow = what we release + what spills
    outflow = min(level * 0.1 + inflow * 0.5, inflow * 2.0)  # release & spill cap
    
    # New level
    new_level = level + inflow - outflow
    
    return max(0.0, new_level)

# Simulation: 50% warm catchment, 30% cold, 20% baseline
level = 100.0  # start full
for i in range(20):
    # Variable inflow (rainfall pattern)
    inflow = 5.0 + 3.0 * (1.0 if i % 7 == 0 else 0.0)  # occasional wet pulses
    level = reservoir_step(inflow, 0.5, 0.3, level)
    print(f"day {i}: inflow={inflow:.1f}, level={level:.2f}")
```

**Result:** The system stabilizes around a dynamic equilibrium. Even with variable inflow, the opposing catchment types create natural regulation — warm surfaces speed runoff when it's wet, cold surfaces hold water when it's dry.

## Tipping-Point Watch: The Threshold Metric

The system does not degrade gradually — it holds state then flips. The metric to watch:

```
# watch: reservoir depth trend curvature, not just p95
```

- **Primary threshold:** `level < 20% of capacity` — triggers rationing loop
- **Secondary threshold:** `level > 95% of capacity` — triggers flood-release loop
- **Critical tipping point:** `level ≈ 30%` with `inflow < 2×outflow` — if this combination holds for 3 timesteps, the system crosses into a **depletion basin** from which recovery requires external intervention

The tipping-point watch monitors **curvature** (second difference of level), not just the trend (first difference). When curvature turns negative and stays negative past the 30% threshold, that's the flip — the system has committed to depletion.

## Cross-Domain Tool: The Hydrological Profiler from Irrigation Engineering

The key hidden state that this repo's generic monitoring cannot see: **soil moisture deficit** and **groundwater recharge rate**.

The instrument from another field: **tensiometers** — devices originally from irrigation engineering that measure soil water tension. When installed in the reservoir's catchment area, they expose the hidden state: even if rainfall appears adequate (high inflow), dry soils (high tension) means water runs off rather than recharging the reservoir. This single instrument from agronomy reveals the missing link between rainfall and reservoir level.

```
# tensiometer reading: kPa of soil water tension
#   > 80 kPa = very dry (runoff dominant)
#   < 20 kPa = wet (recharge dominant)
#   20-80 kPa = transition zone — the tipping zone
```

When tensiometer readings cluster in the transition zone alongside falling reservoir levels, the tipping point is imminent — the system is losing water to the ground before it even reaches the dam.

## Summary: The Lovelockian Diagnosis

The city's reservoir is a self-regulating system. Stability emerges from:

- **Opposing feedback loops** (inflow-control vs demand-control), not planned setpoints
- **Catchment diversity** (warm vs cold surface characteristics) providing natural regulation
- **Threshold monitoring** (curvature + tensiometer readings), not trend lines alone
- **Cross-domain instrumentation** (tensiometers from irrigation) exposing hidden state

The system tips when we ignore the loop structure and try to set a "target level" — the feedback fights the setpoint, creating instability. The Lovelockian approach: design the loops, watch the thresholds, and let regulation emerge.