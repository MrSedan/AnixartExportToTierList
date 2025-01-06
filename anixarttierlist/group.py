from collections import Counter
from typing import List

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def find_first_substring(strings: List[str]) -> str:
    if not strings:
        return ""
    if len(strings) == 1:
        return strings[0]
    lower_strings = list(map(lambda x: x.lower(), strings))

    shortest = min(lower_strings, key=len)
    for i in range(len(shortest), 0, -1):
        substring = shortest[:i]
        if all(s.startswith(substring) for s in lower_strings):
            return strings[0][:i]
    return ""


def group_by_common_part(strings, n=3) -> List[str]:
    vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(n, n))
    X = vectorizer.fit_transform(strings)
    similarity_matrix = cosine_similarity(X)

    similarity_threshold = .5

    groups = []
    assigned = [False] * len(strings)

    for i in range(len(strings)):
        if assigned[i]:
            continue

        group = [strings[i]]
        assigned[i] = True

        for j in range(i+1, len(strings)):
            if assigned[j] or similarity_matrix[i, j] < similarity_threshold:
                continue
            group.append(strings[j])
            assigned[j] = True

        common_part = find_first_substring(group)
        groups.append((group, common_part))

    return groups
