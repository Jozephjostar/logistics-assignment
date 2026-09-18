package com.logistics.app;

import com.logistics.creator.Logistics;
import com.logistics.ui.Button;
import com.logistics.ui.Checkbox;
import com.logistics.ui.GUIFactory;

import java.util.Objects;

public class DeliveryApplication {

    private final Button button;
    private final Checkbox checkbox;
    private final Logistics logistics;

    public DeliveryApplication(GUIFactory factory, Logistics logistics) {
        Objects.requireNonNull(factory, "GUIFactory must not be null");
        Objects.requireNonNull(logistics, "Logistics must not be null");

        this.button = factory.createButton();
        this.checkbox = factory.createCheckbox();
        this.logistics = logistics;
    }

    public void renderUI() {
        button.paint();
        checkbox.paint();
    }

    public void planDelivery(String cargo, String destination) {
        logistics.planDelivery(cargo, destination);
    }

    public void run(String cargo, String destination) {
        renderUI();
        planDelivery(cargo, destination);
    }

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
