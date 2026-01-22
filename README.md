# Math XXXX Notes: Course Name

An accessible, open-source mathematics textbook built with Sphinx and hosted on GitHub Pages.

## Overview

This project is a comprehensive textbook (or lecture notes) designed with accessibility as a core principle. It uses Sphinx with the Sphinx Book Theme to create a modern, responsive, and fully accessible learning resource.

**Live Site:** [https://codmccabe.github.io/sphinxTemplate2.0/](https://codmccabe.github.io/sphinxTemplate2.0/)

## Features

**Fully Accessible**
- WCAG compliant design
- Semantic HTML structure
- Keyboard navigation support
- Screen reader compatible
- High contrast and dark mode support

**Rich Content Support**
- Markdown and reStructuredText files
- Mathematical equations with LaTeX (`$...$`)
- TikZ diagrams for mathematical visualizations
- Interactive code examples
- Video embedding

**Modern Design**
- Responsive design for all devices
- Sphinx Book Theme with clean UI
- Collapsible chapter navigation
- Syntax highlighting for code
- Dark mode support

**Automated Deployment**
- GitHub Actions CI/CD pipeline
- Automatic builds on push to main
- Auto-deployment to GitHub Pages
- Pull request preview artifacts

## Getting Started

### Prerequisites

- Linux Mint (or Linux/macOS/Windows with WSL)
- Python 3.11+
- Conda (Miniconda or Anaconda)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/codmccabe/sphinxTemplate2.0.git
   cd sphinxTemplate2.0
   ```

2. **Create conda environment:**
   ```bash
   bash setup_conda.sh
   ```

3. **Activate environment:**
   ```bash
   conda activate sphinx-textbook
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

### Building Locally

**Quick Build:**
```bash
sphinx-build -T -W --keep-going doc _build/html
```

**Using the build helper script:**
```bash
chmod +x build.sh
./build.sh
```

Then select option 5 (Clean + Build + Open) to clean, build, and open in Firefox.

**View the documentation:**
```bash
firefox _build/html/index.html
```

Or open `_build/html/index.html` in your browser.

## Project Structure

```
sphinxTemplate2.0/
├── .github/workflows/
│   └── build.yml                    # GitHub Actions workflow
├── doc/
│   ├── _static/
│   │   ├── custom_accessibility.css # Custom accessibility styles
│   │   └── lightbox_init.js         # Lightbox functionality (optional)
│   ├── chapter1/
│   │   ├── c1.rst                   # Chapter 1 toctree
│   │   ├── 11.md through 16.md      # Chapter 1 sections
│   ├── chapter2/ through chapter5/   # Similar structure for other chapters
│   ├── conf.py                      # Sphinx configuration
│   └── index.rst                    # Main index/landing page
├── build.sh                         # Build helper script
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## Writing Content

### Basic Markdown Structure

Create markdown files in chapter folders:

```markdown
# Section Title

Your content here with **bold**, *italic*, and `code`.

## Subsection

More detailed content.
```

### Math Equations

Use dollar signs for inline and display math:

```markdown
Inline math: $y = x^2$

Display math:
$$\int_0^1 x^2 \, dx = \frac{1}{3}$$
```

### TikZ Diagrams

Create mathematical diagrams with TikZ:

````markdown
```{tikz}
:alt: A parabola showing y equals x squared

\begin{tikzpicture}[scale=1.5]
  \draw[->] (-3,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,5) node[above] {$y$};
  \draw[blue, thick, domain=-2.5:2.5, samples=100] plot (\x, {\x*\x});
  \node[blue, above right] at (1.5,2.25) {$y = x^2$};
\end{tikzpicture}
```
````

### Collapsible Content

Use toggles to hide/show content:

````markdown
```{toggle}
Click to reveal solution

The answer is 42.
```
````

### Cards and Callouts

Use design components for emphasis:

````markdown
```{note}
This is important information.
```

```{warning}
Be careful with this!
```

```{tip}
Helpful hint for solving problems.
```
````

### Images with Alt Text

Always include descriptive alt text:

```markdown
![A graph showing the parabola y equals x squared with vertex at origin](images/parabola.png)
```

## Configuration

### Main Files

**`conf.py`** - Sphinx configuration
- Project metadata
- Extensions list
- Theme settings
- Math rendering options

**`requirements.txt`** - Python dependencies
- All Sphinx packages
- Extensions
- Supporting libraries

**`.github/workflows/build.yml`** - GitHub Actions workflow
- Triggers on push to main and PRs
- Installs dependencies
- Builds documentation
- Deploys to GitHub Pages

### Key Extensions

- **myst_parser** - Markdown support
- **sphinx_design** - UI components (cards, tabs)
- **sphinx_book_theme** - Modern, accessible theme
- **sphinxcontrib.tikz** - TikZ diagram support
- **sphinx_accessibility** - Accessibility checks
- **sphinx_tabs** - Tabbed content
- **sphinx_togglebutton** - Collapsible sections

## Deployment

### GitHub Pages Setup

1. Go to **Settings** → **Pages**
2. Select **gh-pages** branch as source
3. Save
4. Site will be available at `https://yourusername.github.io/sphinxTemplate2.0/`

### Automatic Deployment

The GitHub Actions workflow automatically:
- Builds on every push to `main`
- Builds on pull requests (creates artifact preview)
- Deploys to GitHub Pages after successful build

Check the **Actions** tab to monitor builds.

### Manual Rebuild

Go to **Actions** → **build and deploy docs** → **Run workflow**

## Accessibility Features

### Built-in

- Semantic HTML with proper heading hierarchy
- Color contrast meeting WCAG AA standards
- Keyboard navigation with arrow keys
- Focus indicators for all interactive elements
- Alt text for all images and diagrams
- Dark mode support
- Responsive design for all screen sizes

### Best Practices

1. **Always include alt text** for images/diagrams
2. **Use proper heading hierarchy** (don't skip levels)
3. **Use descriptive link text** (avoid "click here")
4. **Provide text alternatives** for visual content
5. **Test with screen readers** when possible
6. **Maintain color contrast** in custom content

## Common Tasks

### Add a New Chapter

1. Create `doc/chapterX/cX.rst` with:
```rst
.. toctree::
   :maxdepth: 1

   X1.md
   X2.md
   X3.md
   X4.md
   X5.md
```

2. Add to `doc/index.rst`:
```rst
.. toctree::
   chapterX/cX.rst
```

3. Create blank markdown files `X1.md` through `X5.md` with titles

### Add a New Section

1. Create `doc/chapterX/Y#.md` with title
2. It's automatically included via the chapter's `cX.rst`

### Update Dependencies

```bash
pip install --upgrade -r requirements.txt
```

### Clean Build

```bash
rm -rf _build
sphinx-build -T -W --keep-going doc _build/html
```

## Troubleshooting

### Build Fails Locally

```bash
conda activate sphinx-textbook
pip install -r requirements.txt --force-reinstall
rm -rf _build
sphinx-build -T -W --keep-going doc _build/html
```

### Math Not Rendering

- Check syntax: `$inline$` or `$$display$$`
- Ensure `dollarmath` is in `myst_enable_extensions` in `conf.py`
- Rebuild: `rm -rf _build && sphinx-build -T -W --keep-going doc _build/html`

### TikZ Diagrams Not Showing

- Install system dependency: `sudo apt-get install texlive-latex-base`
- Check TikZ syntax for errors
- Rebuild documentation

### Changes Not Appearing

- Clear build: `rm -rf _build`
- Rebuild: `sphinx-build -T -W --keep-going doc _build/html`
- Hard refresh browser: `Ctrl+Shift+R` (or `Cmd+Shift+R` on Mac)

## Contributing

1. Create a new branch: `git checkout -b feature/your-feature`
2. Make changes (follow accessibility guidelines)
3. Test locally: `./build.sh`
4. Commit: `git commit -m "Description of changes"`
5. Push: `git push origin feature/your-feature`
6. Create pull request on GitHub

## File Naming Convention

- **Chapters:** `chapterX/cX.rst`
- **Sections:** `chapterX/Y#.md` (e.g., `chapter1/11.md`)
- **Static files:** `doc/_static/`

## Dependencies

Core dependencies:
- sphinx >= 7.2.6
- sphinx-book-theme
- myst-parser
- sphinxcontrib-tikz
- sphinx-design
- sphinx-accessibility
- sphinx-tabs
- sphinx-togglebutton

See `requirements.txt` for complete list and versions.

## Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [MyST Parser Guide](https://myst-parser.readthedocs.io/)
- [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/)
- [TikZ Documentation](https://tikz.dev/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Web Accessibility](https://www.w3.org/WAI/)

## License

This project is open source and available under the GPL-3.0 License.

## Support

For issues, questions, or suggestions:
1. Check existing [GitHub Issues](https://github.com/codmccabe/sphinxTemplate2.0/issues)
2. Create a new issue with detailed description
3. Include error messages and build output if applicable

## Author

Created by Michael McCabe as an accessible mathematics textbook resource.

---

**Last Updated:** January 2025
**Sphinx Version:** 9.0.4
**Python Version:** 3.11