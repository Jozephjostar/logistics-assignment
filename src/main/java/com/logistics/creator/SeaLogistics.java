package com.logistics.creator;

import com.logistics.transport.Ship;
import com.logistics.transport.Transport;

public class SeaLogistics extends Logistics {

    @Override
    public Transport createTransport() {
        return new Ship();
    }
}
