package com.logistics.transport;

import java.util.Objects;

/**
 * Concrete Product representing road delivery transport.
 */
public class Truck implements Transport {

    @Override
    public void deliver(String cargo, String destination) {
        Objects.requireNonNull(cargo, "Cargo must not be null");
        Objects.requireNonNull(destination, "Destination must not be null");
        System.out.println("Truck delivers " + cargo + " to " + destination);
    }
}
