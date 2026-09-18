package com.logistics.ui.macos;

import com.logistics.ui.Button;

public class MacOSButton implements Button {

    @Override
    public void paint() {
        System.out.println("Rendering macOS button");
    }
}
