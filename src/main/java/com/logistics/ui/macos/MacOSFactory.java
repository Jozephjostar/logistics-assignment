package com.logistics.ui.macos;

import com.logistics.ui.Button;
import com.logistics.ui.Checkbox;
import com.logistics.ui.GUIFactory;

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
