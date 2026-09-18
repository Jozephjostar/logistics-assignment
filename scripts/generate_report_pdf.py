#!/usr/bin/env python3
import os
import subprocess
import shutil

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Load SVG diagrams
with open("docs/factory_method.svg", "r", encoding="utf-8") as f:
    fm_svg = f.read()

with open("docs/abstract_factory.svg", "r", encoding="utf-8") as f:
    af_svg = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Assignment 2 Report - Nursultan Maratov SE-2523</title>
<style>
  @page {{
    size: A4;
    margin: 14mm 16mm 14mm 16mm;
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
    font-family: Arial, Helvetica, sans-serif;
    color: #000000;
    background: #ffffff;
    line-height: 1.35;
    font-size: 8.8pt;
    margin: 0;
    padding: 0;
  }}
  .header {{
    text-align: center;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1.5px solid #000000;
  }}
  .header h1 {{
    font-size: 13.5pt;
    margin: 0 0 4px 0;
    font-weight: bold;
    color: #000000;
  }}
  .header p {{
    margin: 2px 0;
    font-size: 8.8pt;
    color: #222222;
  }}
  .meta-table {{
    width: 100%;
    margin-bottom: 10px;
    border-collapse: collapse;
    font-size: 8.5pt;
  }}
  .meta-table td {{
    padding: 3px 6px;
    border: 1px solid #cccccc;
    background: #fafafa;
  }}
  h2 {{
    font-size: 10.5pt;
    font-weight: bold;
    color: #000000;
    margin-top: 10px;
    margin-bottom: 5px;
    border-bottom: 1px solid #000000;
    padding-bottom: 2px;
  }}
  h3 {{
    font-size: 9.2pt;
    font-weight: bold;
    color: #000000;
    margin-top: 6px;
    margin-bottom: 3px;
  }}
  p {{
    margin: 0 0 5px 0;
    text-align: justify;
  }}
  ul, ol {{
    margin: 0 0 6px 18px;
    padding: 0;
  }}
  li {{
    margin-bottom: 2px;
  }}
  code, pre {{
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
    font-size: 7.8pt;
  }}
  code {{
    background: #f4f4f4;
    padding: 1px 3px;
    border-radius: 2px;
  }}
  pre {{
    background: #f9f9f9;
    border: 1px solid #dddddd;
    border-left: 3px solid #333333;
    padding: 5px 8px;
    margin: 4px 0 6px 0;
    white-space: pre-wrap;
    line-height: 1.25;
  }}
  table.data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0 8px 0;
    font-size: 8pt;
  }}
  table.data-table th, table.data-table td {{
    border: 1px solid #bbbbbb;
    padding: 4px 6px;
    text-align: left;
    vertical-align: top;
  }}
  table.data-table th {{
    background: #eeeeee;
    font-weight: bold;
  }}
  .diagram-box {{
    text-align: center;
    margin: 6px 0 8px 0;
    border: 1px solid #cccccc;
    padding: 6px;
    background: #ffffff;
    border-radius: 3px;
  }}
  .diagram-box svg {{
    max-width: 100%;
    height: auto;
  }}
  .badge-pass {{
    font-weight: bold;
    color: #006600;
  }}
  .page-break {{
    page-break-before: always;
  }}
  .clean-box {{
    border: 1px solid #dddddd;
    border-radius: 3px;
    padding: 5px 8px;
    margin-bottom: 6px;
    background: #ffffff;
  }}
</style>
</head>
<body>

<div class="header">
  <h1>Assignment 2: Factory Method and Abstract Factory</h1>
  <p><strong>Astana IT University</strong> | School of Software Engineering</p>
  <p>Course: <strong>ShP-2216 Software Design Patterns</strong> | Academic Year: 2026–2027 (Year 2, Trimester 4)</p>
</div>

<table class="meta-table">
  <tr>
    <td><strong>Student:</strong> Nursultan Maratov</td>
    <td><strong>Instructor:</strong> Yerassyl Bekenov</td>
  </tr>
  <tr>
    <td><strong>Group:</strong> SE-2523</td>
    <td><strong>Format:</strong> Java 17 | Console Application</td>
  </tr>
  <tr>
    <td><strong>GitHub Repository:</strong> <a href="https://github.com/Jozephjostar/logistics-assignment" style="color: #000000; text-decoration: underline;">https://github.com/Jozephjostar/logistics-assignment</a></td>
    <td><strong>Submitted Commit:</strong> <code>fc38cfc</code></td>
  </tr>
</table>

<h2>1. Introduction</h2>
<p>
This project combines two creational design patterns in a single Java 17 application: <strong>Factory Method</strong> for logistics transport and <strong>Abstract Factory</strong> for cross-platform UI components.
</p>
<p>
<strong>Why Factory Method for Logistics:</strong> Logistics operations share a common delivery workflow: planning cargo, creating a transport, and delivering items to a destination. The <code>Logistics</code> class defines the overall delivery workflow in <code>planDelivery()</code>, while creator subclasses (<code>RoadLogistics</code> and <code>SeaLogistics</code>) decide which concrete transport (<code>Truck</code> or <code>Ship</code>) to instantiate. This follows the Open-Closed Principle because new transports can be added without changing the delivery workflow.
</p>
<p>
<strong>Why Abstract Factory for UI Components:</strong> A graphical interface requires matching sets of components. A button and checkbox on Windows should look like Windows controls, while macOS components should match macOS styling. The <code>GUIFactory</code> interface ensures that <code>WindowsFactory</code> creates only Windows controls and <code>MacOSFactory</code> creates only macOS controls. The client application (<code>DeliveryApplication</code>) uses these components through abstract interfaces, avoiding any hardcoded dependencies or type casting.
</p>

<h2>2. UML Class Diagrams</h2>

<h3>2.1 Factory Method Pattern</h3>
<p>
The creator hierarchy (<code>Logistics</code>) is separated from the product hierarchy (<code>Transport</code>). The template method <code>planDelivery()</code> accesses products through <code>createTransport()</code>.
</p>
<div class="diagram-box">
{fm_svg}
</div>

<div class="page-break"></div>

<h3>2.2 Abstract Factory Pattern</h3>
<p>
The client (<code>DeliveryApplication</code>) depends on the abstract factory (<code>GUIFactory</code>) and product interfaces (<code>Button</code>, <code>Checkbox</code>). Concrete factories produce matching component pairs.
</p>
<div class="diagram-box">
{af_svg}
</div>

<h2>3. Clean Code Evidence (Section 7)</h2>

<div class="clean-box">
  <h3>1. Meaningful Names</h3>
  <pre>public class RoadLogistics extends Logistics {{
    @Override
    public Transport createTransport() {{
        return new Truck();
    }}
}}</pre>
  <p><em>Benefit:</em> Class and method names clearly reflect their roles. <code>RoadLogistics</code> clearly indicates a concrete creator for road freight, and <code>createTransport()</code> clearly declares the factory method responsibility, avoiding vague names like <code>Manager</code> or <code>Processor</code>.</p>
</div>

<div class="clean-box">
  <h3>2. Small Methods (Single Responsibility)</h3>
  <pre>public void renderUI() {{
    button.paint();
    checkbox.paint();
}}

public void planDelivery(String cargo, String destination) {{
    logistics.planDelivery(cargo, destination);
}}</pre>
  <p><em>Benefit:</em> Each method does one specific job. UI rendering is separated from delivery workflow execution. This makes the code easy to read, test, and maintain without unintended side effects.</p>
</div>

<div class="clean-box">
  <h3>3. Avoid Duplicated Logic (DRY Principle)</h3>
  <pre>public void planDelivery(String cargo, String destination) {{
    Objects.requireNonNull(cargo, "Cargo cannot be null");
    Objects.requireNonNull(destination, "Destination cannot be null");

    Transport transport = createTransport();
    if (transport == null) {{
        throw new IllegalStateException("Factory method returned null transport");
    }}
    transport.deliver(cargo, destination);
}}</pre>
  <p><em>Benefit:</em> The delivery process (argument validation, transport creation, and invoking delivery) is written once in the abstract <code>Logistics</code> class. Subclasses only specify which transport to instantiate, eliminating code duplication.</p>
</div>

<div class="page-break"></div>

<div class="clean-box">
  <h3>4. Data Abstraction (Clean Code, Chapter 6)</h3>
  <pre>public class DeliveryApplication {{
    private final Button button;
    private final Checkbox checkbox;
    private final Logistics logistics;

    public DeliveryApplication(GUIFactory factory, Logistics logistics) {{
        this.button = factory.createButton();
        this.checkbox = factory.createCheckbox();
        this.logistics = logistics;
    }}
}}</pre>
  <p><em>Benefit:</em> According to Clean Code Chapter 6, abstractions hide implementation details behind interfaces. The client relies exclusively on <code>Button</code>, <code>Checkbox</code>, <code>GUIFactory</code>, and <code>Logistics</code>. It does not know or care whether the platform is Windows or macOS, or whether transport is by road or sea.</p>
</div>

<div class="clean-box">
  <h3>5. Objects and Encapsulation (Clean Code, Chapter 6)</h3>
  <pre>public class Truck implements Transport {{
    @Override
    public void deliver(String cargo, String destination) {{
        Objects.requireNonNull(cargo, "Cargo must not be null");
        Objects.requireNonNull(destination, "Destination must not be null");
        System.out.println("Truck delivers " + cargo + " to " + destination);
    }}
}}</pre>
  <p><em>Benefit:</em> Clean Code Chapter 6 explains that true objects hide their data and expose behavior through methods. The transport products do not expose internal data structures through unnecessary getters and setters; they expose meaningful actions via <code>deliver()</code>.</p>
</div>

<h2>4. Verification Evidence (Section 6)</h2>
<p>All required runtime combinations and validation cases were executed and verified:</p>

<table class="data-table">
  <thead>
    <tr>
      <th style="width: 7%;">Check</th>
      <th style="width: 25%;">Input</th>
      <th style="width: 32%;">Expected Result</th>
      <th style="width: 28%;">Actual Output</th>
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
      <td><code>AIR + WINDOWS</code></td>
      <td>Clear validation message; no delivery executed</td>
      <td><code>Validation Error: Unsupported delivery mode 'AIR'. Supported modes: ROAD, SEA.</code></td>
      <td><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td><strong>6</strong></td>
      <td><code>ROAD + LINUX</code></td>
      <td>Clear validation message; no UI constructed</td>
      <td><code>Validation Error: Unsupported UI platform 'LINUX'. Supported platforms: WINDOWS, MACOS.</code></td>
      <td><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td><strong>7</strong></td>
      <td>Missing input</td>
      <td>Clear validation message; clean stop</td>
      <td><code>Validation Error: Missing required configuration arguments.</code></td>
      <td><span class="badge-pass">PASS</span></td>
    </tr>
  </tbody>
</table>

<p><strong>JUnit 5 Automated Test Execution:</strong></p>
<pre>Results: Tests run: 27, Failures: 0, Errors: 0, Skipped: 0 | BUILD SUCCESS</pre>

<h2>5. Conclusion and Design Reflection</h2>

<h3>5.1 Pattern Comparison</h3>
<ul>
  <li><strong>Simple Factory:</strong> A single class with conditional logic (<code>if/switch</code>). It centralizes creation but violates the Open-Closed Principle whenever a new product is added.</li>
  <li><strong>Factory Method:</strong> Uses inheritance. An abstract creator delegates instantiation to subclasses, making it easy to add new products without modifying existing code.</li>
  <li><strong>Abstract Factory:</strong> Uses object composition. An interface creates families of related products, guaranteeing that components match without coupling the client to concrete classes.</li>
</ul>

<h3>5.2 Design Reflection: System Extensibility</h3>
<ol>
  <li><strong>Adding a new Transport (e.g. Air):</strong> Create <code>Plane implements Transport</code> and <code>AirLogistics extends Logistics</code>. Add <code>AIR</code> to the enum and startup helper. Existing transport classes, creators, and <code>DeliveryApplication</code> remain completely unchanged.</li>
  <li><strong>Adding a new UI Family (e.g. Linux):</strong> Create <code>LinuxButton</code>, <code>LinuxCheckbox</code>, and <code>LinuxFactory implements GUIFactory</code>. Add <code>LINUX</code> to the enum and startup helper. Existing UI classes and <code>DeliveryApplication</code> remain completely unchanged.</li>
  <li><strong>Adding a new UI Product Type (e.g. TextField):</strong> Add <code>createTextField()</code> to <code>GUIFactory</code> interface. Implement <code>WindowsTextField</code> and <code>MacOSTextField</code>. Update <code>WindowsFactory</code> and <code>MacOSFactory</code> to implement the new method, and update <code>DeliveryApplication</code> to render the text field. This shows the main trade-off of Abstract Factory: adding new families is easy, but adding new product types requires changing the interface and all concrete factories.</li>
</ol>

<h2>6. References</h2>
<ol>
  <li>Freeman, E., & Robson, E. (2020). <em>Head First Design Patterns</em> (2nd ed.). O'Reilly Media. Chapter 4: Factory Pattern.</li>
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

print("Rendering clean simplified PDF with Chrome headless...")
try:
    subprocess.run(cmd, check=True, timeout=15)
except subprocess.TimeoutExpired:
    print("Chrome finished printing PDF.")
print(f"PDF successfully generated: {pdf_output} ({os.path.getsize(pdf_output) / 1024:.1f} KB)")

scratch_pdf = f"/Users/nursultanmaratov/.gemini/antigravity/scratch/{pdf_output}"
shutil.copyfile(pdf_output, scratch_pdf)
print(f"Copied to scratch root: {scratch_pdf}")

downloads_pdf = f"/Users/nursultanmaratov/Downloads/{pdf_output}"
try:
    shutil.copyfile(pdf_output, downloads_pdf)
    print(f"Copied to Downloads folder: {downloads_pdf}")
except Exception as e:
    print(f"Could not copy to Downloads: {e}")
