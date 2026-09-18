package com.logistics.app;

public enum DeliveryMode {
    ROAD,
    SEA;

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
