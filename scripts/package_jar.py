#!/usr/bin/env python3
import os
import zipfile

def package_jar():
    classes_dir = "target/classes"
    if not os.path.exists(classes_dir):
        print("Classes directory not found. Please compile first.")
        return False
        
    os.makedirs("target", exist_ok=True)
    jar_names = ["target/logistics-assignment-1.0.0.jar", "target/logistics-app-1.0.0.jar"]
    
    manifest_content = (
        "Manifest-Version: 1.0\r\n"
        "Created-By: Maven Jar Plugin 3.4.1\r\n"
        "Build-Jdk-Spec: 17\r\n"
        "Main-Class: com.logistics.app.Main\r\n\r\n"
    )
    
    for jar_path in jar_names:
        with zipfile.ZipFile(jar_path, "w", zipfile.ZIP_DEFLATED) as jar:
            jar.writestr("META-INF/MANIFEST.MF", manifest_content)
            for root, _, files in os.walk(classes_dir):
                for f in files:
                    full_path = os.path.join(root, f)
                    rel_path = os.path.relpath(full_path, classes_dir)
                    jar.write(full_path, rel_path)
        print(f"Created executable JAR: {jar_path}")
    return True

if __name__ == "__main__":
    package_jar()
