from pathlib import Path

s = (Path(__file__).parent / "day_5_input.txt").read_text()

seat_ids = set()
for line in s.splitlines():
    b = (
        line
        .replace("F", "0")
        .replace("B", "1")
        .replace("L", "0")
        .replace("R", "1")
    )
    seat_ids.add(int(b[:7], 2) * 8 + int(b[-3:], 2))

print(max(seat_ids))

all_ = set(range(min(seat_ids), max(seat_ids) + 1))
print(all_ - seat_ids)
