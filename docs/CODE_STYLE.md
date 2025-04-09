# Python Code Style Guide for CLI Applications

Welcome to the project! This guide outlines our code style, project structure, tooling, and best practices to ensure consistency, readability, and maintainability throughout the codebase. All contributors should follow these guidelines when working on the code.

---

## 📁 Project Structure

- **`src/`**: All application code lives here.
- **`tests/`**: Unit and integration tests live here.
- **`config/`**: Application configuration settings.
- **`static/`**: Static assets, if any.
- **`pyproject.toml`**: Dependency management files.

---

## 🎨 Code Style

- Format code using **Black** (max line length: 88 characters).
- Sort imports using **isort**.
- Follow **PEP 8** conventions:

```python
# Functions and variables
calculate_average = ...

# Classes
class UserProfile:
    ...

# Constants
DEFAULT_TIMEOUT = 30
```

- Use **absolute imports**:

```python
# ✅ Absolute
from your_package_name.module import function

# 🚫 Avoid relative
from ..module import function
```

---

## 🔍 Type Hints

- Use type hints for all function parameters and return types.
- Import from `typing` as needed:

```python
from typing import Optional, List, Dict, Union, Any, TypeVar, Protocol

T = TypeVar("T")

def get_user(id: int) -> Optional[User]:
    ...
```

- Prefer `Optional[Type]` over `Type | None` for compatibility.
- Use `types.py` to store custom type aliases.
- Use `Protocol` for duck typing:

```python
class Serializer(Protocol):
    def serialize(self) -> str:
        ...
```

---

## 📄 File Handling

- Use `pathlib.Path`:

```python
from pathlib import Path

config_path = Path("config/settings.yaml")
```

- Always use context managers:

```python
with open("file.txt", "r") as file:
    content = file.read()
```

---

## 🗃️ Database

- Use connection pooling (e.g., with SQLAlchemy or async engines).
- Organize models in a dedicated `models/` module.
- Define relationships and indexes explicitly.

```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    data_entries = relationship("DataEntry", back_populates="user")
```

---

## ✅ Testing

- Use **pytest** and **pytest-cov**.
- Mock with **pytest-mock**.
- Write test cases for all commands and edge cases.
- Use fixtures:

```python
import pytest

@pytest.fixture
def sample_user():
    return User(email="test@example.com")
```

---

## 🛡️ Security

- Sanitize all user inputs.
- Use secure configurations when dealing with file systems or networks.
- Avoid hardcoding secrets—use environment variables and `config/` setup files.
- Log sensitive actions responsibly and avoid leaking credentials.

---

## 🚀 Performance

- Optimize DB queries and use proper indexing.
- Use background threads or asynchronous execution for heavy operations.
- Paginate large sets of CLI output if needed.
- Consider caching frequent data lookups when appropriate.

---

## ⚠️ Error Handling

- Create custom exceptions:

```python
class ValidationError(Exception):
    pass
```

- Wrap risky operations in try-except blocks.
- Log exceptions and return meaningful errors:

```python
try:
    ...
except ValidationError as e:
    logger.error(f"Validation failed: {e}")
    print("An error occurred. Check logs for details.")
```

---

## 📚 Documentation

- Use Google-style docstrings:

```python
def add(x: int, y: int) -> int:
    """Add two numbers.

    Args:
        x (int): First number
        y (int): Second number

    Returns:
        int: Sum of x and y
    """
    return x + y
```

- Document all CLI commands and public APIs.
- Maintain `README.md` and setup instructions.
- Use inline comments to clarify non-obvious logic.

---

## 🛠️ Development Workflow

- Use **`uv`** exclusively for dependency management and virtual environments.
  - No `pip`, `pipenv`, or `poetry`. Only `uv`.
- Use **pre-commit** hooks for linting and formatting.
- Follow **GitFlow** or trunk-based development.
- Use **semantic versioning**.
- Set up CI for builds, tests, and lint checks.

---

## 📦 Dependencies

- Manage dependencies with **`uv`** only.
  - Install with: `uv add <package>`
- Pin versions in `pyproject.toml`.
- Separate dev and prod dependencies.

---

Happy hacking! ⚡

Please open issues or ask questions if anything needs clarification.
