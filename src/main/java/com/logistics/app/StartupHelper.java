package com.logistics.app;

import com.logistics.creator.Logistics;
import com.logistics.creator.RoadLogistics;
import com.logistics.creator.SeaLogistics;
import com.logistics.ui.GUIFactory;
import com.logistics.ui.macos.MacOSFactory;
import com.logistics.ui.windows.WindowsFactory;

import java.util.Objects;

public final class StartupHelper {

    public static final String DEFAULT_CARGO = "laboratory equipment";
    public static final String DEFAULT_DESTINATION = "Aktau warehouse";

    private StartupHelper() {
    }

    public static AppConfig parseArguments(String[] args) {
        if (args == null || args.length == 0) {
            throw new IllegalArgumentException("Missing required configuration arguments.\n" + getUsage());
        }

        String modeRaw = null;
        String platformRaw = null;
        String cargo = DEFAULT_CARGO;
        String destination = DEFAULT_DESTINATION;

        if (args.length >= 2 && !args[0].startsWith("-") && !args[1].startsWith("-")) {
            modeRaw = args[0];
            platformRaw = args[1];
            if (args.length >= 4) {
                cargo = args[2];
                destination = args[3];
            }
        } else {
            for (int i = 0; i < args.length; i++) {
                String arg = args[i];
                if (("--delivery".equalsIgnoreCase(arg) || "-d".equalsIgnoreCase(arg)) && i + 1 < args.length) {
                    modeRaw = args[++i];
                } else if (("--platform".equalsIgnoreCase(arg) || "-p".equalsIgnoreCase(arg)) && i + 1 < args.length) {
                    platformRaw = args[++i];
                } else if (("--cargo".equalsIgnoreCase(arg) || "-c".equalsIgnoreCase(arg)) && i + 1 < args.length) {
                    cargo = args[++i];
                } else if (("--destination".equalsIgnoreCase(arg) || "-dest".equalsIgnoreCase(arg)) && i + 1 < args.length) {
                    destination = args[++i];
                } else if (arg.contains("=")) {
                    String[] parts = arg.split("=", 2);
                    if ("--delivery".equalsIgnoreCase(parts[0]) || "-d".equalsIgnoreCase(parts[0])) {
                        modeRaw = parts[1];
                    } else if ("--platform".equalsIgnoreCase(parts[0]) || "-p".equalsIgnoreCase(parts[0])) {
                        platformRaw = parts[1];
                    } else if ("--cargo".equalsIgnoreCase(parts[0]) || "-c".equalsIgnoreCase(parts[0])) {
                        cargo = parts[1];
                    } else if ("--destination".equalsIgnoreCase(parts[0]) || "-dest".equalsIgnoreCase(parts[0])) {
                        destination = parts[1];
                    }
                }
            }
        }

        if (modeRaw == null || modeRaw.trim().isEmpty()) {
            throw new IllegalArgumentException("Missing required delivery mode. Specify ROAD or SEA.\n" + getUsage());
        }
        if (platformRaw == null || platformRaw.trim().isEmpty()) {
            throw new IllegalArgumentException("Missing required UI platform. Specify WINDOWS or MACOS.\n" + getUsage());
        }

        DeliveryMode mode = DeliveryMode.fromString(modeRaw);
        UIPlatform platform = UIPlatform.fromString(platformRaw);

        return new AppConfig(mode, platform, cargo, destination);
    }

    public static Logistics createLogistics(DeliveryMode mode) {
        Objects.requireNonNull(mode, "DeliveryMode cannot be null");
        return switch (mode) {
            case ROAD -> new RoadLogistics();
            case SEA -> new SeaLogistics();
        };
    }

    public static GUIFactory createGUIFactory(UIPlatform platform) {
        Objects.requireNonNull(platform, "UIPlatform cannot be null");
        return switch (platform) {
            case WINDOWS -> new WindowsFactory();
            case MACOS -> new MacOSFactory();
        };
    }

    public static String getUsage() {
        return "Usage:\n" +
               "  java -jar logistics-app.jar <ROAD|SEA> <WINDOWS|MACOS>\n" +
               "  java -jar logistics-app.jar --delivery <ROAD|SEA> --platform <WINDOWS|MACOS> [--cargo <desc>] [--destination <loc>]\n" +
               "Supported delivery modes: ROAD, SEA\n" +
               "Supported UI platforms:  WINDOWS, MACOS";
    }

    public record AppConfig(
            DeliveryMode deliveryMode,
            UIPlatform uiPlatform,
            String cargo,
            String destination
    ) {}
}
