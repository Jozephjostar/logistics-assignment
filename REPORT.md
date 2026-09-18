# Assignment 2: Factory Method and Abstract Factory
**Course:** ShP-2216 Software Design Patterns  
**Institution:** Astana IT University | School of Software Engineering  
**Academic Year:** 2026–2027 | Year 2, Trimester 4  
**Student:** Nursultan Maratov  
**Group:** SE-2523  
**Instructor:** Yerassyl Bekenov  
**GitHub Repository:** [https://github.com/Jozephjostar/logistics-assignment](https://github.com/Jozephjostar/logistics-assignment)  
**Submitted Commit:** `fc38cfc` (refactor: simplify code structure and remove comments across all classes)  

---

## 1. Introduction

This assignment implements a consolidated Java logistics application integrating two core Gang of Four (GoF) creational design patterns: **Factory Method** and **Abstract Factory**. The application models a multi-modal freight system supporting road and maritime transportation while providing cross-platform user interface components for Windows and macOS environments.

### Why Factory Method Fits the Logistics Part
Logistics operations revolve around a single polymorphic product concept: `Transport`. Whether freight moves by highway (`Truck`) or sea lanes (`Ship`), the higher-level shipment workflow remains identical: acquire a vehicle, assign the cargo, and dispatch it to the destination. The **Factory Method** pattern perfectly addresses this by defining an abstract creator (`Logistics`) with a template workflow (`planDelivery`), deferring the concrete choice of vehicle instantiation to specialized creator subclasses (`RoadLogistics`, `SeaLogistics`). This enforces the Open-Closed Principle: introducing new transport modes requires zero modifications to the core delivery workflow.

### Why Abstract Factory Fits the UI Part
User interface controls rarely exist in isolation; they belong to coherent aesthetic and functional ecosystems (families). A button and a checkbox rendered in a single application window must strictly adhere to the same operating system conventions. The **Abstract Factory** pattern (`GUIFactory`) guarantees family consistency by declaring creation methods for both `Button` and `Checkbox`. Concrete factories (`WindowsFactory`, `MacOSFactory`) ensure that Windows components are never mismatched with macOS components. The client (`DeliveryApplication`) interacts purely with product interfaces, completely shielded from platform-specific instantiation logic.

---

## 2. UML Class Diagrams

### 2.1 Factory Method Pattern
The diagram below illustrates the separation between the `Logistics` creator hierarchy and the `Transport` product hierarchy. The creator delegates object instantiation to the abstract method `createTransport()`.

```
+-------------------------------------------------------------------------+
|                  Factory Method Pattern (com.logistics)                 |
+-------------------------------------------------------------------------+
|                                                                         |
|   +-----------------------+              +--------------------------+   |
|   | <<abstract, Creator>> |   <<uses>>   |  <<interface, Product>>  |   |
|   |       Logistics       |------------->|        Transport         |   |
|   +-----------------------+              +--------------------------+   |
|   |+createTransport():Tr. |              |+deliver(cargo,dest):void |   |
|   |+planDelivery(c,d):void|              +--------------------------+   |
|   +-----------------------+                           ^                 |
|               ^                                       |                 |
|        +------+------+                         +------+------+          |
|        |             |                         |             |          |
|  +-----------+ +-----------+             +-----------+ +-----------+    |
|  |RoadLogist.| |SeaLogist. |             |   Truck   | |   Ship    |    |
|  +-----------+ +-----------+             +-----------+ +-----------+    |
|  |+createTr()| |+createTr()|             |+deliver() | |+deliver() |    |
|  +-----------+ +-----------+             +-----------+ +-----------+    |
|        |             |                         ^             ^          |
|        |  <<creates>>|                         |             |          |
|        +-------------|-------------------------+             |          |
|                      +---------------------------------------+          |
+-------------------------------------------------------------------------+
```

### 2.2 Abstract Factory Pattern
The diagram below details the client, abstract factory, and multi-family product relationships.

```
+-----------------------------------------------------------------------------------+
|                        Abstract Factory Pattern (com.logistics)                   |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  +-------------------------+                 +-------------------------------+    |
|  |       <<Client>>        |    <<uses>>     | <<interface, AbstractFactory>>|    |
|  |   DeliveryApplication   |---------------->|          GUIFactory           |    |
|  +-------------------------+                 +-------------------------------+    |
|  |- button: Button         |                 |+ createButton(): Button       |    |
|  |- checkbox: Checkbox     |                 |+ createCheckbox(): Checkbox   |    |
|  |- logistics: Logistics   |                 +-------------------------------+    |
|  +-------------------------+                                 ^                    |
|  |+ renderUI(): void       |                         +-------+-------+            |
|  |+ planDelivery(c,d): void|                         |               |            |
|  |+ run(c,d): void         |                 +---------------+ +---------------+  |
|  +-------------------------+                 |WindowsFactory | | MacOSFactory  |  |
|         |           |                        +---------------+ +---------------+  |
|         v           v                        |+createButton()| |+createButton()|  |
|    +---------+ +------------+                |+createCheck() | |+createCheck() |  |
|    | Button  | |  Checkbox  |                +---------------+ +---------------+  |
|    +---------+ +------------+                        |                 |          |
|         ^            ^                       <<creates>>       <<creates>>        |
|    +----+---+   +----+---+                           |                 |          |
|    |        |   |        |                   +-------+         +-------+          |
|  +----+   +----+----+  +----+                v                 v                  |
|  |Win |   |Mac |Win |  |Mac |        [WindowsButton]     [MacOSButton]            |
|  |Btn |   |Btn |Chk |  |Chk |        [WindowsCheckbox]   [MacOSCheckbox]          |
|  +----+   +----+----+  +----+                                                     |
+-----------------------------------------------------------------------------------+
```

---

## 3. Clean Code Evidence (Section 7)

### Practice 1: Meaningful Names
- **Excerpt from `StartupHelper.java` and `creator/`:**
  ```java
  public class RoadLogistics extends Logistics {
      @Override
      public Transport createTransport() {
          return new Truck();
      }
  }
  ```
- **Explanation & Benefit:** Class and method names explicitly convey their design pattern roles and domain context (`RoadLogistics` clearly identifies a concrete creator for road freight; `createTransport` declares its factory responsibility). This prevents vague names like `TransportManager` or `DeliveryHandler`, facilitating immediate codebase comprehension.

### Practice 2: Small Methods (Single Responsibility Principle)
- **Excerpt from `DeliveryApplication.java`:**
  ```java
  public void renderUI() {
      button.paint();
      checkbox.paint();
  }

  public void planDelivery(String cargo, String destination) {
      logistics.planDelivery(cargo, destination);
  }
  ```
- **Explanation & Benefit:** Each method performs one singular, well-defined function. UI rendering is strictly decoupled from logistics planning. This granularity eases unit testing, simplifies maintenance, and adheres to Martin's rule: *"Methods should do one thing. They should do it well. They should do it only."*

### Practice 3: Avoid Duplicated Logic (DRY Principle)
- **Excerpt from `Logistics.java`:**
  ```java
  public void planDelivery(String cargo, String destination) {
      Objects.requireNonNull(cargo, "Cargo cannot be null");
      Objects.requireNonNull(destination, "Destination cannot be null");

      Transport transport = createTransport();
      if (transport == null) {
          throw new IllegalStateException("Factory method returned null transport");
      }
      transport.deliver(cargo, destination);
  }
  ```
- **Explanation & Benefit:** The orchestration logic (validating inputs, acquiring the product via the factory method, verifying instance integrity, and invoking the delivery contract) is written exactly once in the base `Logistics` class. Concrete creators (`RoadLogistics`, `SeaLogistics`) only define transport instantiation, eliminating duplicate control code.

### Practice 4: Data Abstraction (Clean Code, Chapter 6)
- **Excerpt from `DeliveryApplication.java`:**
  ```java
  public class DeliveryApplication {
      private final Button button;
      private final Checkbox checkbox;
      private final Logistics logistics;

      public DeliveryApplication(GUIFactory factory, Logistics logistics) {
          this.button = factory.createButton();
          this.checkbox = factory.createCheckbox();
          this.logistics = logistics;
      }
  }
  ```
- **Explanation & Benefit:** Martin notes in Chapter 6 that abstractions hide implementation details behind interfaces rather than exposing data. The client holds references exclusively to `Button`, `Checkbox`, `GUIFactory`, and `Logistics`. It is entirely oblivious to whether the operating system is Windows or macOS, or whether transport is via asphalt or sea lanes.

### Practice 5: Objects and Encapsulation (Clean Code, Chapter 6)
- **Excerpt from `Truck.java`:**
  ```java
  public class Truck implements Transport {
      @Override
      public void deliver(String cargo, String destination) {
          Objects.requireNonNull(cargo, "Cargo must not be null");
          Objects.requireNonNull(destination, "Destination must not be null");
          System.out.println("Truck delivers " + cargo + " to " + destination);
      }
  }
  ```
- **Explanation & Benefit:** In Clean Code Chapter 6, Martin contrasts procedural data structures (which expose variables without behavior) with true objects (which hide their data and expose behavior). Our products do not expose internal states through arbitrary getters and setters; they expose meaningful behavior via `deliver(...)` and `paint()`, preserving strict encapsulation.

---

## 4. Verification Evidence (Section 6)

All six required checks plus missing-input testing were executed and confirmed.

### 4.1 Verification Results Table

| Check | Input Configuration | Expected Output | Actual Console Result | Pass/Fail |
|:---:|:---|:---|:---|:---:|
| **1** | `ROAD + WINDOWS` | Truck delivery; Windows button & checkbox | `Rendering Windows button`<br>`Rendering Windows checkbox`<br>`Truck delivers laboratory equipment to Aktau warehouse` | **PASS** |
| **2** | `SEA + WINDOWS` | Ship delivery; Windows button & checkbox | `Rendering Windows button`<br>`Rendering Windows checkbox`<br>`Ship delivers laboratory equipment to Aktau warehouse` | **PASS** |
| **3** | `ROAD + MACOS` | Truck delivery; macOS button & checkbox | `Rendering macOS button`<br>`Rendering macOS checkbox`<br>`Truck delivers laboratory equipment to Aktau warehouse` | **PASS** |
| **4** | `SEA + MACOS` | Ship delivery; macOS button & checkbox | `Rendering macOS button`<br>`Rendering macOS checkbox`<br>`Ship delivers laboratory equipment to Aktau warehouse` | **PASS** |
| **5** | `AIR + WINDOWS`<br>*(Unsupported delivery)* | Clear validation message; no delivery executed | `Validation Error: Unsupported delivery mode 'AIR'. Supported modes: ROAD, SEA.` | **PASS** |
| **6** | `ROAD + LINUX`<br>*(Unsupported platform)* | Clear validation message; no UI constructed | `Validation Error: Unsupported UI platform 'LINUX'. Supported platforms: WINDOWS, MACOS.` | **PASS** |
| **7** | `Missing Input`<br>*(No arguments / empty)* | Clear validation message; clean program exit | `Validation Error: Missing required configuration arguments.` | **PASS** |

### 4.2 Automated Test Suite Execution
Automated regression tests run through JUnit 5 (`mvn test`):
```text
[INFO] Running com.logistics.DeliveryApplicationTest
[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running com.logistics.AbstractFactoryTest
[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running com.logistics.ValidationTest
[INFO] Tests run: 13, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running com.logistics.FactoryMethodTest
[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0
[INFO] -------------------------------------------------------
[INFO] Results: Tests run: 27, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

---

## 5. Conclusion & Design Reflection

### 5.1 Pattern Comparison
- **Simple Factory:** A non-GoF idiom utilizing a single monolithic method with conditional branches (`switch`/`if`) to instantiate classes. Modifying or expanding the product catalog violates OCP.
- **Factory Method:** Employs inheritance. An abstract creator defines a factory method signature, delegating instantiation to subclasses. Ideal for managing a single product hierarchy where workflows are shared.
- **Abstract Factory:** Employs object composition. An abstract factory interface defines creation methods for a suite of related products. Guarantees consistency across product families without leaking concrete classes to clients.

### 5.2 Design Reflection: System Extensibility

#### 1. Adding a New Transport (e.g., Air Logistics / Plane)
- **Classes to Add:** `Plane implements Transport` in `com.logistics.transport`; `AirLogistics extends Logistics` in `com.logistics.creator`. Add `AIR` to `DeliveryMode` enum and update `StartupHelper.createLogistics()`.
- **Existing Classes:** `Transport`, `Truck`, `Ship`, `Logistics`, `RoadLogistics`, `SeaLogistics`, and `DeliveryApplication` require zero code changes (100% Open-Closed).

#### 2. Adding a New UI Family (e.g., Linux Desktop)
- **Classes to Add:** `LinuxButton implements Button`, `LinuxCheckbox implements Checkbox`, and `LinuxFactory implements GUIFactory`. Add `LINUX` to `UIPlatform` enum and update `StartupHelper.createGUIFactory()`.
- **Existing Classes:** `Button`, `Checkbox`, `GUIFactory`, `WindowsFactory`, `MacOSFactory`, and `DeliveryApplication` remain completely untouched.

#### 3. Adding a New UI Product Type (e.g., TextField)
- **Modifications Required:**
  1. Define interface `com.logistics.ui.TextField` with `void paint()`.
  2. Modify `GUIFactory` interface to include `TextField createTextField()`.
  3. Update existing `WindowsFactory` and `MacOSFactory` to implement `createTextField()`.
  4. Implement `WindowsTextField` and `MacOSTextField`.
  5. Update `DeliveryApplication` to request and paint the new text field.
- **Trade-off Analysis:** While Abstract Factory excels at adding new product families, introducing new product types requires modifying the abstract factory interface and every concrete factory implementation.

---

## 6. References
1. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
2. Freeman, E., & Robson, E. (2020). *Head First Design Patterns: Building Extensible and Maintainable Object-Oriented Software* (2nd ed.). O'Reilly Media. Chapter 4: The Factory Pattern.
3. Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. Chapter 6: Objects and Data Structures.
4. Bekenov, Y. (2026). *Software Design Patterns - Lecture 2: Factory Method and Abstract Factory*. Astana IT University.
