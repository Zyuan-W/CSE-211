# Follow the template in provided_tests.py to add your own tests here

Tests = [
    # Testing a simple concatenation of characters.
    ("abc", "abc", True),
    ("abc", "ab", False),
    ("abc", "abcd", False),
    
    # Testing the union of characters.
    ("a|b", "a", True),
    ("a|b", "b", True),
    ("a|b", "ab", False),
    
    # Testing Kleene star.
    ("a*", "", True),
    ("a*", "aaaa", True),
    ("a*", "b", False),
    
    # Testing the optional operator.
    ("a?", "", True),
    ("a?", "a", True),
    ("a?", "aa", False),
    ("helll?o", "helllo", True),
    ("helll?o", "hello", True),
    
    # Combining different operators.
    ("(a|b)*c", "ac", True),
    ("(a|b)*c", "aaabc", True),
    ("(a|b)*c", "abcd", False),
    
    # Complex tests
    ("(a.b|c)*", "ababcab", True),
    ("(a.b|c)*", "ccc", True),
    ("(a.b|c)*", "abc", True)
    ]
