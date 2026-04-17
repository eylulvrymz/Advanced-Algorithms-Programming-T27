import unittest
import numpy as np
import matplotlib.pyplot as plt
from lab7_exercise2 import draw_sierpinski, draw_tree, fractal_dimension

class TestLab7Exercise2(unittest.TestCase):

    def setUp(self):
        # Create a dummy axis for drawing functions
        self.fig, self.ax = plt.subplots()

    def tearDown(self):
        plt.close(self.fig)

    def test_draw_sierpinski_base_case(self):
        """Test draw_sierpinski with depth=0."""
        try:
            draw_sierpinski(self.ax, 0, 0, 1, 0)
        except Exception as e:
            self.fail(f"draw_sierpinski failed on base case (depth=0): {e}")

    def test_draw_tree_base_case(self):
        """Test draw_tree with depth=0."""
        try:
            draw_tree(self.ax, 0, 0, 1, 90, 0)
        except Exception as e:
            self.fail(f"draw_tree failed on base case (depth=0): {e}")

    def test_negative_depth_error(self):
        """Test if negative depth causes a RecursionError (infinite recursion)."""
        with self.assertRaises(RecursionError):
            draw_sierpinski(self.ax, 0, 0, 1, -1)

    def test_fractal_dimension_empty_image(self):
        """Test box-counting with an image that has no fractal pixels."""
        img = np.zeros((100, 100), dtype=bool)
        box_sizes = [2, 4, 8]
        # Should raise an error because it can't fit a line to 0 data points
        with self.assertRaises(Exception):
             fractal_dimension(img, box_sizes)

    def test_fractal_dimension_large_boxes(self):
        """Test box-counting with box sizes larger than the image itself."""
        img = np.zeros((10, 10), dtype=bool)
        img[5, 5] = True # One pixel in the middle
        box_sizes = [20] # Larger than 10x10
        try:
            D, log_inv, log_counts = fractal_dimension(img, box_sizes)
            self.assertEqual(len(log_counts), 1)
        except Exception as e:
             self.fail(f"fractal_dimension failed with large box sizes: {e}")

    def test_fractal_dimension_zero_box_size(self):
        """Test if a box size of 0 correctly raises a ValueError."""
        img = np.ones((10, 10), dtype=bool)
        box_sizes = [0]
        with self.assertRaises(ValueError):
            fractal_dimension(img, box_sizes)

    def test_fractal_dimension_float_box_size(self):
        """Test if floating point box sizes raise a TypeError (range requires ints)."""
        img = np.ones((10, 10), dtype=bool)
        box_sizes = [2.5]
        with self.assertRaises(TypeError):
            fractal_dimension(img, box_sizes)

if __name__ == '__main__':
    unittest.main()
