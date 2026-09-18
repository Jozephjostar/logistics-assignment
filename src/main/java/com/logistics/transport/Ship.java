package com.logistics.transport;

import java.util.Objects;

/**
 * Concrete Product representing maritime sea delivery transport.
 */
public class Ship implements Transport {

    @Override
    public void deliver(String cargo, String destination) {
        Objects.requireNonNull(cargo, "Cargo must not be null");
        Objects.requireNonNull(destination, "Destination must not be null");
        System.out.println("Ship delivers " + cargo + " to " + destination);
    }
}
