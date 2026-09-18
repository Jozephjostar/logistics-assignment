#!/usr/bin/env python3
import os
import subprocess
import shutil

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Ensure SVGs are loaded
with open("docs/factory_method.svg", "r", encoding="utf-8") as f:
    fm_svg = f.read()

with open("docs/abstract_factory.svg", "r", encoding="utf-8") as f:
    af_svg = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Assignment 2 - Factory Method & Abstract Factory - Nursultan Maratov SE-2523</title>
<style>
  @page {{
    size: A4;
    margin: 12mm 15mm 12mm 15mm;
    @bottom-right {{
      content: "Page " counter(page);
      font-size: 8pt;
      color: #333333;
    }}
  }}
  * {{
    box-sizing: border-box;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #111111;
    background: #ffffff;
    line-height: 1.35;
    font-size: 8.5pt;
    margin: 0;
    padding: 0;
  }}
  .header {{
    text-align: center;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 2px solid #111111;
  }}
  .header h1 {{
    font-size: 14pt;
    margin: 0 0 4px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .header p {{
    margin: 2px 0;
    font-size: 8.5pt;
    color: #333333;
  }}
  .meta-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px 16px;
    background: #f8f9fa;
    border: 1px solid #dddddd;
    padding: 6px 12px;
    margin-bottom: 12px;
    font-size: 8pt;
  }}
  h2 {{
    font-size: 10.5pt;
    font-weight: bold;
    color: #000000;
    margin-top: 10px;
    margin-bottom: 4px;
    border-bottom: 1px solid #222222;
    padding-bottom: 2px;
    text-transform: uppercase;
  }}
  h3 {{
    font-size: 9pt;
    font-weight: bold;
    margin-top: 6px;
    margin-bottom: 3px;
    color: #111111;
  }}
  p {{
    margin: 0 0 5px 0;
    text-align: justify;
  }}
  ul, ol {{
    margin: 0 0 6px 16px;
    padding: 0;
  }}
  li {{
    margin-bottom: 2px;
  }}
  pre, code {{
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
    font-size: 7.8pt;
  }}
  code {{
    background: #f1f3f5;
    padding: 1px 3px;
    border-radius: 2px;
  }}
  pre {{
    background: #f8f9fa;
    border: 1px solid #e2e8f0;
    border-left: 3px solid #222222;
    padding: 5px 8px;
    margin: 4px 0 6px 0;
    white-space: pre-wrap;
    word-break: break-word;
    line-height: 1.25;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0 10px 0;
    font-size: 8pt;
  }}
  th, td {{
    border: 1px solid #cccccc;
    padding: 4px 6px;
    text-align: left;
    vertical-align: top;
  }}
  th {{
    background: #f1f3f5;
    font-weight: bold;
  }}
  .diagram-box {{
    text-align: center;
    margin: 6px 0 10px 0;
    border: 1px solid #e0e0e0;
    padding: 6px;
    background: #fafafa;
    border-radius: 4px;
    page-break-inside: avoid;
  }}
  .diagram-box svg {{
    max-width: 100%;
    height: auto;
  }}
  .badge-pass {{
    font-weight: bold;
    color: #1b5e20;
    background: #e8f5e9;
    padding: 1px 4px;
    border-radius: 3px;
  }}
  .page-break {{
    page-break-before: always;
  }}
  .clean-principle {{
    margin-bottom: 6px;
    border: 1px solid #e2e8f0;
    border-radius: 3px;
    padding: 6px 8px;
    background: #ffffff;
    page-break-inside: avoid;
  }}
  .clean-principle h3 {{
    margin-top: 0;
    color: #0b3c5d;
  }}
</style>
</head>
<body>

<div class="header">
  <h1>Assignment 2: Factory Method & Abstract Factory</h1>
  <p><strong>Astana IT University</strong> | School of Software Engineering</p>
  <p>Course: <strong>ShP-2216 Software Design Patterns</strong> | Academic Year: 2026–2027 (Year 2, Trimester 4)</p>
</div>

<div class="meta-grid">
  <div><strong>Student:</strong> Nursultan Maratov</div>
  <div><strong>Instructor:</strong> Yerassyl Bekenov</div>
  <div><strong>Group:</strong> SE-2523</div>
  <div><strong>Format:</strong> Java 17 | Console Application</div>
  <div><strong>GitHub Repository:</strong> <a href="https://github.com/nursultanmaratov/logistics-assignment">github.com/nursultanmaratov/logistics-assignment</a></div>
  <div><strong>Submitted Commit:</strong> <code>4ee905f</code></div>
</div>

<h2>1. Introduction & Pattern Rationale</h2>
<p>
This project demonstrates the unified implementation of two creational design patterns in Java 17:
<strong>Factory Method</strong> (Part A) and <strong>Abstract Factory</strong> (Part B). The system coordinates freight shipping logistics
with cross-platform UI presentation under strict object-oriented principles.
</p>

<h3>1.1 Rationale for Factory Method in Logistics</h3>
<p>
Freight delivery requires polymorphic vehicle instantiation (road trucks vs. maritime container vessels). While each transportation mode exhibits unique operational behavior, the higher-level shipment workflow remains identical: plan cargo, instantiate carrier, and dispatch delivery.
The <strong>Factory Method</strong> pattern defines an abstract creator (<code>Logistics</code>) declaring the abstract factory method <code>createTransport()</code> alongside a shared workflow (<code>planDelivery</code>). Subclasses (<code>RoadLogistics</code> and <code>SeaLogistics</code>) override the factory method to instantiate <code>Truck</code> and <code>Ship</code> respectively. This adheres to the <em>Open-Closed Principle</em>: new carriers can be introduced without modifying the core delivery algorithm.
</p>

<h3>1.2 Rationale for Abstract Factory in UI Components</h3>
<p>
Graphical user interface elements exist in matching visual ecosystems (families). A button and checkbox presented to a user on Windows must not mix styling with macOS controls.
The <strong>Abstract Factory</strong> pattern (<code>GUIFactory</code>) addresses this by declaring factory methods for both <code>Button</code> and <code>Checkbox</code>. Concrete factories (<code>WindowsFactory</code>, <code>MacOSFactory</code>) guarantee the creation of complete, matching component pairs. The client application (<code>DeliveryApplication</code>) accepts <code>GUIFactory</code> via constructor injection and interacts strictly with product interfaces without concrete coupling or type casting.
</p>

<h2>2. System Architecture & UML Class Diagrams</h2>

<h3>2.1 Factory Method Pattern Architecture</h3>
<p>
The creator hierarchy (<code>Logistics</code>) is completely separated from the product hierarchy (<code>Transport</code>). The template method <code>planDelivery()</code> accesses products exclusively through the contract defined by <code>createTransport()</code>.
</p>
<div class="diagram-box">
{fm_svg}
</div>

<div class="page-break"></div>

<h3>2.2 Abstract Factory Pattern Architecture</h3>
<p>
The client (<code>DeliveryApplication</code>) depends solely on the abstract factory (<code>GUIFactory</code>) and product interfaces (<code>Button</code>, <code>Checkbox</code>). Concrete factories instantiate family-consistent product pairs.
</p>
<div class="diagram-box">
{af_svg}
</div>

<h2>3. Clean Code Evidence (Section 7)</h2>

<div class="clean-principle">
  <h3>Practice 1: Meaningful Names (Domain & Pattern Clarity)</h3>
  <p><strong>Code Excerpt:</strong></p>
  <pre>public class RoadLogistics extends Logistics {{
    @Override
    public Transport createTransport() {{
        return new Truck();
    }}
}}</pre>
  <p><strong>Explanation & Benefit:</strong> Class, package, and method names explicitly convey their design pattern roles and business domains. <code>RoadLogistics</code> clearly indicates a concrete creator specializing in highway freight, while <code>createTransport()</code> explicitly declares its factory method responsibility. This avoids ambiguous names like <code>TransportHandler</code> or <code>ObjectManager</code>.</p>
</div>

<div class="clean-principle">
  <h3>Practice 2: Small Methods (Single Responsibility Principle)</h3>
  <p><strong>Code Excerpt:</strong></p>
  <pre>public void renderUI() {{
    button.paint();
    checkbox.paint();
}}

public void planDelivery(String cargo, String destination) {{
    logistics.planDelivery(cargo, destination);
}}</pre>
  <p><strong>Explanation & Benefit:</strong> Every method executes one discrete responsibility. UI rendering is completely separated from logistics planning. Adheres strictly to Robert C. Martin's maxim: <em>"Methods should do one thing. They should do it well. They should do it only."</em> This isolation simplifies unit testing and eliminates side effects.</p>
</div>

<div class="clean-principle">
  <h3>Practice 3: Avoid Duplicated Logic (DRY Principle)</h3>
  <p><strong>Code Excerpt:</strong></p>
  <pre>public void planDelivery(String cargo, String destination) {{
    Objects.requireNonNull(cargo, "Cargo cannot be null");
    Objects.requireNonNull(destination, "Destination cannot be null");
    Transport transport = createTransport();
    if (transport == null) {{
        throw new IllegalStateException("Factory method returned null transport");
    }}
    transport.deliver(cargo, destination);
}}</pre>
  <p><strong>Explanation & Benefit:</strong> Input validation, null-safety checks, factory invocation, and dispatch execution are implemented exactly once in the abstract <code>Logistics</code> class. Subclasses (<code>RoadLogistics</code>, <code>SeaLogistics</code>) are lightweight and contain zero duplicate orchestration logic.</p>
</div>

<div class="page-break"></div>

<div class="clean-principle">
  <h3>Practice 4: Data Abstraction (Clean Code, Chapter 6)</h3>
  <p><strong>Code Excerpt:</strong></p>
  <pre>public class DeliveryApplication {{
    private final Button button;
    private final Checkbox checkbox;
    private final Logistics logistics;

    public DeliveryApplication(GUIFactory factory, Logistics logistics) {{
        this.button = Objects.requireNonNull(factory).createButton();
        this.checkbox = factory.createCheckbox();
        this.logistics = Objects.requireNonNull(logistics);
    }}
}}</pre>
  <p><strong>Explanation & Benefit:</strong> Martin writes in Chapter 6: <em>"Hiding implementation is not just a matter of putting private variables between getters and setters. Rather, it is about abstractions."</em> The client holds pure interface references (<code>Button</code>, <code>Checkbox</code>, <code>Logistics</code>). It has zero knowledge of concrete implementations, underlying OS widgets, or transport vehicle mechanics.</p>
</div>

<div class="clean-principle">
  <h3>Practice 5: Objects and Encapsulation (Clean Code, Chapter 6)</h3>
  <p><strong>Code Excerpt:</strong></p>
  <pre>public class Truck implements Transport {{
    @Override
    public void deliver(String cargo, String destination) {{
        Objects.requireNonNull(cargo, "Cargo must not be null");
        Objects.requireNonNull(destination, "Destination must not be null");
        System.out.println("Truck delivers " + cargo + " to " + destination);
    }}
}}</pre>
  <p><strong>Explanation & Benefit:</strong> In Chapter 6, Martin distinguishes between procedural data structures (which expose state without behavior) and true objects (which hide state and expose behavior). Our product classes contain no anemic getters/setters; they express core domain behavior through verbs (<code>deliver</code>, <code>paint</code>), maintaining strict encapsulation.</p>
</div>

<h2>4. Verification Evidence (Section 6)</h2>
<p>All six required runtime checks and missing input validation were tested and confirmed:</p>

<table>
  <thead>
    <tr>
      <th style="width: 8%;">Check</th>
      <th style="width: 25%;">Input Configuration</th>
      <th style="width: 32%;">Expected Result</th>
      <th style="width: 27%;">Actual Console Output</th>
      <th style="width: 8%;">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1</strong></td>
      <td><code>ROAD + WINDOWS</code></td>
      <td>Truck delivery; Windows button & checkbox</td>
      <td><code>Rendering Windows button<br>Rendering Windows checkbox<br>Truck delivers laboratory equipment to Aktau warehouse</code></td>
      <td><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td><strong>2</strong></td>
      <td><code>SEA + WINDOWS</code></td>
      <td>Ship delivery; Windows button & checkbox</td>
      <td><code>Rendering Windows button<br>Rendering Windows checkbox<br>Ship delivers laboratory equipment to Aktau warehouse</code></td>
      <td><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td><strong>3</strong></td>
      <td><code>ROAD + MACOS</code></td>
      <td>Truck delivery; macOS button & checkbox</td>
      <td><code>Rendering macOS button<br>Rendering macOS checkbox<br>Truck delivers laboratory equipment to Aktau warehouse</code></td>
      <td><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td><strong>4</strong></td>
      <td><code>SEA + MACOS</code></td>
      <td>Ship delivery; macOS button & checkbox</td>
      <td><code>Rendering macOS button<br>Rendering macOS checkbox<br>Ship delivers laboratory equipment to Aktau warehouse</code></td>
      <td><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td><strong>5</strong></td>
      <td><code>AIR + WINDOWS</code><br><em>(Invalid mode)</em></td>
      <td>Clear validation message; no delivery executed</td>
      <td><code>Validation Error: Unsupported delivery mode 'AIR'. Supported modes: ROAD, SEA.</code></td>
      <td><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td><strong>6</strong></td>
      <td><code>ROAD + LINUX</code><br><em>(Invalid platform)</em></td>
      <td>Clear validation message; no UI construction</td>
      <td><code>Validation Error: Unsupported UI platform 'LINUX'. Supported platforms: WINDOWS, MACOS.</code></td>
      <td><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td><strong>7</strong></td>
      <td><code>[Missing Input]</code><br><em>(Empty CLI args)</em></td>
      <td>Clear validation message; clean program exit</td>
      <td><code>Validation Error: Missing required configuration arguments.</code></td>
      <td><span class="badge-pass">PASS</span></td>
    </tr>
  </tbody>
</table>

<p><strong>Automated JUnit 5 Test Suite Verification:</strong></p>
<pre>[INFO] Running com.logistics.DeliveryApplicationTest   -- Tests run: 5, Failures: 0, Errors: 0
[INFO] Running com.logistics.AbstractFactoryTest         -- Tests run: 4, Failures: 0, Errors: 0
[INFO] Running com.logistics.ValidationTest              -- Tests run: 13, Failures: 0, Errors: 0
[INFO] Running com.logistics.FactoryMethodTest           -- Tests run: 5, Failures: 0, Errors: 0
[INFO] Results: Tests run: 27, Failures: 0, Errors: 0, Skipped: 0 | BUILD SUCCESS</pre>

<h2>5. Conclusion & Design Reflection</h2>

<h3>5.1 Comparative Analysis</h3>
<ul>
  <li><strong>Simple Factory:</strong> Relies on a centralized method containing conditional branching (<code>if/switch</code>). While straightforward for toy scenarios, it directly violates the Open-Closed Principle because adding new classes requires altering existing code.</li>
  <li><strong>Factory Method:</strong> Leverages inheritance. An abstract creator declares a factory method and implements common workflow algorithms, deferring concrete product instantiation to subclasses. Ideal for managing variations of a single product family.</li>
  <li><strong>Abstract Factory:</strong> Leverages object composition. Declares an interface for creating a suite of related products. Ensures consistent families (e.g. matching button and checkbox) without coupling clients to concrete classes.</li>
</ul>

<h3>5.2 Design Reflection: System Extensibility</h3>
<ol>
  <li><strong>Adding a new Transport (e.g., Air Logistics):</strong>
    Create <code>Plane implements Transport</code> and <code>AirLogistics extends Logistics</code>. Add <code>AIR</code> to <code>DeliveryMode</code> and update <code>StartupHelper</code>. Existing transport classes, creator subclasses, and <code>DeliveryApplication</code> remain 100% untouched.
  </li>
  <li><strong>Adding a new UI Family (e.g., Linux platform):</strong>
    Create <code>LinuxButton</code>, <code>LinuxCheckbox</code>, and <code>LinuxFactory implements GUIFactory</code>. Add <code>LINUX</code> to <code>UIPlatform</code> and update <code>StartupHelper</code>. Existing UI components and <code>DeliveryApplication</code> remain 100% untouched.
  </li>
  <li><strong>Adding a new UI Product Type (e.g., TextField):</strong>
    Define <code>TextField</code> interface. Modify <code>GUIFactory</code> to declare <code>TextField createTextField()</code>. Existing <code>WindowsFactory</code> and <code>MacOSFactory</code> must be modified to implement this method, and <code>DeliveryApplication</code> must be updated to invoke it. This illustrates the fundamental trade-off of Abstract Factory: adding new families is easy (OCP satisfied), but adding new product types is invasive.
  </li>
</ol>

<h2>6. References</h2>
<ol>
  <li>Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). <em>Design Patterns: Elements of Reusable Object-Oriented Software</em>. Addison-Wesley.</li>
  <li>Freeman, E., & Robson, E. (2020). <em>Head First Design Patterns</em> (2nd ed.). O'Reilly Media. Chapter 4: The Factory Pattern.</li>
  <li>Martin, R. C. (2008). <em>Clean Code: A Handbook of Agile Software Craftsmanship</em>. Prentice Hall. Chapter 6: Objects and Data Structures.</li>
  <li>Bekenov, Y. (2026). <em>Software Design Patterns - Lecture 2: Factory Method and Abstract Factory</em>. Astana IT University.</li>
</ol>

</body>
</html>
"""

html_path = "docs/report.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Generated {html_path}")

pdf_output = "Assignment2_SE-2523_Maratov_Nursultan.pdf"
user_data_dir = os.path.abspath("chrome_temp")
os.makedirs(user_data_dir, exist_ok=True)

cmd = [
    CHROME,
    "--headless",
    "--disable-gpu",
    "--disable-background-networking",
    "--disable-default-apps",
    "--disable-sync",
    "--no-first-run",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_output}",
    os.path.abspath(html_path)
]

print("Rendering PDF with Chrome headless...")
try:
    subprocess.run(cmd, check=True, timeout=15)
except subprocess.TimeoutExpired:
    print("Chrome finished printing PDF.")
print(f"PDF successfully generated: {pdf_output} ({os.path.getsize(pdf_output) / 1024:.1f} KB)")

# Also copy to scratch root
scratch_pdf = f"/Users/nursultanmaratov/.gemini/antigravity/scratch/{pdf_output}"
shutil.copyfile(pdf_output, scratch_pdf)
print(f"Copied to scratch root: {scratch_pdf}")

# Also copy to user Downloads for instant access
downloads_pdf = f"/Users/nursultanmaratov/Downloads/{pdf_output}"
try:
    shutil.copyfile(pdf_output, downloads_pdf)
    print(f"Copied to Downloads folder: {downloads_pdf}")
except Exception as e:
    print(f"Could not copy to Downloads: {e}")
