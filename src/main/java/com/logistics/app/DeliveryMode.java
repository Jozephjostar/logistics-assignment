package com.logistics.app;

/**
 * Supported delivery modes for runtime selection.
 */
public enum DeliveryMode {
    ROAD,
    SEA;

    /**
     * Parses a case-insensitive string into a DeliveryMode.
     *
     * @param value input string
     * @return matching DeliveryMode
     * @throws IllegalArgumentException if the mode is unsupported or null
     */
    public static DeliveryMode fromString(String value) {
        if (value == null || value.trim().isEmpty()) {
            throw new IllegalArgumentException("Delivery mode cannot be empty");
        }
        String normalized = value.trim().toUpperCase();
        for (DeliveryMode mode : values()) {
            if (mode.name().equals(normalized)) {
                return mode;
            }
        }
        throw new IllegalArgumentException("Unsupported delivery mode '" + value + "'. Supported modes: ROAD, SEA.");
    }
}
