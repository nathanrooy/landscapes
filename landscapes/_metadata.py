"""Metadata schema and decorator for optimization test functions."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Protocol, cast


@dataclass(frozen=True, slots=True)
class Solution:
    """Container for a known solution."""

    f_opt: float
    x_opt: list[float]


class BenchmarkFunction(Protocol):
    """Protocol for a function with attached benchmark metadata."""

    bounds: list[tuple[float, float]]
    dimensions: int | None
    g_opt: list[Solution]

    def __call__(self, *args: Any, **kwargs: Any) -> float: ...


def _format_docstring(
    base_doc: str,
    bounds: list[tuple[float, float]],
    dimensions: int | None,
    g_opt: list[Solution],
) -> str:
    """Construct a standardized benchmark docstring."""
    title = base_doc.strip() if base_doc else ""
    bounds_str = str(bounds)
    dims_str = str(dimensions) if dimensions is not None else "n (scalable)"

    opt_lines = [
        f"      {i}) f(x*) = {opt.f_opt}, x* = {opt.x_opt}"
        for i, opt in enumerate(g_opt, 1)
    ]
    opt_str = "\n".join(opt_lines) if opt_lines else "      None specified"

    metadata_block = (
        f"Benchmark Metadata\n"
        f"------------------\n"
        f"Bounds: {bounds_str}\n"
        f"Dimensions: {dims_str}\n"
        f"Global Optima:\n{opt_str}"
    )

    if title:
        return f"{title}\n\n{metadata_block}"
    return metadata_block


def benchmark(
    bounds: list[tuple[float, float]],
    dimensions: int | None = None,
    g_opt: list[Solution] | None = None,
) -> Callable[[Callable[..., float]], BenchmarkFunction]:
    """Decorator for attaching metadata to a function."""

    def decorator(fn: Callable[..., float]) -> BenchmarkFunction:
        target: Any = fn
        target.bounds = bounds
        target.dimensions = dimensions
        target.g_opt = g_opt if g_opt is not None else []

        fn.__doc__ = _format_docstring(
            fn.__doc__ or "",
            bounds=bounds,
            dimensions=dimensions,
            g_opt=target.g_opt,
        )

        return cast(BenchmarkFunction, target)

    return decorator
