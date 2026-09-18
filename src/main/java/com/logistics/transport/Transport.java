package com.logistics.transport;

/**
 * Product interface in Factory Method pattern.
 * Defines the contract for all delivery transports.
 */
public interface Transport {
    /**
     * Executes the delivery of cargo to the specified destination.
     *
     * @param cargo       description of the cargo to be delivered
     * @param destination final destination for the delivery
     */
    void deliver(String cargo, String destination);
}
