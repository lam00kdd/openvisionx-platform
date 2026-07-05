# ADR-0004

## Status

Accepted

---

## Decision

Pipeline execution is managed by the Engine module.

Tools communicate only through ExecutionContext.

Pipeline owns ToolCollection.

BaseTool implements the Template Method pattern.