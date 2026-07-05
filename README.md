# OpenVisionX Platform

<p align="center">

Industrial Machine Vision Platform built with Python.

Design for AOI, OCR, AI Vision, Robotics and Industrial Automation.

</p>

---

## Vision

OpenVisionX is an open-source platform for developing industrial Machine Vision applications.

Unlike a traditional AOI project, OpenVisionX is designed as a reusable platform that enables engineers to rapidly build vision applications.

---

## Features

- Industrial Pipeline Engine
- ROI Management
- OpenCV Image Processing
- AI Inference
- Camera Integration
- PLC Communication
- Barcode & QR Code
- OCR
- Vision Studio (Planned)

---

## Project Structure

```text
openvisionx-platform/

├── docs/
├── examples/
├── src/
│   └── openvisionx/
├── tests/
├── pyproject.toml
└── README.md
```

---

## Current Progress

| Module | Status |
|---------|--------|
| Core | ✅ |
| Engine | 🚧 |
| Vision | ⏳ |
| Devices | ⏳ |
| AI | ⏳ |
| Studio | ⏳ |

---

## Requirements

- Python 3.12+
- OpenCV
- NumPy
- pytest
- Ruff

---

## Installation

```bash
git clone https://github.com/lam00kdd/openvisionx-platform.git

cd openvisionx-platform

python -m venv .venv

pip install -e .
```

---

## Example

```python
from openvisionx.engine import Pipeline

pipeline = Pipeline()

pipeline.run(context)
```

---

## Roadmap

- [x] Core Foundation
- [ ] Pipeline Engine
- [ ] Vision Tools
- [ ] Camera SDK
- [ ] AI Module
- [ ] Vision Studio

---

## Development

```bash
pytest

ruff check .
```

---

## License

MIT License