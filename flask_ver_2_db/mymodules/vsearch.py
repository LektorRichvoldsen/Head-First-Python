def search4letters(phrase: str, letters: str = 'aeiouyøæå') -> set:
    """Return as set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
