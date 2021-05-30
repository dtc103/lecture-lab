import re

flashcard_answers = """
What is serotonin? Answer: Serotonin is a molecule that looks something like this, it's a monoamine neurotransmitter.
Flashcard 2) Question: What is serotonin synthesized from? Answer: Serotonin is synthesized from tryptophan, which is an amino acid common in turkey.  
Flashcard 3) Question: What does serotonin do?Answer: Serotonin regulates intestinal movement, nausea and vomiting, and it also has a role in cognition.
"""


for match in re.findall(r"(.*question:)?(.+\?\s*)\n?answer:(.*)\n?", flashcard_answers, re.IGNORECASE | re.MULTILINE):
    print(match[1].rstrip().lstrip())
    print(match[2].rstrip().lstrip())
    #for i in range(1, len(match.groups()) + 1):
    #    sting = match.groups(i)
    #    print(sting)

