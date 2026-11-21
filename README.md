# Manim Animations

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Manim](https://img.shields.io/badge/Manim-Community-E07A5F?style=for-the-badge)

A collection of mathematical animations and visual experiments built with [Manim Community Edition](https://www.manim.community/).

---


## Getting Started

### Prerequisites
* **Python 3.9+**
* **FFmpeg** (required for video rendering)
* **LaTeX** *(optional, required for rendering math equations with `MathTex`)*

### Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/yourusername/your-repo.git](https://github.com/yourusername/your-repo.git)
   cd your-repo
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Manim**
   ```bash
   pip install --upgrade pip
   pip install manim
   ```

---

## Rendering Animations

Run any scene using the `manim` CLI:

```bash
# Fast preview (480p, 15fps)
manim -pql scene.py DrawCircle

# Smooth preview (480p, 60fps)
manim -pql --fps 60 scene.py DrawCircle

# High-quality render (1080p, 60fps)
manim -pqh scene.py DrawCircle
```

### Quality Flags Reference

| Flag | Resolution | Frame Rate |
| :--- | :--- | :--- |
| `-ql` | 480p | 15 fps |
| `-qm` | 720p | 30 fps |
| `-qh` | 1080p | 60 fps |
| `-qp` | 1440p | 60 fps |
| `-qk` | 4K (2160p) | 60 fps |

---

## Project Structure

```text
.
├── .gitignore
├── README.md
├── scene.py
├── transform.py
└── demo.py
```

*Note: The `media/` and `.venv/` folders are excluded from Git via `.gitignore`.*