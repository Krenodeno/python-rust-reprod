#[macro_use]
extern crate cpython;

use cpython::{PyResult, Python};

fn generate_hello_world(_py: Python) -> PyResult<String> {
    Ok(String::from("Hello, World!"))
}

py_module_initializer!(
    libhellors,
    libhellors,
    PyInit_libhellors,
    |py, m| {
        m.add(py, "__doc__", "This module is implemented in Rust")?;
        m.add(
            py,
            "generate_hello_world",
            py_fn!(py, generate_hello_world()),
        )?;
        Ok(())
    }
);
