#!/usr/bin/env python3
import os

def generate_factory_method_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 370" width="100%" height="auto" style="background:#ffffff; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
    <marker id="triangle" viewBox="0 0 12 12" refX="12" refY="6" markerWidth="9" markerHeight="9" orient="auto-start-reverse">
      <polygon points="0,0 12,6 0,12" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="400" y="24" font-size="14" font-weight="bold" text-anchor="middle" fill="#000000">Factory Method Pattern - Class Diagram (Logistics Transport)</text>

  <!-- Package Creator -->
  <rect x="20" y="40" width="350" height="315" fill="none" stroke="#777777" stroke-width="1" stroke-dasharray="4,4" rx="4" />
  <text x="30" y="56" font-size="10" font-weight="bold" fill="#555555">package com.logistics.creator</text>

  <!-- Abstract Class Logistics -->
  <g id="logistics">
    <rect x="50" y="75" width="290" height="95" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="195" y="94" font-size="10" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;abstract, Creator&gt;&gt;</text>
    <text x="195" y="110" font-size="13" font-weight="bold" text-anchor="middle" fill="#000000">Logistics</text>
    <line x1="50" y1="118" x2="340" y2="118" stroke="#000000" stroke-width="1" />
    <text x="58" y="136" font-size="10" font-style="italic" fill="#000000">+ {abstract} createTransport(): Transport</text>
    <text x="58" y="154" font-size="10" fill="#000000">+ planDelivery(cargo: String, dest: String): void</text>
  </g>

  <!-- Concrete Creator: RoadLogistics -->
  <g id="roadLogistics">
    <rect x="40" y="240" width="145" height="70" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="112" y="258" font-size="9" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;ConcreteCreator&gt;&gt;</text>
    <text x="112" y="274" font-size="12" font-weight="bold" text-anchor="middle" fill="#000000">RoadLogistics</text>
    <line x1="40" y1="282" x2="185" y2="282" stroke="#000000" stroke-width="1" />
    <text x="46" y="299" font-size="9" fill="#000000">+ createTransport(): Transport</text>
  </g>

  <!-- Concrete Creator: SeaLogistics -->
  <g id="seaLogistics">
    <rect x="205" y="240" width="145" height="70" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="277" y="258" font-size="9" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;ConcreteCreator&gt;&gt;</text>
    <text x="277" y="274" font-size="12" font-weight="bold" text-anchor="middle" fill="#000000">SeaLogistics</text>
    <line x1="205" y1="282" x2="350" y2="282" stroke="#000000" stroke-width="1" />
    <text x="211" y="299" font-size="9" fill="#000000">+ createTransport(): Transport</text>
  </g>

  <!-- Inheritance: RoadLogistics -> Logistics -->
  <path d="M 112 240 L 112 185 L 160 185 L 160 172" fill="none" stroke="#000000" stroke-width="1.5" marker-end="url(#triangle)" />

  <!-- Inheritance: SeaLogistics -> Logistics -->
  <path d="M 277 240 L 277 185 L 230 185 L 230 172" fill="none" stroke="#000000" stroke-width="1.5" marker-end="url(#triangle)" />

  <!-- Package Transport -->
  <rect x="420" y="40" width="360" height="315" fill="none" stroke="#777777" stroke-width="1" stroke-dasharray="4,4" rx="4" />
  <text x="430" y="56" font-size="10" font-weight="bold" fill="#555555">package com.logistics.transport</text>

  <!-- Interface Transport -->
  <g id="transport">
    <rect x="450" y="75" width="300" height="85" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="600" y="94" font-size="10" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;interface, Product&gt;&gt;</text>
    <text x="600" y="110" font-size="13" font-weight="bold" text-anchor="middle" fill="#000000">Transport</text>
    <line x1="450" y1="118" x2="750" y2="118" stroke="#000000" stroke-width="1" />
    <text x="458" y="140" font-size="10" fill="#000000">+ deliver(cargo: String, destination: String): void</text>
  </g>

  <!-- Concrete Product: Truck -->
  <g id="truck">
    <rect x="440" y="240" width="150" height="70" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="515" y="258" font-size="9" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;ConcreteProduct&gt;&gt;</text>
    <text x="515" y="274" font-size="12" font-weight="bold" text-anchor="middle" fill="#000000">Truck</text>
    <line x1="440" y1="282" x2="590" y2="282" stroke="#000000" stroke-width="1" />
    <text x="446" y="299" font-size="9" fill="#000000">+ deliver(cargo, dest): void</text>
  </g>

  <!-- Concrete Product: Ship -->
  <g id="ship">
    <rect x="615" y="240" width="150" height="70" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="690" y="258" font-size="9" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;ConcreteProduct&gt;&gt;</text>
    <text x="690" y="274" font-size="12" font-weight="bold" text-anchor="middle" fill="#000000">Ship</text>
    <line x1="615" y1="282" x2="765" y2="282" stroke="#000000" stroke-width="1" />
    <text x="621" y="299" font-size="9" fill="#000000">+ deliver(cargo, dest): void</text>
  </g>

  <!-- Implementation: Truck -> Transport -->
  <path d="M 515 240 L 515 180 L 560 180 L 560 162" fill="none" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#triangle)" />

  <!-- Implementation: Ship -> Transport -->
  <path d="M 690 240 L 690 180 L 640 180 L 640 162" fill="none" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#triangle)" />

  <!-- Dependency: Logistics uses Transport -->
  <path d="M 340 117 L 442 117" fill="none" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow)" />
  <text x="390" y="110" font-size="9" text-anchor="middle" fill="#000000">&lt;&lt;uses&gt;&gt;</text>

  <!-- Dependency: RoadLogistics creates Truck (routes cleanly under boxes) -->
  <path d="M 112 310 L 112 335 L 515 335 L 515 318" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arrow)" />
  <text x="310" y="347" font-size="8.5" text-anchor="middle" fill="#000000">&lt;&lt;creates Truck&gt;&gt;</text>

  <!-- Dependency: SeaLogistics creates Ship (routes cleanly under boxes) -->
  <path d="M 277 310 L 277 325 L 690 325 L 690 318" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arrow)" />
  <text x="635" y="321" font-size="8.5" text-anchor="middle" fill="#000000">&lt;&lt;creates Ship&gt;&gt;</text>
</svg>"""
    with open("docs/factory_method.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated docs/factory_method.svg")

def generate_abstract_factory_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 470" width="100%" height="auto" style="background:#ffffff; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
    <marker id="triangle" viewBox="0 0 12 12" refX="12" refY="6" markerWidth="9" markerHeight="9" orient="auto-start-reverse">
      <polygon points="0,0 12,6 0,12" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="440" y="22" font-size="14" font-weight="bold" text-anchor="middle" fill="#000000">Abstract Factory Pattern - Class Diagram (Cross-Platform UI)</text>

  <!-- Client Package -->
  <g id="client-app">
    <rect x="20" y="40" width="260" height="175" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="150" y="58" font-size="10" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;Client&gt;&gt;</text>
    <text x="150" y="74" font-size="13" font-weight="bold" text-anchor="middle" fill="#000000">DeliveryApplication</text>
    <line x1="20" y1="82" x2="280" y2="82" stroke="#000000" stroke-width="1" />
    <text x="28" y="98" font-size="9.5" fill="#000000">- button: Button</text>
    <text x="28" y="114" font-size="9.5" fill="#000000">- checkbox: Checkbox</text>
    <text x="28" y="130" font-size="9.5" fill="#000000">- logistics: Logistics</text>
    <line x1="20" y1="138" x2="280" y2="138" stroke="#000000" stroke-width="1" />
    <text x="28" y="154" font-size="9" fill="#000000">+ DeliveryApplication(f: GUIFactory, l: Logistics)</text>
    <text x="28" y="169" font-size="9" fill="#000000">+ renderUI(): void</text>
    <text x="28" y="184" font-size="9" fill="#000000">+ planDelivery(cargo: String, dest: String): void</text>
    <text x="28" y="199" font-size="9" fill="#000000">+ run(cargo: String, dest: String): void</text>
  </g>

  <!-- Abstract Factory Interface -->
  <g id="gui-factory">
    <rect x="330" y="40" width="220" height="95" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="440" y="58" font-size="10" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;interface, AbstractFactory&gt;&gt;</text>
    <text x="440" y="74" font-size="13" font-weight="bold" text-anchor="middle" fill="#000000">GUIFactory</text>
    <line x1="330" y1="82" x2="550" y2="82" stroke="#000000" stroke-width="1" />
    <text x="338" y="102" font-size="10" fill="#000000">+ createButton(): Button</text>
    <text x="338" y="120" font-size="10" fill="#000000">+ createCheckbox(): Checkbox</text>
  </g>

  <!-- Client -> GUIFactory dependency -->
  <path d="M 280 88 L 322 88" fill="none" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow)" />
  <text x="305" y="80" font-size="8.5" text-anchor="middle" fill="#000000">&lt;&lt;uses&gt;&gt;</text>

  <!-- Abstract Product Interfaces -->
  <g id="btn-interface">
    <rect x="620" y="40" width="230" height="60" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="735" y="56" font-size="10" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;interface, AbstractProduct&gt;&gt;</text>
    <text x="735" y="72" font-size="12" font-weight="bold" text-anchor="middle" fill="#000000">Button</text>
    <line x1="620" y1="78" x2="850" y2="78" stroke="#000000" stroke-width="1" />
    <text x="628" y="93" font-size="9.5" fill="#000000">+ paint(): void</text>
  </g>

  <g id="chk-interface">
    <rect x="620" y="125" width="230" height="60" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="735" y="141" font-size="10" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;interface, AbstractProduct&gt;&gt;</text>
    <text x="735" y="157" font-size="12" font-weight="bold" text-anchor="middle" fill="#000000">Checkbox</text>
    <line x1="620" y1="163" x2="850" y2="163" stroke="#000000" stroke-width="1" />
    <text x="628" y="178" font-size="9.5" fill="#000000">+ paint(): void</text>
  </g>

  <!-- Factory -> Product dependencies -->
  <path d="M 550 65 L 612 65" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arrow)" />
  <path d="M 550 115 L 580 115 L 580 150 L 612 150" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arrow)" />

  <!-- Concrete Factory: WindowsFactory -->
  <g id="win-factory">
    <rect x="260" y="240" width="190" height="80" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="355" y="258" font-size="9" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;ConcreteFactory&gt;&gt;</text>
    <text x="355" y="274" font-size="12" font-weight="bold" text-anchor="middle" fill="#000000">WindowsFactory</text>
    <line x1="260" y1="282" x2="450" y2="282" stroke="#000000" stroke-width="1" />
    <text x="268" y="298" font-size="9" fill="#000000">+ createButton(): Button</text>
    <text x="268" y="313" font-size="9" fill="#000000">+ createCheckbox(): Checkbox</text>
  </g>

  <!-- Concrete Factory: MacOSFactory -->
  <g id="mac-factory">
    <rect x="260" y="350" width="190" height="80" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="355" y="368" font-size="9" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;ConcreteFactory&gt;&gt;</text>
    <text x="355" y="384" font-size="12" font-weight="bold" text-anchor="middle" fill="#000000">MacOSFactory</text>
    <line x1="260" y1="392" x2="450" y2="392" stroke="#000000" stroke-width="1" />
    <text x="268" y="408" font-size="9" fill="#000000">+ createButton(): Button</text>
    <text x="268" y="423" font-size="9" fill="#000000">+ createCheckbox(): Checkbox</text>
  </g>

  <!-- Implementation: WindowsFactory -> GUIFactory -->
  <path d="M 355 240 L 355 160 L 400 160 L 400 143" fill="none" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#triangle)" />

  <!-- Implementation: MacOSFactory -> GUIFactory -->
  <path d="M 440 350 L 440 143" fill="none" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#triangle)" />

  <!-- Concrete Products: Windows Family -->
  <g id="win-products">
    <rect x="520" y="240" width="150" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="595" y="255" font-size="8.5" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;ConcreteProduct&gt;&gt;</text>
    <text x="595" y="269" font-size="11" font-weight="bold" text-anchor="middle" fill="#000000">WindowsButton</text>
    <line x1="520" y1="274" x2="670" y2="274" stroke="#000000" stroke-width="1" />
    <text x="526" y="286" font-size="9" fill="#000000">+ paint(): void</text>

    <rect x="695" y="240" width="155" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="772" y="255" font-size="8.5" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;ConcreteProduct&gt;&gt;</text>
    <text x="772" y="269" font-size="11" font-weight="bold" text-anchor="middle" fill="#000000">WindowsCheckbox</text>
    <line x1="695" y1="274" x2="850" y2="274" stroke="#000000" stroke-width="1" />
    <text x="701" y="286" font-size="9" fill="#000000">+ paint(): void</text>
  </g>

  <!-- Concrete Products: MacOS Family -->
  <g id="mac-products">
    <rect x="520" y="350" width="150" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="595" y="365" font-size="8.5" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;ConcreteProduct&gt;&gt;</text>
    <text x="595" y="379" font-size="11" font-weight="bold" text-anchor="middle" fill="#000000">MacOSButton</text>
    <line x1="520" y1="384" x2="670" y2="384" stroke="#000000" stroke-width="1" />
    <text x="526" y="396" font-size="9" fill="#000000">+ paint(): void</text>

    <rect x="695" y="350" width="155" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
    <text x="772" y="365" font-size="8.5" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;ConcreteProduct&gt;&gt;</text>
    <text x="772" y="379" font-size="11" font-weight="bold" text-anchor="middle" fill="#000000">MacOSCheckbox</text>
    <line x1="695" y1="384" x2="850" y2="384" stroke="#000000" stroke-width="1" />
    <text x="701" y="396" font-size="9" fill="#000000">+ paint(): void</text>
  </g>

  <!-- Product Implementations -->
  <!-- WindowsButton -> Button -->
  <path d="M 595 240 L 595 195 L 680 195 L 680 107" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#triangle)" />
  <!-- MacOSButton -> Button -->
  <path d="M 540 350 L 540 210 L 660 210 L 660 107" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#triangle)" />

  <!-- WindowsCheckbox -> Checkbox -->
  <path d="M 772 240 L 772 192" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#triangle)" />
  <!-- MacOSCheckbox -> Checkbox -->
  <path d="M 790 350 L 790 192" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#triangle)" />

  <!-- WindowsFactory -> creates Windows components -->
  <path d="M 450 260 L 512 260" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arrow)" />
  <!-- MacOSFactory -> creates MacOS components -->
  <path d="M 450 370 L 512 370" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arrow)" />
</svg>"""
    with open("docs/abstract_factory.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated docs/abstract_factory.svg")

if __name__ == "__main__":
    os.makedirs("docs", exist_ok=True)
    generate_factory_method_svg()
    generate_abstract_factory_svg()
