---
name: repo
type: repo
agent: CodeActAgent
---

# Clean Code Guidelines

## Constants Over Magic Numbers
- Replace hard-coded values with named constants
- Use descriptive constant names that explain the value's purpose
- Keep constants at the top of the file or in a dedicated constants file

## Meaningful Names
- Variables, functions, and classes should reveal their purpose
- Names should explain why something exists and how it's used
- Avoid abbreviations unless they're universally understood

## Smart Comments
- Don't comment on what the code does - make the code self-documenting
- Use comments to explain why something is done a certain way
- Document APIs, complex algorithms, and non-obvious side effects

## Single Responsibility
- Each function should do exactly one thing
- Functions should be small and focused
- If a function needs a comment to explain what it does, it should be split

## DRY (Don't Repeat Yourself)
- Extract repeated code into reusable functions
- Share common logic through proper abstraction
- Maintain single sources of truth

## Clean Structure
- Keep related code together
- Organize code in a logical hierarchy
- Use consistent file and folder naming conventions

## Encapsulation
- Hide implementation details
- Expose clear interfaces
- Move nested conditionals into well-named functions

## Code Quality Maintenance
- Refactor continuously
- Fix technical debt early
- Leave code cleaner than you found it

## Testing
- Write tests before fixing bugs
- Keep tests readable and maintainable
- Test edge cases and error conditions

## Version Control
- Write clear commit messages
- Make small, focused commits
- Use meaningful branch names 

# Code Quality Guidelines

## Verify Information
Always verify information before presenting it. Do not make assumptions or speculate without clear evidence.

## File-by-File Changes
Make changes file by file and give me a chance to spot mistakes.

## No Apologies
Never use apologies.

## No Understanding Feedback
Avoid giving feedback about understanding in comments or documentation.

## No Whitespace Suggestions
Don't suggest whitespace changes.

## No Summaries
Don't summarize changes made.

## No Inventions
Don't invent changes other than what's explicitly requested.

## No Unnecessary Confirmations
Don't ask for confirmation of information already provided in the context.

## Preserve Existing Code
Don't remove unrelated code or functionalities. Pay attention to preserving existing structures.

## Single Chunk Edits
Provide all edits in a single chunk instead of multiple-step instructions or explanations for the same file.

## No Implementation Checks
Don't ask the user to verify implementations that are visible in the provided context.

## No Unnecessary Updates
Don't suggest updates or changes to files when there are no actual modifications needed.

## Provide Real File Links
Always provide links to the real files, not x.md.

## No Current Implementation
Don't show or discuss the current implementation unless specifically requested.


# Python Best Practices

## Project Structure
- Use src-layout with `src/your_package_name/`
- Place tests in `tests/` directory parallel to `src/`
- Keep configuration in `config/` or as environment variables
- Store requirements in `requirements.txt` or `pyproject.toml`
- Place static files in `static/` directory
- Use `templates/` for Jinja2 templates

## Code Style
- Follow Black code formatting
- Use isort for import sorting
- Follow PEP 8 naming conventions:
  - snake_case for functions and variables
  - PascalCase for classes
  - UPPER_CASE for constants
- Maximum line length of 88 characters (Black default)
- Use absolute imports over relative imports

## Type Hints
- Use type hints for all function parameters and returns
- Import types from `typing` module
- Use `Optional[Type]` instead of `Type | None`
- Use `TypeVar` for generic types
- Define custom types in `types.py`
- Use `Protocol` for duck typing

## Flask Structure
- Use Flask factory pattern
- Organize routes using Blueprints
- Use Flask-SQLAlchemy for database
- Implement proper error handlers
- Use Flask-Login for authentication
- Structure views with proper separation of concerns

## Database
- Use SQLAlchemy ORM
- Implement database migrations with Alembic
- Use proper connection pooling
- Define models in separate modules
- Implement proper relationships
- Use proper indexing strategies

## Authentication
- Use Flask-Login for session management
- Implement Google OAuth using Flask-OAuth
- Hash passwords with bcrypt
- Use proper session security
- Implement CSRF protection
- Use proper role-based access control

## API Design
- Use Flask-RESTful for REST APIs
- Implement proper request validation
- Use proper HTTP status codes
- Handle errors consistently
- Use proper response formats
- Implement proper rate limiting

## Testing
- Use pytest for testing
- Write tests for all routes
- Use pytest-cov for coverage
- Implement proper fixtures
- Use proper mocking with pytest-mock
- Test all error scenarios

## Security
- Use HTTPS in production
- Implement proper CORS
- Sanitize all user inputs
- Use proper session configuration
- Implement proper logging
- Follow OWASP guidelines

## Performance
- Use proper caching with Flask-Caching
- Implement database query optimization
- Use proper connection pooling
- Implement proper pagination
- Use background tasks for heavy operations
- Monitor application performance

## Error Handling
- Create custom exception classes
- Use proper try-except blocks
- Implement proper logging
- Return proper error responses
- Handle edge cases properly
- Use proper error messages

## Documentation
- Use Google-style docstrings
- Document all public APIs
- Keep README.md updated
- Use proper inline comments
- Generate API documentation
- Document environment setup

## Development Workflow
- Use virtual environments (venv)
- Implement pre-commit hooks
- Use proper Git workflow
- Follow semantic versioning
- Use proper CI/CD practices
- Implement proper logging

## Dependencies
- Pin dependency versions in pyproject.toml
- Use uv for production dependencies
- Separate development dependencies
- Enforce version constraints
- Update dependencies regularly
- Monitor security vulnerabilities

# GitHub README Best Practices for Open-Source Projects

## Introduction
A GitHub README is the gateway to an open-source project, serving as the primary resource for users and contributors. It should clearly explain what the project does, how to use it, and how to get involved, all while being well-organized and engaging. This guide provides best practices for an LLM to write a README, leveraging its ability to generate clear text and code snippets, while noting where visuals could be added by others.

## General Writing Principles
- Use **clear and concise language** to ensure accessibility for all readers, including beginners and non-native speakers.
- Adopt an **inclusive and welcoming tone** to encourage participation from diverse contributors.
- Maintain a **professional yet friendly style** to reflect the project's quality and foster community.
- Ensure **proper grammar and spelling** using tools like spell checkers to polish the text.
- Format **code snippets** with Markdown's triple backticks and specify the language (e.g., ```bash) for readability.

## README Structure
- Include standard sections: **Project Overview**, **Installation**, **Usage**, **Contributing**, **License**, etc.
- Use **Markdown headers** (`#` for main sections, `##` for subsections) to create a logical flow.
- Order sections intuitively, starting with an introduction and progressing to detailed instructions.

## Project Overview
- **Describe the project**: Start with a brief, compelling summary of what the project does. Example: "A lightweight Rust web framework for building fast, scalable APIs."
- **Highlight purpose and value**: Explain why the project exists and its unique features (e.g., "Designed for simplicity and performance, unlike heavier alternatives").
- **Target the audience**: Specify who the project is for if not obvious (e.g., "Ideal for Rust developers new to web programming").
- **Keep it short**: Limit this to 2-3 paragraphs to retain reader interest.

## Installation Instructions
- **List prerequisites**: Detail required software or libraries (e.g., "Requires Rust 1.50+ and Cargo").
- **Provide step-by-step commands**: Use code blocks for clarity. Example:
  ```bash
  git clone https://github.com/user/project.git
  cd project
  cargo build --release
  ```
- **Address multiple platforms**: Include variations for different OSes if applicable (e.g., "On Windows, use `cargo build` without sudo").
- **Test instructions**: Ensure commands are accurate and reproducible.

## Usage Examples
- **Demonstrate functionality**: Provide practical examples of how to use the project. Example:
  ```rust
  use project::App;

  fn main() {
      let app = App::new();
      app.route("/hello", |req| "Hello, world!");
      app.run(8080);
  }
  ```
- **Explain the code**: Follow snippets with plain-language descriptions (e.g., "This sets up a server responding with 'Hello, world!' on port 8080").
- **Show outputs**: Describe expected results (e.g., "Visiting `localhost:8080/hello` displays 'Hello, world!'").
- **Suggest visuals**: Note where images could help (e.g., "A screenshot of the server output would clarify this step").

## Contributing Guidelines
- **Welcome contributions**: State that all skill levels are encouraged to participate.
- **Link to details**: Reference a `CONTRIBUTING.md` file if available (e.g., "See [Contributing](./CONTRIBUTING.md) for more").
- **Outline processes**: Briefly explain how to submit issues or pull requests (e.g., "File bugs on GitHub Issues; PRs should include tests").
- **Set expectations**: Mention coding standards or requirements (e.g., "Follow Rustfmt and pass Clippy checks").

## License
- **Specify the license**: Clearly state the terms (e.g., "Licensed under MIT").
- **Include or link**: Add the full text or link to a `LICENSE` file (e.g., "[MIT License](./LICENSE)").
- **Guide selection**: Suggest using [choosealicense.com](https://choosealicense.com/) if undecided.

## Badges
- **Display status**: Use badges for build status, version, etc. Example:
  ```markdown
  ![Build](https://img.shields.io/badge/build-passing-green)
  ![License](https://img.shields.io/badge/license-MIT-blue)
  ```
- **Source badges**: Recommend services like [shields.io](https://shields.io/) and link them to relevant pages.
- **Place strategically**: Position badges at the top for immediate visibility.

## Dependencies
- **List clearly**: Include all runtime and dev dependencies. Example:
  ```markdown
  - `serde` (v1.0) - Serialization framework
  - `tokio` (v0.2) - Async runtime
  ```
- **Use tables for complexity**: For many dependencies, format as:
  | Dependency | Version | Purpose          |
  |------------|---------|------------------|
  | `serde`    | 1.0     | Serialization    |
  | `tokio`    | 0.2     | Async processing |
- **Keep updated**: Reflect the latest `Cargo.toml` or equivalent.

## Support
- **Offer help channels**: List contact options (e.g., "Join our [Discord](https://discord.gg/xyz) or email support@project.com").
- **Encourage issues**: Point to GitHub Issues (e.g., "Report bugs at [Issues](https://github.com/user/project/issues)").
- **Set response tone**: Assure timely replies (e.g., "We aim to respond within 48 hours").

## Credits
- **Recognize contributors**: Name key individuals or teams (e.g., "Thanks to @alice and @bob").
- **Link profiles**: Use GitHub handles or URLs (e.g., "[@alice](https://github.com/alice)").
- **Reference GitHub**: Suggest viewing all contributors via the repository’s contributor graph.

## Visual Suggestions
- **Recommend types**: Suggest screenshots, diagrams, or GIFs (e.g., "A GIF of the app running would show its speed").
- **Describe placement**: Advise proximity to relevant text (e.g., "Place a terminal screenshot after installation steps").
- **Acknowledge limits**: Note that LLMs can’t create visuals but can describe them (e.g., "Diagram the request flow here").
- **Mention tools**: Suggest [Asciinema](https://asciinema.org/) or [ttygif](https://github.com/icholy/ttygif) for terminal demos.

## Formatting and Style
- **Leverage Markdown**: Use headers, lists, tables, and emphasis (e.g., **bold**, *italics*).
- **Organize content**: Break long sections into subsections for skimmability.
- **Highlight key points**: Use bold or code blocks to draw attention (e.g., **Run `cargo test`**).

## Maintenance
- **Update regularly**: Revise the README with project changes to avoid outdated info.
- **Use relative links**: Link to repo files with `./` (e.g., `./docs/setup.md`) for branch compatibility.
- **Test usability**: Follow the README steps to confirm they work as written.
- **Seek feedback**: Encourage community input to refine the document.

## Conclusion
A stellar README enhances a project's accessibility and appeal, driving adoption and collaboration. By following these guidelines, an LLM can craft a README that’s informative, structured, and community-friendly, even without visuals. Keep it current and open to improvement for lasting impact.

Repository: clive-py
Description: An AI agent for processing long form video content into short clips. Should support local LLMs via Ollama as well as remote LLMs like OpenAI and Anthropic via LiteLLM.

Directory Structure:
- src/: Main application code
  - src/agents/: Any agent related code, including tools and sub-agents.
  - src/utils/: Utility code.
  - Create new folders as needed.
- tests/: Test files
- docs/: Documentation. Must be markdown.
- main.py: Main script for the user to execute.
- .env.example: Example environment variables.

Modules Used:
- [smolagents](https:/huggingface.co/docs/smolagents/guided_tour) for agentic programming.
- [fire](https:/github.com/google/python-fire) for easy CLI development.
- [LiteLLM](https:/docs.litellm.ai/docs) for using any AI platform.
- [sqlite-vec](https:/alexgarcia.xyz/sqlite-vec) for a local vector database via SQLite.
- [pywhispercpp](https://github.com/absadiki/pywhispercpp) for audio transcriptions.
  - Requres FFMPEG to be installed on the system.
  - For GPU acceleration support, see [their docs](https://github.com/absadiki/pywhispercpp?tab=readme-ov-file#nvidia-gpu-support).

Setup:
- Uses [uv](https:/docs.astral.sh/uv) for package management.
- Install `uv` on Mac & Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Install `uv` on Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- `uv sync` to create virtual environment and install packages.
- `uv add <package name>` to add packages.
- `uv remove <package name>` to remove packages

Guidelines:
- Follow PEP8 Guidelines
- Write tests for all new features
- Use strong type hinting.
- Use modern Python features.
