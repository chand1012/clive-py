# Contributing to clive-py

Thank you for your interest in contributing to clive-py! This document provides guidelines and instructions for contributing to the project.

## Before You Start

Be sure to check the issue you're working on (if one exists) is not already assigned to or claimed by another contributor. That way no one duplicates work, and we can keep the project moving forward!

## Development Setup

### Prerequisites
- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv) package manager
  - Mac & Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- FFMPEG (required for audio processing)
  - Mac: `brew install ffmpeg`
  - Linux: `sudo apt-get install ffmpeg`
  - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)
- For GPU Acceleration (Optional):
  You can use either Vulkan (cross-platform) or Metal (Mac) acceleration:
- For local LLM support (Optional):
  - [Ollama](https://ollama.com/download)


### Setting Up the Development Environment
1. Fork the repository and clone your fork:
   ```bash
   git clone https://github.com/your-username/clive-py.git
   cd clive-py
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```



#### Vulkan Support:
1. Install Vulkan SDK:
   ```bash
   # On Linux/WSL
   sudo apt-get install vulkan-tools libvulkan-dev vulkan-validationlayers-dev spirv-tools

   # On Mac
   brew install vulkan-sdk molten-vk

   # On Windows
   # Download and install the Vulkan SDK from https://vulkan.lunarg.com/
   ```
2. Install pywhispercpp with Vulkan support:
   ```bash
   # Set environment variable before installing
   GGML_VULKAN=1 uv sync
   ```

#### Metal Support (Mac only):
Metal acceleration is enabled by default on Apple Silicon Macs. For additional performance, you can optionally enable CoreML support:
```bash
# Install with CoreML support for better performance
WHISPER_COREML=1 uv sync
```

## Project Structure
```
clive-py/
├── src/               # Main application code
│   ├── agents/       # Agent-related code and tools
│   └── utils/        # Utility functions
├── tests/            # Test files
├── docs/             # Documentation
├── main.py           # Main entry point
└── .env.example      # Example environment configuration
```

## Development Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use strong type hinting for all functions and variables
- Utilize modern Python features
- Keep functions focused and single-purpose
- Write clear, descriptive variable and function names
- More guidelines can be found in [CODE_STYLE.md](CODE_STYLE.md)

### Documentation
- Document all new functions, classes, and modules
- Use docstrings for Python code documentation
- Keep documentation in the `docs/` directory up to date
- Write documentation in Markdown format

### Testing
- Write tests for all new features
- Place tests in the `tests/` directory
- Ensure all tests pass before submitting a PR
- Aim for good test coverage

### Dependencies
- Use `uv add <package>` to add new dependencies
- Use `uv remove <package>` to remove dependencies
- Update requirements.txt when adding/removing dependencies

## Core Technologies
The project uses several key technologies:
- [smolagents](https://huggingface.co/docs/smolagents/guided_tour) for agentic programming
- [fire](https://github.com/google/python-fire) for CLI development
- [LiteLLM](https://docs.litellm.ai/docs) for AI platform integration
- [sqlite-vec](https://alexgarcia.xyz/sqlite-vec) for local vector database

## Pull Request Process
1. Create a new branch for your feature
2. Write your code following the guidelines above
3. Add tests for new functionality
4. Update documentation as needed
5. Submit a pull request with a clear description of changes
6. Ensure all CI checks pass

## Reporting Issues
- Use the GitHub issue tracker
- Provide clear steps to reproduce bugs
- Include relevant system information
- Use issue templates if available

## Code Review
All submissions require review. We use GitHub pull requests for this purpose:
1. Fork the repo and create your branch
2. Make your changes
3. Submit a pull request
4. Address any review comments

## License
By contributing, you agree that your contributions will be licensed under the project's license.

## Questions?
Feel free to open an issue for any questions about contributing to the project. 
