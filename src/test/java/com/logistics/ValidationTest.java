package com.logistics;

import com.logistics.app.DeliveryMode;
import com.logistics.app.StartupHelper;
import com.logistics.app.UIPlatform;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Tests for input validation and error handling:
 * - Check 5: Unsupported delivery mode
 * - Check 6: Unsupported UI platform
 * - Missing input handling
 * - Case-insensitive parsing
 */
class ValidationTest {

    @Test
    @DisplayName("Check 5: Unsupported delivery mode throws clear validation message")
    void testUnsupportedDeliveryMode() {
        String[] args = {"AIR", "WINDOWS"};

        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () ->
                StartupHelper.parseArguments(args)
        );

        assertTrue(ex.getMessage().contains("Unsupported delivery mode 'AIR'"),
                "Exception message must specify the invalid mode");
        assertTrue(ex.getMessage().contains("Supported modes: ROAD, SEA"),
                "Exception message must list supported alternatives");
    }

    @Test
    @DisplayName("Check 6: Unsupported UI platform throws clear validation message")
    void testUnsupportedUIPlatform() {
        String[] args = {"ROAD", "LINUX"};

        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () ->
                StartupHelper.parseArguments(args)
        );

        assertTrue(ex.getMessage().contains("Unsupported UI platform 'LINUX'"),
                "Exception message must specify the invalid platform");
        assertTrue(ex.getMessage().contains("Supported platforms: WINDOWS, MACOS"),
                "Exception message must list supported alternatives");
    }

    @Test
    @DisplayName("Missing arguments array throws descriptive exception")
    void testMissingArguments() {
        IllegalArgumentException exNull = assertThrows(IllegalArgumentException.class, () ->
                StartupHelper.parseArguments(null)
        );
        assertTrue(exNull.getMessage().contains("Missing required configuration arguments"));

        IllegalArgumentException exEmpty = assertThrows(IllegalArgumentException.class, () ->
                StartupHelper.parseArguments(new String[]{})
        );
        assertTrue(exEmpty.getMessage().contains("Missing required configuration arguments"));
    }

    @Test
    @DisplayName("Incomplete arguments (only delivery mode provided) throws descriptive exception")
    void testIncompleteArgumentsMissingPlatform() {
        String[] args = {"--delivery", "ROAD"};

        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () ->
                StartupHelper.parseArguments(args)
        );

        assertTrue(ex.getMessage().contains("Missing required UI platform"));
    }

    @Test
    @DisplayName("Incomplete arguments (only platform provided) throws descriptive exception")
    void testIncompleteArgumentsMissingDelivery() {
        String[] args = {"--platform", "WINDOWS"};

        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () ->
                StartupHelper.parseArguments(args)
        );

        assertTrue(ex.getMessage().contains("Missing required delivery mode"));
    }

    @ParameterizedTest
    @ValueSource(strings = {"road", "ROAD", "Road", "rOaD"})
    @DisplayName("DeliveryMode parsing is case-insensitive")
    void testDeliveryModeCaseInsensitive(String input) {
        assertEquals(DeliveryMode.ROAD, DeliveryMode.fromString(input));
    }

    @ParameterizedTest
    @ValueSource(strings = {"macos", "MACOS", "MacOS", "mAcOs"})
    @DisplayName("UIPlatform parsing is case-insensitive")
    void testUIPlatformCaseInsensitive(String input) {
        assertEquals(UIPlatform.MACOS, UIPlatform.fromString(input));
    }
}
