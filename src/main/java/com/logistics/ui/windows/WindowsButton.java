package com.logistics.ui.windows;

import com.logistics.ui.Button;

/**
 * Concrete Product representing a Windows platform button.
 */
public class WindowsButton implements Button {

    @Override
    public void paint() {
        System.out.println("Rendering Windows button");
    }
}
