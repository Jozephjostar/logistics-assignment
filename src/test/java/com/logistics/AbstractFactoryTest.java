package com.logistics;

import com.logistics.ui.Button;
import com.logistics.ui.Checkbox;
import com.logistics.ui.GUIFactory;
import com.logistics.ui.macos.MacOSButton;
import com.logistics.ui.macos.MacOSCheckbox;
import com.logistics.ui.macos.MacOSFactory;
import com.logistics.ui.windows.WindowsButton;
import com.logistics.ui.windows.WindowsCheckbox;
import com.logistics.ui.windows.WindowsFactory;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.*;

class AbstractFactoryTest {

    @Test
    @DisplayName("WindowsFactory creates a matching pair of WindowsButton and WindowsCheckbox")
    void testWindowsFactoryProductFamily() {
        GUIFactory factory = new WindowsFactory();
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();

        assertNotNull(button);
        assertNotNull(checkbox);
        assertInstanceOf(WindowsButton.class, button);
        assertInstanceOf(WindowsCheckbox.class, checkbox);
    }

    @Test
    @DisplayName("MacOSFactory creates a matching pair of MacOSButton and MacOSCheckbox")
    void testMacOSFactoryProductFamily() {
        GUIFactory factory = new MacOSFactory();
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();

        assertNotNull(button);
        assertNotNull(checkbox);
        assertInstanceOf(MacOSButton.class, button);
        assertInstanceOf(MacOSCheckbox.class, checkbox);
    }

    @Test
    @DisplayName("Windows UI components render correct platform text")
    void testWindowsRendering() {
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(outContent));

        try {
            GUIFactory factory = new WindowsFactory();
            factory.createButton().paint();
            factory.createCheckbox().paint();

            String output = outContent.toString();
            assertTrue(output.contains("Rendering Windows button"));
            assertTrue(output.contains("Rendering Windows checkbox"));
        } finally {
            System.setOut(originalOut);
        }
    }

    @Test
    @DisplayName("macOS UI components render correct platform text")
    void testMacOSRendering() {
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(outContent));

        try {
            GUIFactory factory = new MacOSFactory();
            factory.createButton().paint();
            factory.createCheckbox().paint();

            String output = outContent.toString();
            assertTrue(output.contains("Rendering macOS button"));
            assertTrue(output.contains("Rendering macOS checkbox"));
        } finally {
            System.setOut(originalOut);
        }
    }
}
