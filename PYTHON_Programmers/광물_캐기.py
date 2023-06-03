DIAMOND, IRON, STONE = 0, 1, 2
fatigue_matrix = ((1, 1, 1),
                  (5, 1, 1),
                  (25, 5, 1))


def solution(picks, minerals):
    mineral_bundles = get_mineral_bundles(picks, minerals)
    mineral_bundles.sort(reverse=True)
    total_fatigue = 0
    for mineral_bundle in mineral_bundles:
        if not any(picks):
            break

        if 1 <= picks[DIAMOND]:
            total_fatigue += calc_fatigues(DIAMOND, mineral_bundle)
            picks[DIAMOND] -= 1
            continue

        elif 1 <= picks[IRON]:
            total_fatigue += calc_fatigues(IRON, mineral_bundle)
            picks[IRON] -= 1
            continue

        elif 1 <= picks[STONE]:
            total_fatigue += calc_fatigues(STONE, mineral_bundle)
            picks[STONE] -= 1
            continue

    return total_fatigue


def get_mineral_bundles(picks, minerals):
    bundles = []
    pickable_minerals = minerals[: sum(picks) * 5]
    for i in range(0, len(pickable_minerals), 5):
        bundle = [0, 0, 0]
        for j in range(i, min(i + 5, len(pickable_minerals))):
            mineral = pickable_minerals[j]
            if mineral == "diamond":
                bundle[DIAMOND] += 1
            elif mineral == "iron":
                bundle[IRON] += 1
            elif mineral == "stone":
                bundle[STONE] += 1
        bundles.append(bundle)

    return bundles


def calc_fatigues(pick, mineral_bundle):
    fatigue = 0
    for mineral, count in enumerate(mineral_bundle):
        fatigue += fatigue_matrix[pick][mineral] * count

    return fatigue