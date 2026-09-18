package com.logistics.creator;

import com.logistics.transport.Transport;
import com.logistics.transport.Truck;

public class RoadLogistics extends Logistics {

    @Override
    public Transport createTransport() {
        return new Truck();
    }
}
