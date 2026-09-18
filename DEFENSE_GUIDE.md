# Individual Defense Guide (50 Points)
## Assignment 2: Factory Method and Abstract Factory

This guide prepares you for the individual oral defense (worth **50% of the total assignment score**). Every section directly addresses the rubric criteria (D1–D6) in Section 9 of the assignment specification.

---

## Criterion D1: Factory Method Roles (10 points)

| Role | Class in Project | Code Explanation |
|---|---|---|
| **Product** | `com.logistics.transport.Transport` | Interface defining delivery contract: `void deliver(String cargo, String destination)`. Decouples callers from transport mechanisms. |
| **Concrete Products** | `com.logistics.transport.Truck`<br>`com.logistics.transport.Ship` | Concrete implementations. `Truck` prints road delivery behavior; `Ship` prints sea freight behavior. |
| **Creator** | `com.logistics.creator.Logistics` | Abstract class. Declares abstract factory method `createTransport()` and provides the shared template method `planDelivery(String cargo, String destination)`. |
| **Concrete Creators** | `com.logistics.creator.RoadLogistics`<br>`com.logistics.creator.SeaLogistics` | Subclasses overriding `createTransport()`. `RoadLogistics` instantiates `Truck`; `SeaLogistics` instantiates `Ship`. |
| **Runtime Path** | Trace: `Main` $\rightarrow$ `DeliveryApplication` $\rightarrow$ `Logistics` $\rightarrow$ `Transport` | 1. `Main` parses CLI input (`ROAD`) and calls `StartupHelper.createLogistics(DeliveryMode.ROAD)`, returning `RoadLogistics`.<br>2. `DeliveryApplication.run()` calls `logistics.planDelivery(cargo, destination)`.<br>3. `Logistics.planDelivery()` invokes the overridden `createTransport()`, obtaining a `Truck`.<br>4. `Logistics.planDelivery()` calls `transport.deliver(cargo, destination)`. |

---

## Criterion D2: Abstract Factory Roles (10 points)

| Role | Class in Project | Code Explanation |
|---|---|---|
| **Abstract Products** | `com.logistics.ui.Button`<br>`com.logistics.ui.Checkbox` | Product interfaces defining UI rendering contracts (`void paint()`). |
| **Concrete Products grouped into Families** | **Windows Family:** `WindowsButton`, `WindowsCheckbox`<br>**macOS Family:** `MacOSButton`, `MacOSCheckbox` | Platform-specific implementations printing styled platform text (`Rendering Windows button`, `Rendering macOS button`). |
| **Abstract Factory** | `com.logistics.ui.GUIFactory` | Interface declaring creation methods: `Button createButton()` and `Checkbox createCheckbox()`. |
| **Concrete Factories** | `com.logistics.ui.windows.WindowsFactory`<br>`com.logistics.ui.macos.MacOSFactory` | `WindowsFactory` returns `WindowsButton` and `WindowsCheckbox`.<br>`MacOSFactory` returns `MacOSButton` and `MacOSCheckbox`. |
| **Client** | `com.logistics.app.DeliveryApplication` | Injected with `GUIFactory` through constructor. Obtains components exclusively via `factory.createButton()` and `factory.createCheckbox()`, invoking `paint()` without concrete references or casting. |

---

## Criterion D3: Comparison and Extension Decisions (15 points)

### 1. Simple Factory vs. Factory Method (5 points)
- **Conditional creation (Simple Factory):** Uses a single concrete class containing an `if` or `switch` block (`if (type.equals("TRUCK")) return new Truck();`). Violates the Open-Closed Principle (OCP) because adding a new transport requires editing existing source code.
- **Subclass overrides (Factory Method):** Defers instantiation to subclasses (`RoadLogistics`, `SeaLogistics`). New products are added by creating new creator subclasses without modifying the base `Logistics` class.
- **Shared product contract:** Both patterns return instances adhering to a common interface (`Transport`).
- **Our implementation:** We implemented abstract class `Logistics` with concrete subclasses `RoadLogistics` and `SeaLogistics` overriding `createTransport()`.
- **Why startup selection is allowed:** `StartupHelper` selects the initial creator based on user input at application boot. Once the creator is created, all subsequent execution is strictly polymorphic without branching on concrete transport types.

### 2. Factory Method vs. Abstract Factory (5 points)
- **Product Scope:** Factory Method creates **one product** (`Transport`); Abstract Factory creates **families of related products** (`Button` + `Checkbox`).
- **Mechanism:** Factory Method relies on **inheritance** (subclasses override a method); Abstract Factory relies on **object composition** (a factory object is injected into a client).
- **Transport Use Case:** Suited for Factory Method because logistics requires one primary vehicle per delivery workflow.
- **GUI Use Case:** Suited for Abstract Factory because a user interface requires multiple consistent controls (button, checkbox) that must adhere to the same visual platform.
- **Family Consistency:** Abstract Factory guarantees that a Windows button is never accidentally paired with a macOS checkbox.

### 3. Design Reflection & System Extensions (5 points)

#### Extension 1: Adding a new Transport (e.g., Air Logistics / Airplane)
- **Classes to Add:**
  - `com.logistics.transport.Plane` implementing `Transport`.
  - `com.logistics.creator.AirLogistics` extending `Logistics`.
  - Add `AIR` value to `DeliveryMode` enum and update `StartupHelper.createLogistics()`.
- **Classes Remaining Unchanged:**
  - `Transport`, `Truck`, `Ship`, `Logistics`, `RoadLogistics`, `SeaLogistics`, and `DeliveryApplication` remain 100% untouched.

#### Extension 2: Adding a new UI Family (e.g., Linux platform)
- **Classes to Add:**
  - `com.logistics.ui.linux.LinuxButton` implementing `Button`.
  - `com.logistics.ui.linux.LinuxCheckbox` implementing `Checkbox`.
  - `com.logistics.ui.linux.LinuxFactory` implementing `GUIFactory`.
  - Add `LINUX` value to `UIPlatform` enum and update `StartupHelper.createGUIFactory()`.
- **Classes Remaining Unchanged:**
  - `Button`, `Checkbox`, `GUIFactory`, `WindowsFactory`, `MacOSFactory`, and `DeliveryApplication` remain 100% untouched.

#### Extension 3: Adding a new UI Product Type (e.g., TextField)
- **Classes to Change / Add:**
  - Define new interface `com.logistics.ui.TextField` with `void paint()`.
  - Add `TextField createTextField();` method to `GUIFactory` interface.
  - **Required changes to existing classes:** `WindowsFactory` and `MacOSFactory` must implement `createTextField()`.
  - Implement concrete products `WindowsTextField` and `MacOSTextField`.
  - Update `DeliveryApplication` client to store and render the new `TextField`.
- **Key Insight:** Abstract Factory makes adding new product families easy (Open-Closed Principle), but adding new product types is difficult because it requires changing the abstract factory interface and all concrete factories.

---

## Criterion D4: Demonstration (5 points)

Run the following commands in terminal to demonstrate all required outcomes:

1. **Road Delivery:**
   ```bash
   java -jar target/logistics-assignment-1.0.0.jar ROAD WINDOWS
   ```
2. **Sea Delivery:**
   ```bash
   java -jar target/logistics-assignment-1.0.0.jar SEA WINDOWS
   ```
3. **Windows UI Pair:**
   ```bash
   java -jar target/logistics-assignment-1.0.0.jar ROAD WINDOWS
   # Displays both 'Rendering Windows button' and 'Rendering Windows checkbox'
   ```
4. **macOS UI Pair:**
   ```bash
   java -jar target/logistics-assignment-1.0.0.jar ROAD MACOS
   # Displays both 'Rendering macOS button' and 'Rendering macOS checkbox'
   ```
5. **Invalid Input Handling:**
   ```bash
   java -jar target/logistics-assignment-1.0.0.jar AIR WINDOWS
   # Displays 'Validation Error: Unsupported delivery mode 'AIR'. Supported modes: ROAD, SEA.'
   ```

---

## Criterion D5: Explanation of Own Code (5 points)

The instructor may select any method from your codebase and ask:
- **Purpose:** What does it do?
- **Inputs & Return:** What arguments does it accept, what does it return?
- **Control Flow:** How does it execute?
- **Collaborating Objects:** What interfaces or classes does it interact with?
- **Hypothetical Change:** What happens if input is null or a new type is added?

### Example: `Logistics.planDelivery(String cargo, String destination)`
- **Purpose:** Orchestrates the core delivery workflow.
- **Inputs:** `cargo` (`String`), `destination` (`String`).
- **Return Value:** `void`.
- **Control Flow:** Checks non-null arguments $\rightarrow$ calls `createTransport()` $\rightarrow$ checks transport non-null $\rightarrow$ calls `transport.deliver(cargo, destination)`.
- **Collaborating Objects:** Collaborates with `Transport` interface (polymorphic dependency).
- **Hypothetical Change:** If `cargo` is `null`, it throws `NullPointerException` (defensive programming). If a new transport `Drone` is created, `planDelivery()` works without changing a single character of code.

### Example: `DeliveryApplication.renderUI()`
- **Purpose:** Renders the button and checkbox controls.
- **Inputs:** None.
- **Return Value:** `void`.
- **Control Flow:** Calls `button.paint()`, then `checkbox.paint()`.
- **Collaborating Objects:** `Button` and `Checkbox` interfaces. It does not know whether they are Windows or macOS components.

---

## Criterion D6: Clean Code Justification (5 points)

| Clean Code Practice | Project Excerpt | Justification & Benefit |
|---|---|---|
| **1. Meaningful Names** | `RoadLogistics`, `WindowsFactory`, `DeliveryApplication` | Clearly conveys pattern role and business domain. Avoids ambiguous names like `Manager` or `Processor`. |
| **2. Small Methods (SRP)** | `StartupHelper.parseArguments()` vs. `createLogistics()` | Each method performs one clear operation. Argument parsing is separated from object instantiation and rendering. |
| **3. Avoid Duplicated Logic (DRY)** | `Logistics.planDelivery()` | The workflow of acquiring transport and executing delivery is implemented once in the abstract creator, not repeated in subclasses. |
| **4. Data Abstraction (Chapter 6)** | `DeliveryApplication(GUIFactory factory, Logistics logistics)` | High-level client depends on pure interfaces (`GUIFactory`, `Button`, `Checkbox`, `Transport`). Zero exposure of internal representations. |
| **5. Objects & Encapsulation (Chapter 6)** | `Truck.deliver(...)`, `button.paint()` | Adheres to "Objects hide their data behind abstractions and expose operations that operate on that data" (Clean Code, p. 95). No anemic getter/setter data structures. |
