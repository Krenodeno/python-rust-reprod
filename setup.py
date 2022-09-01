#!/usr/bin/env python

import os

from setuptools import setup, find_namespace_packages
from setuptools_rust import Binding, RustExtension

setup(
    name="python-rust-reprod",
    version="0.0.1",
    description="Minimal reproduction of build error",
    long_description="",
    author="Krenodeno",
    packages=find_namespace_packages(),
    install_requires=[],
    extras_require={
        "dev": [
            "flake8",
            "black",
        ],
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "python-rust = python_rust.__main__:main",
        ],
    },
    rust_extensions=[
        RustExtension(
            "python-rust-reprod.libhellors",
            binding=Binding.RustCPython,
            path="hello-rs/Cargo.toml",
        )
    ],
    zip_safe=False,
)
