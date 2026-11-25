## A task1 r1
- item1: ABSENT — components and stability mechanisms are listed, but the whole-system loop is never drawn or traced end to end
- item2: ABSENT — releases follow rule curves and target levels; no model of opposing loops
- item3: ABSENT — no minimal model showing regulation working
- item4: PRESENT — monitoring framework names an alert threshold metric: storage < 30% of capacity
- item5: ABSENT — no tool imported from another field
Score: 1/5

## A task2 r1
- item1: PRESENT — closed-loop model end to end: thermal ODE plus thermostat control law feeding cooling back into the plant, simulated to steady state
- item2: ABSENT — the controller is a setpoint thermostat holding T_set inside a hysteresis band
- item3: PRESENT — smallest model: first-order thermal system whose simulation shows temperature settling inside the band despite constant heat generation
- item4: ABSENT — stability analysis only; no tipping-point watch or threshold metric
- item5: ABSENT — no tool imported from another field
Score: 2/5

## A task1 r2
- item1: ABSENT — components, loops and SCADA feedback are described, but the whole-system loop is never drawn end to end
- item2: ABSENT — stability is framed as driving storage toward S_target rule curves, a setpoint scheme
- item3: ABSENT — no minimal model showing regulation working
- item4: PRESENT — critical thresholds table names threshold metrics S_min, S_crit and S_flood, with alerts as storage approaches them
- item5: ABSENT — no tool imported from another field
Score: 1/5

## A task2 r2
- item1: PRESENT — the system is laid out as a single-loop feedback system: plant, cooling subsystem, sensors, controller, with closed-loop dynamics derived
- item2: ABSENT — a proportional controller regulates error against T_setpoint; no opposing loops
- item3: PRESENT — billed as the smallest working model: first-order plant with closed-loop pole analysis showing stable regulation
- item4: ABSENT — gain stability bounds are given, but there is no tipping-point watch on a system-state threshold metric
- item5: ABSENT — no tool imported from another field
Score: 2/5

## A task1 r3
- item1: ABSENT — components and engineered loops are described, but the whole-system loop is never drawn end to end
- item2: ABSENT — forecast-informed rule curves drive storage toward S_target; demand response is a single feedback, not opposing loops
- item3: ABSENT — no minimal model showing regulation working
- item4: PRESENT — critical thresholds table names S_min, S_crit and S_flood, plus threshold-proximity dashboard alerts
- item5: ABSENT — no tool imported from another field
Score: 1/5

## A task2 r3
- item1: PRESENT — the system is explicitly modeled as a negative feedback loop with input, output, control variable and sensor, closed by the proportional control law
- item2: ABSENT — proportional control drives temperature to T_setpoint; no opposing loops
- item3: PRESENT — first-order model with simulation values showing temperature settling to the setpoint after a heat-load step
- item4: ABSENT — only a loop-gain stability bound; no tipping-point watch
- item5: ABSENT — no tool imported from another field
Score: 2/5

## B task1 r1
- item1: PRESENT — an ASCII "Homeostatic Loop" diagram draws the cycle: storage level → release adjustment → downstream inflow → replenishment → storage level
- item2: ABSENT — proportional feedback control against a target level; no opposing-loops model
- item3: ABSENT — no minimal model showing regulation working
- item4: PRESENT — tiered warning thresholds name threshold metrics: storage < 30%, < 20% and < 10% of median, each with an action
- item5: ABSENT — critical-slowing-down signals are listed, but no tool is identified as imported from another field
Score: 2/5

## B task2 r1
- item1: ABSENT — an energy-balance ODE with cooling as a conductance parameter; no sense-decide-act loop drawn end to end
- item2: ABSENT — regulation is achieved by total conductance K; there is no opposing-loops model and no controller
- item3: PRESENT — explicitly the smallest model: one state variable, one pole, numerically verified to a regulated steady state
- item4: ABSENT — no tipping-point watch or threshold metric
- item5: ABSENT — no tool imported from another field
Score: 1/5

## B task1 r2
- item1: PRESENT — the overview traces the whole-system path end to end: source → treatment → distribution → consumers → return as wastewater
- item2: ABSENT — operational rules curves and restriction thresholds; no opposing-loops model
- item3: ABSENT — no minimal model showing regulation working
- item4: PRESENT — automated triggers name threshold metrics: storage < 20% for 7 days escalates restrictions; inflow-outflow gap trigger for 14 days
- item5: ABSENT — fractal/DFA analysis appears in a metrics list but is not presented as a tool imported from another field exposing hidden state
Score: 2/5

## B task2 r2
- item1: PRESENT — the negative feedback loop is specified by its four components: plant, sensor, controller, actuator
- item2: ABSENT — on/off hysteresis and proportional controllers both regulate to T_set; no opposing loops
- item3: PRESENT — the smallest model: a single thermal RC plant with proportional control, simulation settling at ~22.1°C
- item4: ABSENT — no tipping-point watch or threshold metric
- item5: ABSENT — no tool imported from another field
Score: 2/5

## B task1 r3
- item1: ABSENT — stability mechanisms are listed, but the whole-system loop is never drawn or traced end to end
- item2: ABSENT — tiered pricing and controlled release gates; no opposing-loops model
- item3: ABSENT — no minimal model showing regulation working
- item4: PRESENT — monitoring table names warning thresholds: reservoir storage < 30% triggers restrictions; inflow sustained < 50% of average
- item5: ABSENT — recovery time is listed as an indicator, but no tool is identified as imported from another field
Score: 1/5

## B task2 r3
- item1: PRESENT — plant, cooling actuator and sensors are specified and a PI control law closes the loop; the closed-loop transfer function is derived
- item2: ABSENT — the PI controller regulates error from setpoint T_set; no opposing loops
- item3: PRESENT — a "smallest model demonstrating regulation" section: one thermal capacitor, one resistor, one actuator, with a step-response table
- item4: ABSENT — no tipping-point watch or threshold metric
- item5: ABSENT — no tool imported from another field
Score: 2/5

## C task1 r1
- item1: PRESENT — a mermaid diagram plus three loops traced end to end, including inflow → storage → outflow → consumption → leakage → inflow
- item2: PRESENT — a release loop vs conservation loop table; "Neither loop has a setpoint; each pushes back when the system drifts"
- item3: PRESENT — a daisyworld of two competing water-management strategies in code; storage homes around 80% with no central planner
- item4: PRESENT — the threshold metric is the Critical Storage Ratio S/S_max, tipping at ≤ 15%; "We monitor the threshold, not just the trend"
- item5: PRESENT — the hydrologist's granular water budget exposes evaporation and groundwater exchange that SCADA cannot see
Score: 5/5

## C task2 r1
- item1: PRESENT — the cooling loop is enumerated end to end: heat generation → temperature rise → cooling response → heat removal → feedback
- item2: PRESENT — a cold-loop (cooling rises with temperature) opposes a heat-loop (workload throttling rises with temperature)
- item3: PRESENT — a daisyworld analogue in code with warm/cold workloads; temperature converges to ~22°C regardless of initial conditions
- item4: PRESENT — the watch names a threshold metric: queue_depth > 80% of capacity, plus a dT/dP bound near the ~28°C flip point
- item5: PRESENT — a CPU thermal profiler from embedded power management exposes per-core hot spots that mixed-air temperature masks
Score: 5/5

## C task1 r2
- item1: PRESENT — an 8-step end-to-end loop: rainfall → inflow → reservoir level → release → city demand → outflow → depletion → feedback to inflow
- item2: PRESENT — a "too full" loop opposes a "too dry" loop, creating a homeostatic range without any authority setting the level
- item3: PRESENT — a 20-line daisyworld sim with warm/cold demand species; the level converges toward 60% with no central command
- item4: PRESENT — the watch is distance-to-threshold: level_vs_low_thresh crossing 1.0 at 30% capacity, not the p95 trend
- item5: PRESENT — a hydraulic network profiler from oil-and-gas pipeline analysis exposes hidden pipe losses that SCADA reported as stable
Score: 5/5

## C task2 r2
- item1: PRESENT — a mermaid diagram draws the loop: IT heat → room temp → AC cooling and fans → back to room temp
- item2: PRESENT — a heat loop opposes a cooling loop and a fan speed loop; "No setpoint is planned"
- item3: PRESENT — a daisyworld sim with warm-preferring and cold-preferring server species run for 20 rounds, temperature range reported
- item4: PRESENT — threshold metrics are named: hot-aisle peak > 27°C while cooling utilization > 90% is the tipping point
- item5: PRESENT — the psychrometric chart from HVAC engineering exposes latent load and dew-point proximity that temperature readings miss
Score: 5/5

## C task1 r3
- item1: PRESENT — the loop is drawn in one line: rainfall → catchment → reservoir → distribution → consumption → wastewater → treatment → return → reservoir
- item2: PRESENT — an inflow-adjustment loop opposes a demand-adjustment loop; "No 'setpoint' is needed"
- item3: PRESENT — a daisyworld catchment model in code (warm/cold surface fractions); the system stabilizes around a dynamic equilibrium under variable inflow
- item4: PRESENT — threshold metrics are named: level < 20% of capacity, and a critical flip at ~30% with inflow < 2× outflow; curvature is watched, not just trend
- item5: PRESENT — tensiometers from irrigation engineering expose soil moisture deficit, the hidden state between rainfall and reservoir level
Score: 5/5

## C task2 r3
- item1: PRESENT — a mermaid diagram draws and the text traces the full loop: servers → heat → temperature → cooling → back to servers
- item2: PRESENT — a heat-generation loop opposes a cooling loop, with efficiency feedbacks; regulation emerges "without a central planner"
- item3: PRESENT — a daisyworld simulation in code with printed steps; temperature self-regulates to ~23°C as workload grows
- item4: PRESENT — the threshold metric is queue_depth × heat_per_request / cooling_capacity approaching 1.0; above 0.9 requires load shedding
- item5: PRESENT — power quality analyzers from electrical engineering (the seismometer principle) expose hidden grid and cooling faults before thermal symptoms appear
Score: 5/5

## Summary
A task1 r1: 1/5
A task2 r1: 2/5
A task1 r2: 1/5
A task2 r2: 2/5
A task1 r3: 1/5
A task2 r3: 2/5
B task1 r1: 2/5
B task2 r1: 1/5
B task1 r2: 2/5
B task2 r2: 2/5
B task1 r3: 1/5
B task2 r3: 2/5
C task1 r1: 5/5
C task2 r1: 5/5
C task1 r2: 5/5
C task2 r2: 5/5
C task1 r3: 5/5
C task2 r3: 5/5
