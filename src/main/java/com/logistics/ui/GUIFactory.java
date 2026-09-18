package com.logistics.ui;

/**
 * Abstract Factory interface for creating families of matching UI components.
 */
public interface GUIFactory {
    /**
     * Creates a matching platform-specific Button component.
     *
     * @return Button product
     */
    Button createButton();

    /**
     * Creates a matching platform-specific Checkbox component.
     *
     * @return Checkbox product
     */
    Checkbox createCheckbox();
}
