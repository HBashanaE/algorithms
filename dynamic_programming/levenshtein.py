import functools

def levenshtein_distance(a, b):
    """
    the minimum number of editing operations needed to transform a string into another string. The allowed
    editing operations are as follows:
        • insert a character (e.g. ABC → ABCA )
        • remove a character (e.g. ABC → AC )
        • modify a character (e.g. ABC → ADC )

    dist(ai, bi) = min(
                            dist(ai-1, bi) + 1, -> Deletion
                            dist(ai, bi-1) + 1, -> Insertion
                            dist(ai-1, bi-1) + 1|0 -> substitution
                    )
    """
    @functools.lru_cache(maxsize=1024, typed=False)
    def distance(ai, bi):
        if ai < 0 and bi < 0:
            return 0
        deletion = insertion = modification = float("inf")
        if ai >= 0:
            deletion = distance(ai-1,bi) + 1
        if bi >= 0:
            insertion = distance(ai,bi-1) + 1
        if ai >= 0 and bi >= 0:
            cost = (a[ai] != b[bi])
            modification = distance(ai-1,bi-1) + cost

        return min(deletion, insertion, modification)
    
    v = distance(len(a)-1, len(b)-1)
    # print(distance.cache_info())
    return v

    
if __name__ == "__main__":
    print(levenshtein_distance("LOVE", "MOVIE"))