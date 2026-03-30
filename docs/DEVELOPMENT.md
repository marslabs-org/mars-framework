# Development Guide

This guide explains how to build, test, and develop the `mars-framework` when making changes to the C++ core or Python bindings.

## 🏗️ Building and Testing C++ Changes

Because the C++ code (`core/`) is compiled into a Python extension (`bindings/python/`), Python needs to recompile the C++ code whenever you make a change before you can test it.

### 1. Make your changes
Modify any files within `core/src/`, `core/include/`, or `bindings/python/src/`.

### 2. Recompile the extension
Run the following command from the root of your project to trigger CMake and rebuild the `mars_core` Python package:

```bash
uv pip install -e bindings/python
```
*Note: The `-e` (editable) flag tells the environment to link the build, but C++ code still requires recompilation when structural changes happen.*

### 3. Test your changes
Run your Python test script to verify the C++ logic:

```bash
uv run python main.py
```

---

## 🧹 Troubleshooting Builds

If CMake caches an old build or you encounter weird compilation errors after restructuring folders, you can clear the build cache and force a clean reinstall:

```bash
# Force a clean rebuild of the bindings
uv pip install --reinstall -e bindings/python
```

---

## ⚡ Direct CMake Build (Advanced)

If you are only working on the C++ `core/` and want direct compiler feedback without involving Python or `uv`, you can use native CMake commands from the project root:

```bash
# 1. Generate the build environment
cmake -B build

# 2. Compile the C++ code
cmake --build build
```
