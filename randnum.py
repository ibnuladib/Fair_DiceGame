import secrets


class RandNum:
    def secure_int(min: int, max: int) -> int:
        if min > max:
            raise ValueError(f"wrong parameters")
        intrange = max - min + 1
        random_value = int.from_bytes(secrets.token_bytes(32), 'big')
        if random_value < (1 << 256) // intrange * intrange:
            return min + (random_value % intrange)
