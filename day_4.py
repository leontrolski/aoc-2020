from pathlib import Path

s = (Path(__file__).parent / "day_4_input.txt").read_text()

required = {
    "byr": lambda v: v.isdigit() and 1920 <= int(v) <= 2002,
    "iyr": lambda v: v.isdigit() and 2010 <= int(v) <= 2020,
    "eyr": lambda v: v.isdigit() and 2020 <= int(v) <= 2030,
    "hgt": lambda v: (
        (v.endswith("cm") or v.endswith("in"))
        and v[:-2].isdigit()
        and (150 <= int(v[:-2]) <= 193) if v[-2:] == "cm"
        else (59 <= int(v[:-2]) <= 76)
    ),
    "hcl": lambda v: (
        v.startswith("#")
        and all(l in "0123456789abcdef" for l in v[1:])
    ),
    "ecl": lambda v: v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda v: len(v) == 9 and all(l.isdigit() for l in v),
}
required_keys = set(required)

valid = 0
passports = s.split("\n\n")
for passport in passports:
    fields = dict(f.split(":") for f in passport.replace("\n", " ").split(" ") if f)
    valid += (
        (set(fields) & required_keys) == required_keys
        and all(required[k](v) for k, v in fields.items() if k in required_keys)
    )

print(valid)