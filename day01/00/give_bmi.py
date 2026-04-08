import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    arrayw = np.array(weight)
    arrayh = np.array(height)
    return (arrayw / (arrayh ** 2)).tolist()

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    arraybmi = np.array(bmi)
    return (arraybmi > limit).tolist()


def main():
    pass

if __name__ == "__main__":
    main()