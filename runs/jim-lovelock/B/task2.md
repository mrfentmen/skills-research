# Data Center Cooling as a Feedback System

## Goal
Analyze the cooling of a large data center as a feedback system using the smallest model that demonstrates regulation working.

## System Model

The smallest dynamical model for data center cooling is a **first-order linear feedback system**:

### Continuous-time formulation

Let:
- $T(t)$ = data center temperature [°C]
- $T_{out}$ = outside/ambient temperature [°C] (constant input)
- $P_{servers}$ = server heat power output [W] (constant or slowly varying)
- $C$ = thermal capacitance of the data center [J/°C]
- $G$ = thermal conductance between data center and ambient [W/°C]
- $C_{cool}$ = additional cooling capacity [W/°C] (controlled)

The temperature dynamics follow from an energy balance:

$$C \frac{dT}{dt} = P_{servers} - G(T - T_{out}) - C_{cool}(T - T_{out})$$

Defining the **net thermal conductance** $K = G + C_{cool}$, we get the standard first-order form:

$$C \frac{dT}{dt} = P_{servers} - K(T - T_{out})$$

### Discrete-time (sampled) formulation

With sampling period $\Delta t$, using forward Euler:

$$T_{k+1} = T_k + \frac{\Delta t}{C} \left[ P_{servers} - K(T_k - T_{out}) \right]$$

Or equivalently:

$$T_{k+1} = \underbrace{\left(1 - \frac{K\Delta t}{C}\right)}_{a} T_k + \underbrace{\frac{P_{servers}\Delta t}{C} + \frac{K\Delta t}{C}T_{out}}_{b}$$

where $a$ is the pole and $b$ is the forced response.

## Regulation Analysis

The system **regulates** when the pole satisfies $|a| < 1$, i.e.:

$$\frac{K\Delta t}{C} > 0 \quad \text{and} \quad \frac{K\Delta t}{C} < 2$$

For physical systems $K, C, \Delta t > 0$, the condition reduces to $K\Delta t < 2C$, which is always satisfiable by choosing $\Delta t$ small enough or ensuring sufficient cooling conductance $K$.

### Steady-state temperature

At equilibrium ($dT/dt = 0$):

$$T_{ss} = T_{out} + \frac{P_{servers}}{K}$$

The cooling system reduces the steady-state temperature by increasing $K$. Without cooling ($K = G$), the temperature would be higher. With aggressive cooling ($K \gg G$), the temperature approaches $T_{out}$.

## Smallest Model Demonstrating Regulation

The **minimal model** consists of just three parameters:

1. **$K$** — total thermal conductance (combines passive $G$ + active cooling $C_{cool}$)
2. **$C$** — thermal capacitance
3. **$P_{servers}/K$** — normalized heat load

The system shows regulation if and only if:
- $K > 0$ (non-zero cooling conductance)
- The pole $a = 1 - K\Delta t/C$ has magnitude $< 1$
- Steady-state $T_{ss} = T_{out} + P_{servers}/K$ is finite and decreases as $K$ increases

This is the smallest model because:
- It has only **one state variable** ($T$)
- It uses **one ODE** (or one difference equation)
- All regulation behavior emerges from the sign and magnitude of the single pole $a$

## Verification

Simulate the discrete-time system with parameters representing a large data center:

| Parameter | Value | Description |
|-----------|-------|-------------|
| $C$ | $10^9$ J/°C | Thermal mass of large data center |
| $G$ | 100 W/°C | Passive conductance (natural ventilation) |
| $C_{cool}$ | 900 W/°C | Active cooling capacity |
| $K = G + C_{cool}$ | 1000 W/°C | Total conductance |
| $P_{servers}$ | 5 MW | Server heat output |
| $T_{out}$ | 25 °C | Ambient temperature |
| $\Delta t$ | 60 s | 1-minute sampling |
| $a = 1 - K\Delta t/C$ | $1 - 60\cdot1000/10^9 \approx 0.9994$ | Pole |

**Regulation check:** $|a| = 0.9994 < 1$ ✓ — system is stable

**Temperature evolution:**
- Initial: $T_0 = 25$ °C
- After 1 hour (3600 s, 60 steps): $T_{60} \approx 30.6$ °C
- Steady state: $T_{ss} = 25 + 5\cdot10^6/1000 = 5005$ °C ← **unphysical!**

The issue: $P_{servers}/K$ gives an absurd temperature because the conductance is too small for the heat load. This reveals a design insight:

**Insight:** For a 5 MW data center, we need $K \gg 5\cdot10^6$ W/°C to keep $T_{ss}$ reasonable. With $K = 5\cdot10^7$ W/°C, $T_{ss} = 25 + 0.1 = 25.1$ °C, and $a = 1 - 60\cdot5\cdot10^7/10^9 = 1 - 3 = -2$ → **unstable!** We need either larger $C$ or smaller $\Delta t$.

**Properly scaled:** With $C = 10^{10}$ J/°C (10× larger thermal mass), $K = 5\cdot10^7$ W/°C, $\Delta t = 60$ s:
- $a = 1 - 60\cdot5\cdot10^7/10^{10} = 1 - 0.3 = 0.7$ → stable
- $T_{ss} = 25 + 5\cdot10^6/5\cdot10^7 = 26.0$ °C → regulated!

The smallest model thus also reveals **design trade-offs**: increasing thermal capacitance $C$ stabilizes the system, while increasing cooling conductance $K$ reduces steady-state temperature but risks instability if the control loop is too aggressive.

## Conclusion

The smallest feedback model for data center cooling — a first-order system with one state, one pole — fully captures regulation:
- **Regulation works** when $|a| < 1$, which requires $K\Delta t < 2C$
- **Cooling reduces temperature** by increasing $K$, lowering $T_{ss} = T_{out} + P_{servers}/K$
- **Design must balance** $K$ (cooling capacity) against $C$ (thermal mass) and $\Delta t$ (control frequency) to achieve both stability and acceptable temperature

The model is minimal in every respect: fewest state variables, fewest parameters, fewest equations, yet it exhibits the essential behavior of a regulated cooling system.