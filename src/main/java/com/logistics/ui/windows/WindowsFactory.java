package com.logistics.ui.windows;

import com.logistics.ui.Button;
import com.logistics.ui.Checkbox;
import com.logistics.ui.GUIFactory;

/**
 * Concrete Factory for creating Windows UI components.
 * Ensures buttons and checkboxes belong to the matching Windows family.
 */
public class WindowsFactory implements GUIFactory {

    @Override
    public Button createButton() {
        return new WindowsButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }
}
