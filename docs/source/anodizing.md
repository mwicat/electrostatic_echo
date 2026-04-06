# Anodizing

## General procedure

Notes:

- In general you want to apply either a constant voltage in small steps (for example, first 15V then 30V then 60V etc.) or constant current.
- You want to monitor the voltage and current at all times.
- In constant voltage regime, you set the voltage and then expect the current to go down with time and settle on some small value (ideally 0.1mA/cm2)
- In constant current regime, you set the current to 1 mA/cm2 (note that this value depends on the surface area of your disk) and then expect the voltage to go up until the maximum value which is also set by you and it a target voltage value
- Constant current is better for controlling the process
- Constant voltage is easier to set up

Good summary of constant current vs constant voltage can be found at [Anodizing by Constant Current Density](https://electrolurgy.com/wp-content/uploads/2026/01/Anodizing-by-Current-Density-Charlie-Grubbs.pdf):

### Constant Voltage

Anodizing by constant voltage can be compared to driving your car blindfolded. Because the voltage is only the **driving force** (much like the car’s accelerator pedal) in a very dynamic system, other methods of control must be employed.

The best method is the use of **constant current density anodizing**.

### Constant Current

Let us again refer to the automobile analogy. If we consider the accelerator as the voltage and the current as the cruise control, we can see how constant current is a more controllable system of finishing.

As you are aware, when using cruise control on your automobile, you set the desired speed (amperage). You then allow the accelerator pedal (voltage) to increase or decrease as needed to maintain this speed.

This is the same principle that applies in an anodizing tank:

- The **voltage fluctuates** according to system needs  
- The **current (amperage) is maintained constant**

Factors that influence the required voltage include:

- Bath temperature  
- Acid concentration  
- Aluminum content  
- Aluminum alloy
- Electrical resistance  
- Other process variables  

These variables change the voltage necessary to achieve a **good, consistent anodizing result**.

---

Note that the general article describes porous anodizing
in dissolving acids which is a different thing, but the comparison and analogy on the current and voltage is quite good, especially for the layman.


Sourced from [Electrophotographic reproduction system utilizing ion modulator and dielectric and dielectric imaging surface](https://patents.google.com/patent/US3907560A/en?oq=us3%2c907%2c560)

#### Sample Preparation

- Wash with tap water and acetone/IPA
- Air dry

#### Anodizing Bath Composition

- **Deionized water:** 1 liter  
- **Boric acid (H₃BO₃):** 90 g  
- **Sodium tetraborate (borax, Na₂B₄O₇·10H₂O):** 5.6 g  

Bath temperature: **20 °C**

#### Anodizing Setup

- Aluminum sample connected to **positive terminal (anode)**  
- Power supply: **0–100 V DC**  

Cathode:
- Graphite or stainless steel plate
- Positioned parallel to the anode  
- Separation: **~25 mm**

#### Post-Treatment

- Remove sample
- Wash with tap water  

## Importance of bath purity

Sourced from [Chapter VII: The filming electrolyte of The Electrolytic Capacitor](https://archive.org/details/TheElectrolyticCapacitor/page/n51/mode/2up)

The purity of all constituents of the solution, including the water, which should be distilled, is of prime importance. Particular attention must be given to the prevention of contamination with chlorides, as their interfering effect with the film formation is most potent. A few parts per million of chlorides, present in the forming or operating electrolyte, may adversely affect the quality of the film.

## Anodizing in boric acid

Sourced from [Chapter VII: The filming electrolyte of The Electrolytic Capacitor](https://archive.org/details/TheElectrolyticCapacitor/page/n51/mode/2up)

An aqueous solution of **boric acid** with the addition of an appropriate percentage of **sodium borate** meets the usual requirements for the formation of capacitor anodes and is widely employed.

The film formed in a solution of boric acid and its salts is:

- Dense  
- Impermeable to the solution  
- Practically insoluble in the electrolyte  

As a result:

- Film formation is rapid  
- Growth stops once an extremely thin coating is produced  
- The coating prevents further contact between the underlying metal and electrolyte ions  

### Properties of Such Films

- Very thin → poor protection against corrosion and abrasion  
- Low adsorbency  
- Excellent dielectric properties  

These characteristics make them well suited for **capacitor anodes**

---

### Composition of the Filming Solution

- **Boric acid (H₃BO₃):**
  - Typically ~10% by weight  
  - Can vary without major impact  

- **Sodium borate (Na₂B₄O₇·10H₂O):**
  - Must be carefully controlled  
  - Strongly affects **electrolyte resistivity**  
  - Resistivity influences **breakdown voltage**

---

### Effect of Sodium Borate Concentration

- Typical proportion: ~1% of total solution weight  

#### Low voltage formation:
- Higher sodium borate content  
- Lower resistivity  
- Reduced power loss (**P·R losses**)  

#### High voltage formation:
- Lower sodium borate content  
- Higher resistivity  
- Enables higher breakdown voltage  

#### Very high voltage (>500 V):
- Often use **pure boric acid solution**  
- No sodium borate added  

Sourced from [US patent US2116449A: Electrolytic device](https://patents.google.com/patent/US2116449A/en?oq=us2%2c116%2c449+)

While a large number of electrolytes have been suggested for film formation, as well as for use as final (filling) electrolytes in dry electrolytic capacitors, both the forming and final electrolytes now used are generally of the **borate type**. In these electrolytes, the ionogen is **boric acid and/or a salt of boric acid**.

This preference arises because borate electrolytes have been found to produce films that, for a given thickness, exhibit:

- Higher electrical resistance  
- Higher breakdown voltage  
- Lower power factor  

Compared to films formed using other electrolytes, borate-based films provide **better overall operating characteristics** in capacitors.

## Anodizing in citric acid

The anodization in citric acid is described in [Investigation of anodic oxide formation on AA 7075 in citric acid](https://www.sciencedirect.com/science/article/pii/S0254058424005832?ref=pdf_download&fr=RR-2&rr=9e84bd098da47326) and [Anodizing in Aqueous Solutions of Organic Carboxylic Acids
](https://www.tandfonline.com/doi/abs/10.1080/00202967.1967.11870016)


## Influence of the electrolyte on the film properties

Sourced from [M. Katoh: The characteristic and the evaluation of the barrier type
anodic oxide film](https://www.jstage.jst.go.jp/article/sfj1950/39/8/39_8_420/_article/-char/ja/)

### Table 1: General tendencies

| Electrolyte | Breakdown Voltage | Leakage Current | Hydration Resistance | Acid Resistance |
| --- | --- | --- | --- | --- |
| Borate | Good | Poor | Poor | Poor |
| Phthalate | Moderate | Moderate | Poor | Good |
| Phosphate | Moderate | Good | Excellent | Poor |
| Adipate | Moderate | Excellent | Poor | Good |

The incorporation of **anions into the oxide film** likely explains these differences.

### Table 2: Some examples of the forming electrolyte

| Electrolyte                                              | Abbreviation | Concentration (g/L) | pH  | Specific Resistance (Ω·cm) |
|----------------------------------------------------------|--------------|---------------------|-----|-----------------------------|
| Ammonium Adipate (NH₄COO·(CH₂)₄·COONH₄)                 | Ad           | 150                 | 6.8 | 7.8                         |
| Ammonium Borate (NH₄BO₂)                                | B            | 100                 | 6.0 | 8.0                         |
| Ammonium Dihydrogen Phosphate (NH₄H₂PO₄)                | P            | 1.4                 | 5.5 | 350                         |
| Potassium Hydrogen Phthalate (KOOC·C₆H₄·COOH)           | Ph           | 20                  | 5.0 | 55                          |

### Table 3: Comparison among the barrier films formed in the several anodizing solutions

| Electrolyte | Break-down Voltage | Leakage Current | Hydration Resistance | Acid Resistance | Transient Behavior |
|-------------|------------------|----|-----------|------|--------------------|
| B           | excellent / 1000V  | poor | poor      | poor | poor               |
| Ph          | moderate / 200V    | good | poor      | excellent | moderate       |
| P           | poor / 120V        | excellent | excellent | poor | good         |
| Ad          | moderate / 250V    | excellent | poor      | excellent | excellent   |


## Influence of hydration on the film properties

Sourced from [US patent US20060124465A1: Capacitor containing aluminum anode foil anodized in low water content glycerine-phosphate electrolyte
](https://patents.google.com/patent/US20060124465A1/en)

Hydration resistance, an important consideration for foil used in electrolytic capacitors, may be enhanced by including a small amount of an alpha-hydroxy carboxylic acid (such as tartaric acid or citric acid) in the anodizing electrolyte solution, as described in U.S. Pat. No. 4,481,084.

The tendency of anodic aluminum oxide to absorb water—forming a variety of hydrated species with impaired dielectric properties—appears to be, at least in part, a function of the hydration state of the outermost portion of the anodic oxide at the end of the anodizing process.

Lilienfeld, in U.S. Pat. No. 2,826,724, states:

> “It is the hydration stratum of the oxide film, adjacent the film–electrolyte interface, which causes most of the power loss; and that the progressive development of hydration at the interface causes the aforesaid instability.”

Alwitt, in U.S. Pat. No. 3,733,291, describes a method of removing the residual hydration layer from the outer surface of anodized aluminum capacitor foil. This foil has been exposed to a pre-anodizing hydration step (referred to by Alwitt as a “preboil”) prior to anodizing in order to conserve electrical energy during anodizing.

Alwitt employs a dilute phosphoric acid solution, generally containing a small amount of chromate to inhibit corrosion, to dissolve the outer hydration layer.

## Resources

### Articles

- [Anodic oxide films on aluminum](https://psec.uchicago.edu/Papers/Chemical_Reviews_Anodic_oxide_films_on_aluminum.pdf)

### Books

- [Chapter IX: Formation of the anodic film Electrolytic capacitors : the theory, construction, characteristics and application of all types / by Paul McKnight Deeley](https://babel.hathitrust.org/cgi/pt?id=mdp.39015002917980&seq=121)
- [The Electrolytic Capacitor by Alexander M. Georgiev](https://archive.org/details/TheElectrolyticCapacitor/page/n47/mode/2up)

