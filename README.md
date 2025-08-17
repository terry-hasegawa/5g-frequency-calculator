# 5G NR Frequency Calculator

A comprehensive Python tool for calculating 5G New Radio (NR) Point A frequencies and ARFCN conversions based on 3GPP TS 38.104 Release 16 specifications.

## Features

- **Point A ARFCN Calculation**: Calculate Point A frequencies for both TDD and FDD bands
- **ARFCN to Frequency Conversion**: Convert NR-ARFCN values to frequencies in MHz
- **Multi-band Support**: Currently supports 9 major FR1 bands
- **Multiple SCS Support**: 15 kHz, 30 kHz, and 60 kHz subcarrier spacing
- **Flexible Bandwidth**: Support for various channel bandwidths (5-100 MHz)
- **CLI Interface**: Easy-to-use command-line interface
- **Python API**: Programmatic access for integration into other tools

## Supported Bands

| Band | Purpose | Duplex Mode | Frequency Range (MHz) | Supported SCS (kHz) | Supported Bandwidths (MHz) |
|------|---------|-------------|----------------------|--------------------|-----------------------------|
| n1   | 2GHz Band | FDD | UL: 1920-1980<br>DL: 2110-2170 | 15, 30 | 5, 10, 15, 20, 25, 30, 40, 50 |
| n2   | PCS | FDD | UL: 1850-1910<br>DL: 1930-1990 | 15, 30 | 5, 10, 15, 20, 25, 30, 40, 50 |
| n3   | DCS | FDD | UL: 1710-1785<br>DL: 1805-1880 | 15, 30 | 5, 10, 15, 20, 25, 30, 40, 50 |
| n5   | 850MHz Band | FDD | UL: 824-849<br>DL: 869-894 | 15, 30 | 5, 10, 15, 20, 25, 30, 40, 50 |
| n7   | 2.6GHz Band | FDD | UL: 2500-2570<br>DL: 2620-2690 | 15, 30 | 5, 10, 15, 20, 25, 30, 40, 50 |
| n8   | 900MHz Band | FDD | UL: 880-915<br>DL: 925-960 | 15, 30 | 5, 10, 15, 20, 25, 30, 40, 50 |
| n12  | 700MHz Band | FDD | UL: 699-716<br>DL: 729-746 | 15, 30 | 5, 10, 15, 20, 25, 30, 40, 50 |
| n48  | CBRS | TDD | 3550-3700 | 15, 30 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |
| n77  | C-Band | TDD | 3300-4200 | 15, 30, 60 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |

## Installation

### Requirements
- Python 3.8 or higher
- pytest (for testing)
- numpy (for calculations)

### Setup
```bash
# Clone the repository
git clone https://github.com/your-username/5g-frequency-calculator.git
cd 5g-frequency-calculator

# Install dependencies
pip install -r requirements.txt

# Run tests to verify installation
python -m pytest tests/ -v
```

## Usage

### Command Line Interface

#### 1. Point A Calculation for TDD Bands

**Band n77 (C-Band)**
```bash
python src/cli.py point-a --band n77 --scs 30 --bandwidth 100 --center-arfcn 650000
```
**Output:**
```
Band: n77 (TDD)
SCS: 30 kHz
Bandwidth: 100 MHz
Center ARFCN: 650000
Center Frequency: 3450.00 MHz
--------------------------------------------------
Point A ARFCN: 646724 (3400.86 MHz)
```

**Band n48 (CBRS)**
```bash
python src/cli.py point-a --band n48 --scs 30 --bandwidth 50 --center-arfcn 641668
```

#### 2. Point A Calculation for FDD Bands

**Band n1 (2GHz Band)**
```bash
python src/cli.py point-a-fdd --band n1 --scs 15 --bandwidth 10 --dl-center-arfcn 432000 --ul-center-arfcn 394000
```
**Output:**
```
Band: n1 (FDD)
SCS: 15 kHz
Bandwidth: 10 MHz
DL Center ARFCN: 432000
DL Center Frequency: 2160.00 MHz
UL Center ARFCN: 394000
UL Center Frequency: 1970.00 MHz
--------------------------------------------------
DL Point A ARFCN: 431064 (2155.32 MHz)
UL Point A ARFCN: 393064 (1965.32 MHz)
```

**Other FDD Bands (Single ARFCN input)**
```bash
# Band n7 (2.6GHz Band)
python src/cli.py point-a --band n7 --scs 15 --bandwidth 25 --center-arfcn 531000

# Band n8 (900MHz Band)
python src/cli.py point-a --band n8 --scs 15 --bandwidth 5 --center-arfcn 188500

# Band n12 (700MHz Band)
python src/cli.py point-a --band n12 --scs 15 --bandwidth 15 --center-arfcn 147500
```

#### 3. ARFCN to Frequency Conversion
```bash
python src/cli.py convert --band n77 --arfcn 650000
```
**Output:**
```
Band: n77
ARFCN: 650000
Frequency: 3450.00 MHz
```

#### 4. Band Information
```bash
python src/cli.py band-info --band n7
```
**Output:**
```
Band Information: n7
------------------------------
Name: n7
Frequency Range: FR1
Duplex Mode: FDD
DL Frequency Range: 2620.0 - 2690.0 MHz
UL Frequency Range: 2500.0 - 2570.0 MHz
Delta F Global: 5.0 kHz
Supported SCS: [15, 30] kHz
Supported Bandwidths: [5, 10, 15, 20, 25, 30, 40, 50] MHz
```

#### 5. Help
```bash
python src/cli.py --help
python src/cli.py point-a --help
python src/cli.py point-a-fdd --help
```

### Python API

```python
from src.frequency_calculator import FrequencyCalculator

# Initialize calculator
calc = FrequencyCalculator()

# Calculate Point A for TDD band (n77)
point_a_arfcn = calc.calculate_point_a_arfcn(
    band='n77',
    scs_khz=30,
    bandwidth_mhz=100,
    center_arfcn=650000
)
print(f"Point A ARFCN: {point_a_arfcn}")  # Output: 646724

# Calculate Point A for FDD band (n1)
dl_point_a, ul_point_a = calc.calculate_point_a_arfcn_fdd(
    band='n1',
    scs_khz=15,
    bandwidth_mhz=10,
    dl_center_arfcn=432000,
    ul_center_arfcn=394000
)
print(f"DL Point A: {dl_point_a}, UL Point A: {ul_point_a}")  # Output: 431064, 393064

# Calculate Point A for FDD band (single ARFCN)
point_a_arfcn = calc.calculate_point_a_arfcn(
    band='n7',
    scs_khz=15,
    bandwidth_mhz=25,
    center_arfcn=531000
)
print(f"Point A ARFCN: {point_a_arfcn}")  # Output: 528606

# Convert ARFCN to frequency
frequency = calc.arfcn_to_frequency('n77', 650000)
print(f"Frequency: {frequency:.2f} MHz")  # Output: 3450.00 MHz

# Get band information
band_info = calc.get_band_info('n7')
print(f"Band: {band_info['name']}, Mode: {band_info['duplex_mode']}")
```

## Technical Implementation

### Point A Calculation Method

The calculator uses the following method for Point A calculation:

1. **Convert center ARFCN to frequency** using 3GPP formula:
   ```
   F_REF = F_REF_Offs + Δf_global × (N_REF - N_REF_Offs) / 1000
   ```

2. **Calculate HalfGrid**:
   ```
   HalfGrid = (N_RB × 12 × SCS) / 2 [kHz]
   ```

3. **Calculate Point A frequency**:
   ```
   Point A Frequency = Center Frequency - HalfGrid
   ```

4. **Convert back to ARFCN** using inverse formula

### ARFCN Parameters by Frequency Range

| Frequency Range | F_REF_Offs (MHz) | N_REF_Offs | Δf_global (kHz) | Bands |
|-----------------|------------------|------------|-----------------|-------|
| 0 - 3000 MHz    | 0               | 0          | 5               | n1, n2, n3, n5, n7, n8, n12 |
| 3000 - 24250 MHz| 3000            | 600000     | 15              | n48, n77 |

### Calculation Examples

#### Band n7 (2.6GHz FDD) Example
- **Input**: Band n7, SCS 15kHz, BW 25MHz, Center ARFCN 531000
- **N_RB**: 133 (from 3GPP TS 38.101-1 Table 5.3.2-1)
- **HalfGrid**: (133 × 12 × 15) / 2 = 11,970 kHz = 11.97 MHz
- **Center Frequency**: 2655.00 MHz
- **Point A Frequency**: 2655.00 - 11.97 = 2643.03 MHz
- **Point A ARFCN**: 528606

#### Band n8 (900MHz FDD) Example
- **Input**: Band n8, SCS 15kHz, BW 5MHz, Center ARFCN 188500
- **N_RB**: 25 (from 3GPP TS 38.101-1 Table 5.3.2-1)
- **HalfGrid**: (25 × 12 × 15) / 2 = 2,250 kHz = 2.25 MHz
- **Center Frequency**: 942.50 MHz
- **Point A Frequency**: 942.50 - 2.25 = 940.25 MHz
- **Point A ARFCN**: 188050

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=src --cov-report=html

# Run specific test for new bands
python -m pytest tests/test_frequency_calculator.py::TestFrequencyCalculator::test_additional_bands_calculations -v
```

**Test Results:**
```
16 passed, 0 failed
- Point A calculations for all 9 bands
- ARFCN to frequency conversions
- Edge cases and error handling
- FDD dual-band calculations
```

## Project Structure

```
5g-frequency-calculator/
├── README.md
├── LICENSE (MIT)
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py                    # Command-line interface
│   ├── frequency_calculator.py   # Main calculator class
│   └── band_data.py             # 5G band definitions (9 bands)
├── tests/
│   ├── __init__.py
│   └── test_frequency_calculator.py  # 16 test cases
└── examples/
```

## Standards Compliance

This tool is based on the following 3GPP specifications:
- **3GPP TS 38.104 Release 16**: NR Base Station radio transmission and reception
- **3GPP TS 38.101-1**: NR User Equipment radio transmission and reception (Part 1: Range 1 Standalone)

## Roadmap

### Current Implementation (v0.1.0)
- ✅ Point A ARFCN calculation for TDD and FDD bands
- ✅ 9 major FR1 bands (n1, n2, n3, n5, n7, n8, n12, n48, n77)
- ✅ ARFCN to frequency conversion
- ✅ Multiple SCS support (15, 30, 60 kHz)
- ✅ Flexible bandwidth support (5-100 MHz)
- ✅ Comprehensive CLI interface
- ✅ Complete test coverage

### Upcoming Features
- [ ] Complete FR1 band coverage (n20, n25, n28, n34, n38, n39, n40, n41, n66, n70, n71, n78, n79, etc.)
- [ ] SSB frequency candidate calculation for FDD bands
- [ ] SSB frequency candidate calculation for TDD bands
- [ ] GSCN (Global Synchronization Channel Number) conversion
- [ ] Control Resource Set Zero configuration support
- [ ] GUI interface

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-band`)
3. Add tests for new functionality
4. Implement the feature following TDD approach
5. Run the test suite (`python -m pytest tests/ -v`)
6. Commit your changes (`git commit -am 'Add new band support'`)
7. Push to the branch (`git push origin feature/new-band`)
8. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Terry
