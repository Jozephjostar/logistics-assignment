package com.logistics.ui.macos;

import com.logistics.ui.Button;
import com.logistics.ui.Checkbox;
import com.logistics.ui.GUIFactory;

/**
 * Concrete Factory for creating macOS UI components.
 * Ensures buttons and checkboxes belong to the matching macOS family.
 */
public class MacOSFactory implements GUIFactory {

    @Override
    public Button createButton() {
        return new MacOSButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new MacOSCheckbox();
    }
}
