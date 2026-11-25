# Data Center Cooling as a Feedback System

## Task Overview
Analyze the cooling of a large data center as a feedback system, using the smallest model that demonstrates regulation working.

## System Description

The data center cooling system can be modeled as a negative feedback loop:

- **Input**: Heat load from servers (Q_servers)
- **Output**: Data center temperature (T)
- **Control Variable**: Cooling system capacity (C)
- **Sensor**: Temperature sensors distributed throughout the facility

## Smallest Viable Model

A first-order linear model is sufficient to demonstrate regulation:

### Differential Equation

```math
C \frac{dT}{dt} + T = K \cdot Q_{servers}
```

Where:
- `T` = temperature deviation from setpoint (°C)
- `dT/dt` = rate of temperature change
- `C` = thermal capacitance of the data center (s)
- `K` = heat-to-temperature gain factor (°C/kW)
- `Q_servers` = server heat load (kW)

### Transfer Function

```math
G(s) = \frac{T(s)}{Q_{servers}(s)} = \frac{K}{Cs + 1}
```

This is a standard first-order system with time constant τ = C.

## Regulation Mechanism

The feedback controller adjusts cooling capacity based on measured temperature:

```python
# Simple proportional control
C(t) = C_base + K_p * (T_setpoint - T_measured)
```

Where:
- `C_base` = baseline cooling capacity
- `K_p` = proportional gain
- `T_setpoint` = desired temperature (e.g., 22°C)
- `T_measured` = actual measured temperature

## Stability Analysis

For stable regulation, the loop gain must satisfy:

```math
0 < K_p < \frac{C}{K}
```

If `K_p` is too high, the system oscillates. If too low, regulation is slow.

## Simulation Results

With typical values:
- C = 1000 s (thermal capacitance)
- K = 0.1 °C/kW
- K_p = 5 (°C/kW)
- Q_servers step from 500 kW to 600 kW

The temperature settles to the new setpoint within ~5 time constants (5000 s ≈ 1.4 hours), demonstrating effective regulation.

## Conclusion

A first-order model with proportional control is the smallest model that reliably demonstrates data center cooling regulation. More complex models (higher-order, distributed parameters) are unnecessary for basic regulation analysis.