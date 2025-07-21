import calcs

# Inputs
width =     400         # 400 mm
height =    600         # 600 mm
force =     100_000     # 100 kN
moment =    50_000_000  # 50 kNm


# --- DIMENSION TESTS ---

# Create dims instance
test_dims = calcs.dims(width, height)

dims_tests = [
    {
        "name": "area",
        "func": lambda w, h: w * h,
        "args": (width, height),
        "actual": lambda: test_dims.area
    },
    {
        "name": "perimeter",
        "func": lambda w, h: 2 * (w + h),
        "args": (width, height),
        "actual": lambda: test_dims.perimeter
    },
    {
        "name": "section_modulus",
        "func": lambda w, h: (1/6) * w * h**2,
        "args": (width, height),
        "actual": lambda: test_dims.section_modulus
    }
]

# Run dimension tests
print("--- Dims Tests ---")
for test in dims_tests:
    expected = test["func"](*test["args"])
    result = test["actual"]()
    if abs(result - expected) < 1e-6:
        print(f"{test['name']} is OK!")
    else:
        print(f"{test['name']} FAILED! Got {result}, expected {expected}")



# --- STRESS TESTS ---

# Create stress instance
test_stress = calcs.stress(force, test_dims.area, moment, test_dims.section_modulus)

stress_tests = [
    {
        "name": "normal",
        "func": lambda f, a: f / a,
        "args": (force, test_dims.area),
        "actual": lambda: test_stress.normal
    },
    {
        "name": "bending",
        "func": lambda m, s: m / s,
        "args": (moment, test_dims.section_modulus),
        "actual": lambda: test_stress.bending
    }
]

# Run stress tests
print("\n--- Stress Tests ---")
for test in stress_tests:
    expected = test["func"](*test["args"])
    result = test["actual"]()
    if abs(result - expected) < 1e-6:
        print(f"{test['name']} is OK!")
    else:
        print(f"{test['name']} FAILED! Got {result}, expected {expected}")
