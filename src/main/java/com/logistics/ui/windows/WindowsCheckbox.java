package com.logistics.ui.windows;

import com.logistics.ui.Checkbox;

/**
 * Concrete Product representing a Windows platform checkbox.
 */
public class WindowsCheckbox implements Checkbox {

    @Override
    public void paint() {
        System.out.println("Rendering Windows checkbox");
    }
}
