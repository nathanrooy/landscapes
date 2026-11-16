"""Metadata schema and decorator for optimization test functions."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Protocol, cast

from landscapes._references import REFERENCES


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
    refs: list[str],
) -> str:
    """Construct a standardized benchmark docstring."""
    title = base_doc.strip()
    dims_str = str(dimensions) if dimensions is not None else "n (scalable)"

    # pretty print global optima
    opt_str = "\n".join(
        f"      {i}) f(x*) = {opt.f_opt}, x* = {opt.x_opt}"
        for i, opt in enumerate(g_opt, 1)
    )

    # join all metadata together
    metadata_block = (
        f"Benchmark Metadata\n"
        f"------------------\n"
        f"Bounds: {bounds}\n"
        f"Dimensions: {dims_str}\n"
        f"Global Optima:\n{opt_str}"
    )

    # add the references
    ref_lines = [f"  [{i}] {REFERENCES[k]}" for i, k in enumerate(refs, 1)]
    ref_block = "References\n----------\n" + "\n".join(ref_lines)

    # finish the docstring and return
    return f"{title}\n\n{metadata_block}\n\n{ref_block}"


def benchmark(
    bounds: list[tuple[float, float]],
    g_opt: list[Solution],
    _ref: list[str],
    dimensions: int | None = None,
) -> Callable[[Callable[..., float]], BenchmarkFunction]:
    """Decorator for attaching metadata to a function."""

    def decorator(fn: Callable[..., float]) -> BenchmarkFunction:
        target: Any = fn
        target.bounds = bounds
        target.dimensions = dimensions
        target.g_opt = g_opt
        target._ref = _ref

        fn.__doc__ = _format_docstring(
            fn.__doc__ or "",
            bounds=bounds,
            dimensions=dimensions,
            g_opt=g_opt,
            refs=_ref,
        )

        return cast(BenchmarkFunction, target)

    return decorator
