package com.logistics.app;

import com.logistics.creator.Logistics;
import com.logistics.ui.Button;
import com.logistics.ui.Checkbox;
import com.logistics.ui.GUIFactory;

import java.util.Objects;

/**
 * Client application that brings together Abstract Factory and Factory Method.
 *
 * It depends exclusively on abstract contracts (GUIFactory, Logistics, Button, Checkbox)
 * injected via constructor, ensuring zero coupling to concrete platform UI classes
 * or concrete transport types.
 */
public class DeliveryApplication {

    private final Button button;
    private final Checkbox checkbox;
    private final Logistics logistics;

    /**
     * Constructs the client application with injected factory abstractions.
     * Obtains UI components from the provided GUIFactory.
     *
     * @param factory   abstract UI factory for creating matched controls
     * @param logistics abstract logistics creator providing delivery workflow
     */
    public DeliveryApplication(GUIFactory factory, Logistics logistics) {
        Objects.requireNonNull(factory, "GUIFactory must not be null");
        Objects.requireNonNull(logistics, "Logistics must not be null");

        // Obtain components through abstract factory interface
        this.button = factory.createButton();
        this.checkbox = factory.createCheckbox();
        this.logistics = logistics;
    }

    /**
     * Renders UI controls through product interfaces without concrete casting.
     */
    public void renderUI() {
        button.paint();
        checkbox.paint();
    }

    /**
     * Initiates delivery workflow through Logistics abstraction.
     *
     * @param cargo       cargo description
     * @param destination destination location
     */
    public void planDelivery(String cargo, String destination) {
        logistics.planDelivery(cargo, destination);
    }

    /**
     * Coordinates the complete flow: UI rendering followed by delivery workflow.
     *
     * @param cargo       cargo description
     * @param destination destination location
     */
    public void run(String cargo, String destination) {
        renderUI();
        planDelivery(cargo, destination);
    }

    // Accessor methods for verification & testing
    public Button getButton() {
        return button;
    }

    public Checkbox getCheckbox() {
        return checkbox;
    }

    public Logistics getLogistics() {
        return logistics;
    }
}
