package com.logistics.creator;

import com.logistics.transport.Ship;
import com.logistics.transport.Transport;

/**
 * Concrete Creator for sea transportation.
 * Overrides createTransport() to create and return a Ship instance.
 */
public class SeaLogistics extends Logistics {

    @Override
    public Transport createTransport() {
        return new Ship();
    }
}
