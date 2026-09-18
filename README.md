# Logistics Application: Factory Method & Abstract Factory

**Course:** ShP-2216 Software Design Patterns  
**Institution:** Astana IT University | School of Software Engineering  
**Academic Year:** 2026–2027 | Year 2, Trimester 4  
**Student:** Nursultan Maratov (Group: SE-2523)  
**Instructor:** Yerassyl Bekenov  

---

## 1. Project Purpose

This application demonstrates the combined application of two fundamental creational design patterns:
1. **Factory Method Pattern (Part A):** Decouples logistics planning (`Logistics`) from concrete transportation mechanisms (`Truck` for road freight, `Ship` for maritime container shipping). Subclasses (`RoadLogistics`, `SeaLogistics`) decide which concrete transport class to instantiate.
2. **Abstract Factory Pattern (Part B):** Provides an interface (`GUIFactory`) to create families of related or dependent cross-platform UI components (`Button`, `Checkbox`) for Windows and macOS platforms without specifying their concrete classes (`WindowsFactory`, `MacOSFactory`).

The client (`DeliveryApplication`) coordinates both workflows using constructor dependency injection, operating strictly against abstract contracts without runtime branching (`instanceof`) or concrete casts.

---

## 2. Package & Directory Structure

```
logistics-assignment/
├── pom.xml                               # Maven build configuration (Java 17 target)
├── .gitignore                            # Git ignore rules
├── README.md                             # Project documentation & run manual
├── REPORT.md                             # English assignment report
├── DEFENSE_GUIDE.md                      # Comprehensive defense preparation guide (D1–D6)
├── docs/
│   ├── factory_method.puml               # PlantUML source for Factory Method
│   ├── factory_method.svg                # Vector diagram for Factory Method
│   ├── abstract_factory.puml             # PlantUML source for Abstract Factory
│   └── abstract_factory.svg              # Vector diagram for Abstract Factory
├── scripts/
│   ├── generate_diagrams.py              # Generates standalone SVG class diagrams
│   ├── package_jar.py                    # Packages the compiled classes into executable JAR
│   └── generate_report_pdf.py            # Generates submission-ready PDF report via Chrome Headless
├── src/
│   ├── main/java/com/logistics/
│   │   ├── transport/                    # Factory Method: Product hierarchy
│   │   │   ├── Transport.java            # Product interface (void deliver(cargo, destination))
│   │   │   ├── Truck.java                # Concrete product (road freight)
│   │   │   └── Ship.java                 # Concrete product (sea container vessel)
│   │   ├── creator/                      # Factory Method: Creator hierarchy
│   │   │   ├── Logistics.java            # Abstract creator with template workflow planDelivery()
│   │   │   ├── RoadLogistics.java        # Concrete creator returning Truck
│   │   │   └── SeaLogistics.java         # Concrete creator returning Ship
│   │   ├── ui/                           # Abstract Factory: Product interfaces & factory
│   │   │   ├── Button.java               # Abstract product interface (void paint())
│   │   │   ├── Checkbox.java             # Abstract product interface (void paint())
│   │   │   ├── GUIFactory.java           # Abstract factory interface
│   │   │   ├── windows/                  # Windows component family
│   │   │   │   ├── WindowsButton.java    # Concrete Windows button
│   │   │   │   ├── WindowsCheckbox.java  # Concrete Windows checkbox
│   │   │   │   └── WindowsFactory.java   # Concrete Windows factory
│   │   │   └── macos/                    # macOS component family
│   │   │       ├── MacOSButton.java      # Concrete macOS button
│   │   │       ├── MacOSCheckbox.java    # Concrete macOS checkbox
│   │   │       └── MacOSFactory.java     # Concrete macOS factory
│   │   └── app/                          # Client and Startup integration
│   │       ├── DeliveryApplication.java  # Client application consuming factories
│   │       ├── DeliveryMode.java         # Enum: ROAD, SEA (case-insensitive parser)
│   │       ├── UIPlatform.java           # Enum: WINDOWS, MACOS (case-insensitive parser)
│   │       ├── StartupHelper.java        # Input validation and factory selector
│   │       └── Main.java                 # CLI & interactive entry point
│   └── test/java/com/logistics/
│       ├── FactoryMethodTest.java        # Tests creator polymorphism & delivery workflow
│       ├── AbstractFactoryTest.java      # Tests UI families & matching component pairs
│       ├── DeliveryApplicationTest.java  # Tests all 4 valid runtime configurations
│       └── ValidationTest.java           # Tests error handling for checks 5, 6, and missing input
```

---

## 3. Prerequisites

- **Java Development Kit (JDK):** Version 17 or higher (Java 17, 21, etc.).
- **Build Tool:** Apache Maven 3.8+ (or IntelliJ IDEA built-in Maven).
- **Python 3:** Version 3.10+ (used for diagram and report generation scripts).

---

## 4. Exact Build Instructions

### Compile the project:
```bash
mvn clean compile
```

### Run automated unit tests:
```bash
mvn test
```
*Expected: 27 tests run, 0 failures, 0 errors.*

### Package into runnable JAR:
```bash
python3 scripts/package_jar.py
```
This generates `target/logistics-assignment-1.0.0.jar`.

---

## 5. Exact Run Instructions

### Option A: Command-Line Arguments (Positional or Flags)

```bash
# Positional syntax: java -jar <jar-file> <DELIVERY_MODE> <UI_PLATFORM>
java -jar target/logistics-assignment-1.0.0.jar ROAD WINDOWS
java -jar target/logistics-assignment-1.0.0.jar SEA MACOS

# Flag syntax:
java -jar target/logistics-assignment-1.0.0.jar --delivery ROAD --platform MACOS
java -jar target/logistics-assignment-1.0.0.jar -d SEA -p WINDOWS
```

### Option B: Interactive Console Input

Run without parameters to activate guided prompts:
```bash
java -jar target/logistics-assignment-1.0.0.jar
```
Prompts:
```text
Enter delivery mode (ROAD or SEA): ROAD
Enter UI platform (WINDOWS or MACOS): WINDOWS
```

### Option C: Via Maven Exec Plugin

```bash
mvn compile exec:java -Dexec.args="ROAD WINDOWS"
```

---

## 6. Supported Input Values & Validation Behavior

| Parameter | Allowed Values (Case-Insensitive) | Invalid Example | Validation Behavior |
|---|---|---|---|
| **Delivery Mode** | `ROAD`, `SEA` | `AIR`, `TRAIN`, `""` | Prints clear validation error, stops execution cleanly (exit code 1). |
| **UI Platform** | `WINDOWS`, `MACOS` | `LINUX`, `WEB`, `""` | Prints clear validation error, stops execution cleanly (exit code 1). |
| **Missing Input** | Both required | No args provided | Displays error and usage syntax without silent default fallbacks. |

---

## 7. Sample Run

```bash
$ java -jar target/logistics-assignment-1.0.0.jar ROAD WINDOWS
Delivery mode: ROAD
UI platform: WINDOWS
Rendering Windows button
Rendering Windows checkbox
Truck delivers laboratory equipment to Aktau warehouse
```

---

## 8. Verification Results (Section 6 Checks)

| Check | Input | Actual Output | Status |
|:---:|:---|:---|:---:|
| **1** | `ROAD + WINDOWS` | Windows button, Windows checkbox, Truck delivery | **PASS** |
| **2** | `SEA + WINDOWS` | Windows button, Windows checkbox, Ship delivery | **PASS** |
| **3** | `ROAD + MACOS` | macOS button, macOS checkbox, Truck delivery | **PASS** |
| **4** | `SEA + MACOS` | macOS button, macOS checkbox, Ship delivery | **PASS** |
| **5** | `AIR + WINDOWS` | `Validation Error: Unsupported delivery mode 'AIR'. Supported modes: ROAD, SEA.` | **PASS** |
| **6** | `ROAD + LINUX` | `Validation Error: Unsupported UI platform 'LINUX'. Supported platforms: WINDOWS, MACOS.` | **PASS** |
| **7** | Missing Input | `Validation Error: Missing required configuration arguments.` | **PASS** |

---

## 9. Clean Code Summary

1. **Meaningful Names:** Clear domain roles (`RoadLogistics`, `WindowsFactory`, `DeliveryApplication`).
2. **Small Methods:** Single responsibility for rendering, workflow planning, argument parsing.
3. **Avoid Duplicated Logic (DRY):** `Logistics.planDelivery(...)` coordinates delivery uniformly.
4. **Data Abstraction (Clean Code Ch. 6):** Client interacts exclusively via `Transport`, `Button`, `Checkbox`, `GUIFactory`, `Logistics`.
5. **Objects & Encapsulation (Clean Code Ch. 6):** Objects express behavior (`deliver`, `paint`) rather than exposing internal data structures.
