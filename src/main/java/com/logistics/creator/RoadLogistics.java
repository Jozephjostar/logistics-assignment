package com.logistics.creator;

import com.logistics.transport.Transport;
import com.logistics.transport.Truck;

/**
 * Concrete Creator for road transportation.
 * Overrides createTransport() to create and return a Truck instance.
 */
public class RoadLogistics extends Logistics {

    @Override
    public Transport createTransport() {
        return new Truck();
    }
}
