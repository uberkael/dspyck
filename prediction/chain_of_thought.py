# %%
import dspy  # type: ignore
import platform
from config.config import lm
from signature import DescriptionCommand


_ = lm


def predict(q: str = "list all files and hidden files in the current directory") -> DescriptionCommand:
	"""Predict the command to execute based on the question."""
	p = dspy.ChainOfThought(DescriptionCommand)
	return p(question=f"in a operating system: {platform.system()}, what is the command and arguments to do: {q}")
