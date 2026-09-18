package com.logistics.app;

import com.logistics.creator.Logistics;
import com.logistics.ui.GUIFactory;

import java.util.Scanner;

/**
 * Main application entry point.
 * Coordinates input acquisition (CLI arguments or interactive console),
 * performs validation, instantiates factories via StartupHelper,
 * and launches DeliveryApplication.
 */
public class Main {

    public static void main(String[] args) {
        try {
            StartupHelper.AppConfig config;

            if (args != null && args.length > 0) {
                // Command-line arguments mode
                config = StartupHelper.parseArguments(args);
            } else {
                // Interactive console input mode
                config = promptInteractiveConfig();
            }

            // Print configuration header
            System.out.println("Delivery mode: " + config.deliveryMode());
            System.out.println("UI platform: " + config.uiPlatform());

            // Instantiate creator and abstract factory using StartupHelper
            Logistics logistics = StartupHelper.createLogistics(config.deliveryMode());
            GUIFactory guiFactory = StartupHelper.createGUIFactory(config.uiPlatform());

            // Inject abstractions into DeliveryApplication client
            DeliveryApplication app = new DeliveryApplication(guiFactory, logistics);

            // Execute application workflow: render UI components and plan delivery
            app.run(config.cargo(), config.destination());

        } catch (IllegalArgumentException ex) {
            System.err.println("Validation Error: " + ex.getMessage());
            System.exit(1);
        } catch (Exception ex) {
            System.err.println("Application Error: " + ex.getMessage());
            System.exit(1);
        }
    }

    /**
     * Interactively prompts the user via console input when no CLI arguments are supplied.
     *
     * @return validated AppConfig
     */
    private static StartupHelper.AppConfig promptInteractiveConfig() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter delivery mode (ROAD or SEA): ");
        if (!scanner.hasNextLine()) {
            throw new IllegalArgumentException("No input provided for delivery mode. Expected ROAD or SEA.");
        }
        String modeLine = scanner.nextLine().trim();
        if (modeLine.isEmpty()) {
            throw new IllegalArgumentException("Delivery mode cannot be empty. Expected ROAD or SEA.");
        }
        DeliveryMode mode = DeliveryMode.fromString(modeLine);

        System.out.print("Enter UI platform (WINDOWS or MACOS): ");
        if (!scanner.hasNextLine()) {
            throw new IllegalArgumentException("No input provided for UI platform. Expected WINDOWS or MACOS.");
        }
        String platformLine = scanner.nextLine().trim();
        if (platformLine.isEmpty()) {
            throw new IllegalArgumentException("UI platform cannot be empty. Expected WINDOWS or MACOS.");
        }
        UIPlatform platform = UIPlatform.fromString(platformLine);

        return new StartupHelper.AppConfig(
                mode,
                platform,
                StartupHelper.DEFAULT_CARGO,
                StartupHelper.DEFAULT_DESTINATION
        );
    }
}
