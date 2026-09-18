package com.logistics.app;

public enum UIPlatform {
    WINDOWS,
    MACOS;

    public static UIPlatform fromString(String value) {
        if (value == null || value.trim().isEmpty()) {
            throw new IllegalArgumentException("UI platform cannot be empty");
        }
        String normalized = value.trim().toUpperCase();
        for (UIPlatform platform : values()) {
            if (platform.name().equals(normalized)) {
                return platform;
            }
        }
        throw new IllegalArgumentException("Unsupported UI platform '" + value + "'. Supported platforms: WINDOWS, MACOS.");
    }
}
