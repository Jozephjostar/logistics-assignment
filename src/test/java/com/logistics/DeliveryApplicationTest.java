package com.logistics;

import com.logistics.app.DeliveryApplication;
import com.logistics.creator.RoadLogistics;
import com.logistics.creator.SeaLogistics;
import com.logistics.ui.macos.MacOSFactory;
import com.logistics.ui.windows.WindowsFactory;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Tests for DeliveryApplication client combining both patterns.
 * Verifies all 4 required combinations:
 * 1. ROAD + WINDOWS
 * 2. SEA + WINDOWS
 * 3. ROAD + MACOS
 * 4. SEA + MACOS
 */
class DeliveryApplicationTest {

    private String captureOutput(Runnable action) {
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(outContent));
        try {
            action.run();
            return outContent.toString();
        } finally {
            System.setOut(originalOut);
        }
    }

    @Test
    @DisplayName("Check 1: ROAD + WINDOWS produces Windows UI pair and Truck delivery")
    void testRoadAndWindows() {
        DeliveryApplication app = new DeliveryApplication(new WindowsFactory(), new RoadLogistics());
        String output = captureOutput(() -> app.run("laboratory equipment", "Aktau warehouse"));

        assertTrue(output.contains("Rendering Windows button"));
        assertTrue(output.contains("Rendering Windows checkbox"));
        assertTrue(output.contains("Truck delivers laboratory equipment to Aktau warehouse"));
    }

    @Test
    @DisplayName("Check 2: SEA + WINDOWS produces Windows UI pair and Ship delivery")
    void testSeaAndWindows() {
        DeliveryApplication app = new DeliveryApplication(new WindowsFactory(), new SeaLogistics());
        String output = captureOutput(() -> app.run("laboratory equipment", "Aktau warehouse"));

        assertTrue(output.contains("Rendering Windows button"));
        assertTrue(output.contains("Rendering Windows checkbox"));
        assertTrue(output.contains("Ship delivers laboratory equipment to Aktau warehouse"));
    }

    @Test
    @DisplayName("Check 3: ROAD + MACOS produces macOS UI pair and Truck delivery")
    void testRoadAndMacOs() {
        DeliveryApplication app = new DeliveryApplication(new MacOSFactory(), new RoadLogistics());
        String output = captureOutput(() -> app.run("laboratory equipment", "Aktau warehouse"));

        assertTrue(output.contains("Rendering macOS button"));
        assertTrue(output.contains("Rendering macOS checkbox"));
        assertTrue(output.contains("Truck delivers laboratory equipment to Aktau warehouse"));
    }

    @Test
    @DisplayName("Check 4: SEA + MACOS produces macOS UI pair and Ship delivery")
    void testSeaAndMacOs() {
        DeliveryApplication app = new DeliveryApplication(new MacOSFactory(), new SeaLogistics());
        String output = captureOutput(() -> app.run("laboratory equipment", "Aktau warehouse"));

        assertTrue(output.contains("Rendering macOS button"));
        assertTrue(output.contains("Rendering macOS checkbox"));
        assertTrue(output.contains("Ship delivers laboratory equipment to Aktau warehouse"));
    }

    @Test
    @DisplayName("DeliveryApplication constructor rejects null dependencies")
    void testConstructorNullRejection() {
        assertThrows(NullPointerException.class, () -> new DeliveryApplication(null, new RoadLogistics()));
        assertThrows(NullPointerException.class, () -> new DeliveryApplication(new WindowsFactory(), null));
    }
}
