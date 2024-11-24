def count_vowels(s: str) -> int:
    """Возвращает количество гласных в строке s."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)