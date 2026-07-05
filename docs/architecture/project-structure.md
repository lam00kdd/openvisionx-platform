# Project Structure

```
src/
│
└── openvisionx/
    │
    ├── core/
    ├── engine/
    ├── vision/
    ├── devices/
    ├── plugins/
    └── studio/
```

---

## Rules

- One responsibility per package.
- One public class per file (khuyến nghị).
- Tests mirror source structure.
- Public APIs exported via __init__.py.