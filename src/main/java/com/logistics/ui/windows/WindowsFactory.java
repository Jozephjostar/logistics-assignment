package com.logistics.ui.windows;

import com.logistics.ui.Button;
import com.logistics.ui.Checkbox;
import com.logistics.ui.GUIFactory;

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
