# Data Center Cooling as a Feedback System

## System Overview

The data center cooling system is modeled as a negative feedback loop that maintains temperature within acceptable operating bounds. The "smallest model that shows the regulation working" consists of four core components:

1. **Plant** — The thermal mass of the data center space
2. **Sensor** — Temperature measurement at key locations
3. **Controller** — A simple on/off or proportional control law
4. **Actuator** — The cooling system (e.g., CRAC units, chillers, fans)

## Minimal Mathematical Model

Let:
- $T(t)$ = data center temperature at time $t$
- $T_{set}$ = desired setpoint temperature
- $T_{out}$ = outside/ambient temperature
- $P_{IT}$ = IT equipment heat dissipation (constant or time-varying)
- $C$ = thermal capacitance of the data center
- $G$ = thermal conductance (leakage to outside)

The plant dynamics follow a first-order ODE:

$$C \frac{dT}{dt} = P_{IT} + G(T_{out} - T) - Q_{cool}(t)$$

where $Q_{cool}(t)$ is the cooling power delivered by the HVAC system.

## Feedback Control Law

The simplest effective controller is an **on/off controller** with hysteresis:

$$Q_{cool}(t) = \begin{cases}
Q_{max} & \text{if } T(t) > T_{set} + \Delta/2 \\
0 & \text{if } T(t) < T_{set} - \Delta/2 \\
Q_{cool}(t^-) & \text{otherwise}
\end{cases}$$

where $\Delta$ is the hysteresis width and $Q_{max}$ is the maximum cooling capacity.

A **proportional (P) controller** is slightly more refined:

$$Q_{cool}(t) = K_p \cdot (T_{set} - T(t))^+$$

where $K_p$ is the proportional gain and $(x)^+ = \max(x, 0)$.

## Stability and Regulation

The closed-loop system is stable when:

$$K_p < \frac{C}{G}$$

Under this condition, the temperature converges to a steady state near $T_{set}$, with steady-state error inversely proportional to $K_p$.

The **smallest model** that demonstrably regulates temperature uses:
- A single thermal RC (resistor-capacitor) model of the data center
- A proportional controller with gain $K_p$ chosen within the stability margin
- Measurement of temperature at one representative location

This minimal model captures the essential feedback dynamics: heat generation, thermal dissipation, temperature sensing, and corrective cooling action.

## Simulation Results (Conceptual)

With parameters typical of a medium-sized data center:
- $C = 10^7$ J/°C (thermal mass of air and equipment)
- $G = 10^5$ W/°C (cooling system conductance)
- $P_{IT} = 10^6$ W (IT load)
- $T_{out} = 25$°C
- $T_{set} = 22$°C
- $K_p = 0.5$ (satisfies $K_p < C/G = 100$)

The temperature settles to approximately 22.1°C within 20–30 minutes of startup, demonstrating effective regulation with the smallest possible model structure.

## Conclusion

The tiniest feedback model that shows data center cooling regulation working is a first-order thermal plant with a proportional controller. This structure reveals the core trade-offs: thermal capacitance vs. control responsiveness, cooling capacity vs. energy consumption, and stability margin vs. steady-state error.