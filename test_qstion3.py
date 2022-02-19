import Question3


def test_count_anagrams():
    palavra = "ovo"
    anagrama = Question3.AnagramasCount(palavra)
    assert anagrama == 2
