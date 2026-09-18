package com.logistics.creator;

import com.logistics.transport.Transport;
import java.util.Objects;

/**
 * Creator abstract class in Factory Method pattern.
 * Declares the factory method createTransport() and provides the shared
 * delivery workflow method planDelivery(...).
 */
public abstract class Logistics {

    /**
     * Factory Method to be implemented by subclasses to instantiate
     * a specific Transport product.
     *
     * @return concrete Transport implementation
     */
    public abstract Transport createTransport();

    /**
     * Shared delivery workflow method.
     * Delegates object creation to createTransport() and invokes delivery
     * through the Transport abstraction.
     *
     * @param cargo       description of cargo
     * @param destination destination location
     */
    public void planDelivery(String cargo, String destination) {
        Objects.requireNonNull(cargo, "Cargo cannot be null");
        Objects.requireNonNull(destination, "Destination cannot be null");

        Transport transport = createTransport();
        if (transport == null) {
            throw new IllegalStateException("Factory method returned null transport");
        }
        transport.deliver(cargo, destination);
    }
}
