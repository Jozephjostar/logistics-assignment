package com.logistics.ui.macos;

import com.logistics.ui.Checkbox;

/**
 * Concrete Product representing a macOS platform checkbox.
 */
public class MacOSCheckbox implements Checkbox {

    @Override
    public void paint() {
        System.out.println("Rendering macOS checkbox");
    }
}
