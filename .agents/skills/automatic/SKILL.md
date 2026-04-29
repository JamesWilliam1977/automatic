```markdown
# automatic Development Patterns

> Auto-generated skill from repository analysis

## Overview

This skill provides a comprehensive guide to contributing to the `automatic` Python codebase. It covers core coding conventions, typical development workflows, and best practices for maintaining and enhancing the repository. Whether you're adding new features, updating dependencies, or improving the frontend, this guide will help you follow established patterns and streamline your contributions.

## Coding Conventions

- **File Naming:**  
  Use `camelCase` for file names.  
  _Example:_  
  ```
  modelQuant.py
  referenceImageHandler.py
  ```

- **Import Style:**  
  Prefer **relative imports** within modules.  
  _Example:_  
  ```python
  from .common import load_config
  from .layers.quantizer import Quantizer
  ```

- **Export Style:**  
  Use **named exports** (explicit function/class definitions, no `__all__` for wildcard exports).  
  _Example:_  
  ```python
  def quantize_model(model):
      # implementation

  class Dequantizer:
      # implementation
  ```

- **Commit Messages:**  
  Freeform, typically ~30 characters. No enforced prefixes.

## Workflows

### Add or Update Reference Image
**Trigger:** When adding a new model cover or reference image.  
**Command:** `/add-reference-image`

1. Add the new image file to `models/Reference/` (e.g., `models/Reference/new_model.jpg`).
2. Update `html/reference.json` with a new entry for the image.
   ```json
   [
     {
       "name": "New Model",
       "file": "new_model.jpg",
       "description": "Cover image for New Model"
     }
   ]
   ```

---

### Update Changelog and Related Code
**Trigger:** When making code or configuration changes that should be documented.  
**Command:** `/update-changelog`

1. Edit relevant code or configuration files.
2. Update `CHANGELOG.md` with a description of the change.
   ```markdown
   ## [Unreleased]
   - Added support for new backend in installer.py
   ```

---

### Feature or Bugfix in SDNQ Module
**Trigger:** When improving, fixing, or refactoring SDNQ quantization logic.  
**Command:** `/update-sdnq`

1. Edit files in `modules/sdnq/` (e.g., `quantizer.py`, `dequantizer.py`, `loader.py`, `common.py`, or files in `layers/`).
2. Optionally update related files:
   - `modules/model_quant.py`
   - `modules/lora/lora_apply.py`
   - `modules/shared.py`
3. Test changes as appropriate.

---

### Update Installer and Backend Support
**Trigger:** When updating backend dependencies or installation logic.  
**Command:** `/update-installer`

1. Edit `installer.py` to support new versions or platforms.
2. Edit related backend files (e.g., `modules/rocm.py`, `modules/ui.py`).
3. Optionally update `CHANGELOG.md`.

---

### Enhance XYZ Script Features
**Trigger:** When adding features or fixing bugs in the XYZ grid script.  
**Command:** `/update-xyz-script`

1. Edit `scripts/xyz/xyz_grid_shared.py`.
2. Edit `scripts/xyz_grid.py`.
3. Edit `scripts/xyz_grid_on.py`.
4. Test the script enhancements.

---

### Gallery JS Enhancement
**Trigger:** When improving the gallery UI/UX or fixing frontend bugs.  
**Command:** `/update-gallery-js`

1. Edit `javascript/gallery.js`.
2. Optionally edit `javascript/indexdb.js`.
3. Test the gallery in the browser.

---

## Testing Patterns

- **Framework:** Unknown (not explicitly detected).
- **Test File Pattern:** Files matching `*.test.*` (e.g., `quantizer.test.py`).
- **Best Practice:** Place tests alongside module files or in dedicated test directories.  
  _Example:_  
  ```
  modules/sdnq/quantizer.test.py
  ```

## Commands

| Command                | Purpose                                                      |
|------------------------|--------------------------------------------------------------|
| /add-reference-image   | Add or update a model cover or reference image               |
| /update-changelog      | Document code/config changes in the changelog                |
| /update-sdnq           | Implement features, fixes, or refactors in the SDNQ module   |
| /update-installer      | Update installer and backend support files                   |
| /update-xyz-script     | Enhance or fix the XYZ grid script                           |
| /update-gallery-js     | Improve or fix the gallery JavaScript frontend               |
```
