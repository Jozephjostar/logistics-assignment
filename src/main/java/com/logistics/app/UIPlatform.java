package com.logistics.app;

/**
 * Supported UI platform families for runtime selection.
 */
public enum UIPlatform {
    WINDOWS,
    MACOS;

    /**
     * Parses a case-insensitive string into a UIPlatform.
     *
     * @param value input string
     * @return matching UIPlatform
     * @throws IllegalArgumentException if the platform is unsupported or null
     */
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
