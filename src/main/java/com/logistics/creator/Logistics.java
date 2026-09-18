package com.logistics.creator;

import com.logistics.transport.Transport;
import java.util.Objects;

public abstract class Logistics {

    public abstract Transport createTransport();

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
