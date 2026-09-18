package com.logistics;

import com.logistics.creator.Logistics;
import com.logistics.creator.RoadLogistics;
import com.logistics.creator.SeaLogistics;
import com.logistics.transport.Ship;
import com.logistics.transport.Transport;
import com.logistics.transport.Truck;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Tests for Factory Method pattern implementation.
 */
class FactoryMethodTest {

    @Test
    @DisplayName("RoadLogistics creates a Truck product")
    void testRoadLogisticsCreatesTruck() {
        Logistics roadLogistics = new RoadLogistics();
        Transport transport = roadLogistics.createTransport();

        assertNotNull(transport, "Factory method must not return null");
        assertInstanceOf(Truck.class, transport, "RoadLogistics must return a Truck");
    }

    @Test
    @DisplayName("SeaLogistics creates a Ship product")
    void testSeaLogisticsCreatesShip() {
        Logistics seaLogistics = new SeaLogistics();
        Transport transport = seaLogistics.createTransport();

        assertNotNull(transport, "Factory method must not return null");
        assertInstanceOf(Ship.class, transport, "SeaLogistics must return a Ship");
    }

    @Test
    @DisplayName("planDelivery executes Truck delivery output")
    void testRoadDeliveryWorkflow() {
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(outContent));

        try {
            Logistics roadLogistics = new RoadLogistics();
            roadLogistics.planDelivery("laboratory equipment", "Aktau warehouse");

            String output = outContent.toString().trim();
            assertTrue(output.contains("Truck delivers"), "Output should indicate Truck delivery");
            assertTrue(output.contains("laboratory equipment"), "Output should contain cargo name");
            assertTrue(output.contains("Aktau warehouse"), "Output should contain destination");
        } finally {
            System.setOut(originalOut);
        }
    }

    @Test
    @DisplayName("planDelivery executes Ship delivery output")
    void testSeaDeliveryWorkflow() {
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(outContent));

        try {
            Logistics seaLogistics = new SeaLogistics();
            seaLogistics.planDelivery("medical containers", "Baku port");

            String output = outContent.toString().trim();
            assertTrue(output.contains("Ship delivers"), "Output should indicate Ship delivery");
            assertTrue(output.contains("medical containers"), "Output should contain cargo name");
            assertTrue(output.contains("Baku port"), "Output should contain destination");
        } finally {
            System.setOut(originalOut);
        }
    }

    @Test
    @DisplayName("planDelivery rejects null cargo or destination")
    void testPlanDeliveryNullParameters() {
        Logistics logistics = new RoadLogistics();
        assertThrows(NullPointerException.class, () -> logistics.planDelivery(null, "Destination"));
        assertThrows(NullPointerException.class, () -> logistics.planDelivery("Cargo", null));
    }
}
