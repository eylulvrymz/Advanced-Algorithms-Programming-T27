import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon
import math


# ─────────────────────────────────────────────
# FUNCTION 1 – draw_sierpinski
# ─────────────────────────────────────────────

def draw_sierpinski(ax, x, y, size, depth):
    """
    Draws a Sierpinski triangle recursively.
    (x, y) = bottom-left corner, size = side length, depth = recursion depth
    """
    if depth == 0:
        # Draw a filled triangle
        triangle = Polygon(
            [[x, y], [x + size, y], [x + size / 2, y + size * math.sqrt(3) / 2]],
            closed=True,
            facecolor="steelblue",
            edgecolor="white",
            linewidth=0.5,
        )
        ax.add_patch(triangle)
        return

    half = size / 2

    # Bottom-left sub-triangle
    draw_sierpinski(ax, x, y, half, depth - 1)
    # Bottom-right sub-triangle
    draw_sierpinski(ax, x + half, y, half, depth - 1)
    # Top sub-triangle
    draw_sierpinski(ax, x + half / 2, y + half * math.sqrt(3) / 2, half, depth - 1)


# ─────────────────────────────────────────────
# FUNCTION 2 – draw_tree
# ─────────────────────────────────────────────

def draw_tree(ax, x, y, length, angle, depth):
    """
    Draws a recursive fractal tree.
    (x, y) = base point, length = branch length, angle in degrees, depth = recursion depth
    """
    if depth == 0:
        # Draw a leaf line
        angle_rad = math.radians(angle)
        x_end = x + length * math.cos(angle_rad)
        y_end = y + length * math.sin(angle_rad)
        ax.plot([x, x_end], [y, y_end], color="green", linewidth=1)
        return

    # Compute end point of current branch
    angle_rad = math.radians(angle)
    x_end = x + length * math.cos(angle_rad)
    y_end = y + length * math.sin(angle_rad)

    # Branch thickness decreases with depth
    lw = max(0.5, depth * 0.5)
    color = "saddlebrown" if depth > 2 else "olivedrab"
    ax.plot([x, x_end], [y, y_end], color=color, linewidth=lw)

    # Recursively draw left and right sub-branches
    draw_tree(ax, x_end, y_end, length / 2, angle + 30, depth - 1)
    draw_tree(ax, x_end, y_end, length / 2, angle - 30, depth - 1)


# ─────────────────────────────────────────────
# FUNCTION 3 – fractal_dimension
# ─────────────────────────────────────────────

def fractal_dimension(fractal_image, box_sizes):
    """
    Estimates the fractal dimension using the box-counting method.
    fractal_image: 2D boolean numpy array (True = part of fractal)
    box_sizes: list of box sizes to test
    Returns: estimated fractal dimension D
    """
    counts = []
    image_height, image_width = fractal_image.shape

    for size in box_sizes:
        count = 0
        # Slide a grid of boxes over the image
        for x in range(0, image_width, size):
            for y in range(0, image_height, size):
                # Check if the box contains any part of the fractal
                box = fractal_image[y : y + size, x : x + size]
                if box.any():
                    count += 1
        counts.append(count)

    counts = np.array(counts, dtype=float)
    box_sizes = np.array(box_sizes, dtype=float)

    # Avoid log(0)
    valid = counts > 0
    log_counts = np.log(counts[valid])
    log_inv_sizes = np.log(1.0 / box_sizes[valid])

    # Slope of log(count) vs log(1/size) = fractal dimension D
    D = np.polyfit(log_inv_sizes, log_counts, 1)[0]
    return D, log_inv_sizes, log_counts


# ─────────────────────────────────────────────
# HELPER – render a Sierpinski triangle to a
#          binary image for box-counting
# ─────────────────────────────────────────────

def sierpinski_to_image(depth=5, img_size=512):
    """Renders Sierpinski triangle into a binary numpy array."""
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")

    draw_sierpinski(ax, 0, 0, 1, depth)

    # Render to numpy array
    fig.canvas.draw()
    buf = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8)
    buf = buf.reshape(fig.canvas.get_width_height()[::-1] + (4,))
    plt.close(fig)

    # Convert to binary (non-black pixels = fractal)
    binary = np.any(buf[:, :, :3] > 30, axis=2)
    return binary


# ─────────────────────────────────────────────
# MAIN – run all three and display results
# ─────────────────────────────────────────────

def main():
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.patch.set_facecolor("#1a1a2e")

    # ── Plot 1: Sierpinski Triangle ──────────
    ax1 = axes[0]
    ax1.set_facecolor("#1a1a2e")
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.set_title("Sierpinski Triangle  (depth=5)", color="white", fontsize=13, pad=10)

    draw_sierpinski(ax1, 0, 0, 1, depth=5)

    # ── Plot 2: Fractal Tree ─────────────────
    ax2 = axes[1]
    ax2.set_facecolor("#1a1a2e")
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(0, 3)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title("Fractal Tree  (depth=8)", color="white", fontsize=13, pad=10)

    # Start at bottom-center, grow upward (90°)
    draw_tree(ax2, 0, 0, 1.0, angle=90, depth=8)

    # ── Plot 3: Fractal Dimension ────────────
    ax3 = axes[2]
    ax3.set_facecolor("#1a1a2e")
    ax3.tick_params(colors="white")
    ax3.xaxis.label.set_color("white")
    ax3.yaxis.label.set_color("white")
    ax3.title.set_color("white")
    for spine in ax3.spines.values():
        spine.set_edgecolor("#444")

    print("Rendering Sierpinski image for box-counting…")
    binary_image = sierpinski_to_image(depth=5, img_size=256)

    box_sizes = [2, 4, 8, 16, 32, 64, 128]
    D, log_inv_sizes, log_counts = fractal_dimension(binary_image, box_sizes)

    # Regression line
    coeffs = np.polyfit(log_inv_sizes, log_counts, 1)
    fit_line = np.polyval(coeffs, log_inv_sizes)

    ax3.scatter(log_inv_sizes, log_counts, color="cyan", zorder=5, label="Box counts")
    ax3.plot(log_inv_sizes, fit_line, color="tomato", linewidth=2,
             label=f"Fit  →  D ≈ {D:.3f}")
    ax3.set_xlabel("log(1 / box size)")
    ax3.set_ylabel("log(count)")
    ax3.set_title("Fractal Dimension  (box-counting)", color="white", fontsize=13, pad=10)
    ax3.legend(facecolor="#2a2a4e", labelcolor="white")

    # Theoretical value for Sierpinski ≈ 1.585
    print(f"\n  Measured fractal dimension D ≈ {D:.4f}")
    print(f"  Theoretical value (Sierpinski) ≈ 1.5850")

    plt.tight_layout(pad=2)
    plt.savefig("lab7_exercise2.png", dpi=150,
                bbox_inches="tight", facecolor=fig.get_facecolor())
    print("\n  Plot saved → lab7_exercise2.png")
    plt.show()


if __name__ == "__main__":
    main()
