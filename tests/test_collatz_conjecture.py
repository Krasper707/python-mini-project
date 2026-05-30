import unittest
import subprocess
import os

class TestCollatzConjecture(unittest.TestCase):
    def setUp(self):
        # Resolve the absolute path to the Collatz Conjecture script
        # Note: Using the exact folder name from the repo: Collatz-Conjecture
        self.script_path = os.path.join(
            os.path.dirname(__file__), "..",
            "math", "Collatz-Conjecture", "Collatz-Conjecture.py"
        )
        self.script_path = os.path.abspath(self.script_path)

    def run_script(self, inputs):
        """
        Helper to run the script and feed it simulated user inputs.
        inputs: List of strings (e.g., ["6", "y", "n"])
        """
        # Join inputs with newline. Ensure it ends with 'n' to break the while True loop
        input_data = "\n".join(inputs + ["n"]) + "\n"
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8" # Necessary for Emojis in some terminals
        
        result = subprocess.run(
            ["python", self.script_path],
            input=input_data,
            text=True,
            capture_output=True,
            encoding='utf-8',
            env=env
        )
        return result.stdout

    def test_standard_flow(self):
        """Test a simple number and ensure sequence summary is correct."""
        # Input 4, No detailed steps (n), No repeat (n)
        output = self.run_script(["4", "n"])
        self.assertIn("Starting with: 4", output)
        self.assertIn("Total steps: 2", output)
        self.assertIn("Highest number reached: 4", output)
        self.assertIn("The sequence reached 1 as expected!", output)

    def test_detailed_steps(self):
        """Test if the detailed step-by-step rendering works."""
        # Input 3, Yes to details (y), No repeat (n)
        output = self.run_script(["3", "y"])
        self.assertIn("Detailed Steps:", output)
        # Check specific mathematical logic transition: 3 is odd -> 3*3+1 = 10
        self.assertIn("3 is odd ➡️   (3 × 3) + 1 = 10", output)
        self.assertIn("Total steps: 7", output)

    def test_base_case_one(self):
        """Test the mathematical base case where input is 1."""
        # Sequence for 1 is just [1], steps = 0
        output = self.run_script(["1", "n"])
        self.assertIn("Total steps: 0", output)
        self.assertIn("Sequence length: 1", output)
    
    def test_complex_sequence_27(self):
        """Test number 27, known for having a long sequence (111 steps)."""
        output = self.run_script(["27", "n"])
        self.assertIn("Total steps: 111", output)
        self.assertIn("Highest number reached: 9232", output)
    
    def test_multi_session_loop(self):
        """Verify the 'Do you want to test another number?' loop works."""
        # First 4 (no details, yes again), then 2 (no details, no again)
        output = self.run_script(["4", "n", "y", "2", "n"])
        self.assertIn("Starting with: 4", output)
        self.assertIn("Starting with: 2", output)
        self.assertIn("Goodbye!", output)
    
    def test_input_whitespace_stripping(self):
        """Verify the script handles inputs with accidental spaces."""
        output = self.run_script(["  7  ", "n"])
        self.assertIn("Starting with: 7", output)
        self.assertIn("Total steps: 16", output)


    def test_invalid_input_handling(self):
        """Test alphabetical input and recovery."""
        # Input 'abc' (invalid), then '2' (valid), then 'n' for details, then 'n' for again
        output = self.run_script(["abc", "2", "n"])
        self.assertIn("Please enter a valid number!", output)
        self.assertIn("Starting with: 2", output)
        self.assertIn("Total steps: 1", output)

    def test_zero_and_negative_input(self):
        """Test non-positive integer validation."""
        # Input 0, then 1, then no details, then no again
        output = self.run_script(["0", "1", "n"])
        self.assertIn("Please enter a positive integer!", output)
        self.assertIn("Starting with: 1", output)

    def test_large_input_guardrail(self):
        """Test the MAX_INPUT constraint."""
        large_val = str(10**12 + 1)
        output = self.run_script([large_val, "1", "n"])
        self.assertIn("Input too large!", output)

    def test_exit_message(self):
        """Test the termination of the main loop."""
        output = self.run_script(["1", "n"])
        self.assertIn("Thanks for exploring the Collatz Conjecture! Goodbye!", output)

if __name__ == '__main__':
    unittest.main()