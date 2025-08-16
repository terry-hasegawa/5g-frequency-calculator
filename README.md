# 5G NR Frequency Calculator

A comprehensive Python tool for calculating 5G New Radio (NR) Point A frequencies and ARFCN conversions based on 3GPP TS 38.104 Release 16 specifications.

## Features

- **Point A ARFCN Calculation**: Calculate Point A frequencies for both TDD and FDD bands
- **ARFCN to Frequency Conversion**: Convert NR-ARFCN values to frequencies in MHz
- **Multi-band Support**: Currently supports Band n1 (FDD) and Band n77 (TDD)
- **Multiple SCS Support**: 15 kHz, 30 kHz, and 60 kHz subcarrier spacing
- **Flexible Bandwidth**: Support for various channel bandwidths (5-100 MHz)
- **CLI Interface**: Easy-to-use command-line interface
- **Python API**: Programmatic access for integration into other tools

## Supported Bands

| Band | Duplex Mode | Frequency Range | Supported SCS | Supported Bandwidths |
|------|-------------|-----------------|---------------|---------------------|
| n1   | FDD         | 1920-1980 (UL)<br>2110-2170 (DL) MHz | 15, 30 kHz | 5, 10, 15, 20, 25, 30, 40, 50 MHz |
| n77  | TDD         | 3300-4200 MHz   | 15, 30, 60 kHz | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 MHz |

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

#### 1. Point A Calculation for TDD Bands (e.g., Band n77)
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

#### 2. Point A Calculation for FDD Bands (e.g., Band n1)
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
python src/cli.py band-info --band n77
```

**Output:**
```
Band Information: n77
------------------------------
Name: n77
Frequency Range: FR1
Duplex Mode: TDD
DL Frequency Range: 3300.0 - 4200.0 MHz
UL Frequency Range: 3300.0 - 4200.0 MHz
Delta F Global: 15.0 kHz
Supported SCS: [15, 30, 60] kHz
Supported Bandwidths: [10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100] MHz
```

#### 5. Help
```bash
python src/cli.py --help
python src/cli.py point-a --help
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
print(f"Point A ARFCN: {point_a_arfcn}")

# Calculate Point A for FDD band (n1)
dl_point_a, ul_point_a = calc.calculate_point_a_arfcn_fdd(
    band='n1',
    scs_khz=15,
    bandwidth_mhz=10,
    dl_center_arfcn=432000,
    ul_center_arfcn=394000
)
print(f"DL Point A: {dl_point_a}, UL Point A: {ul_point_a}")

# Convert ARFCN to frequency
frequency = calc.arfcn_to_frequency('n77', 650000)
print(f"Frequency: {frequency:.2f} MHz")

# Get band information
band_info = calc.get_band_info('n77')
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

### Calculation Examples

#### Band n77 Example
- **Input**: Band n77, SCS 30kHz, BW 100MHz, Center ARFCN 650000
- **N_RB**: 273 (from 3GPP TS 38.101-1 Table 5.3.2-1)
- **HalfGrid**: (273 × 12 × 30) / 2 = 49,140 kHz = 49.14 MHz
- **Center Frequency**: 3450.00 MHz
- **Point A Frequency**: 3450.00 - 49.14 = 3400.86 MHz
- **Point A ARFCN**: 646724

#### Band n1 Example
- **Input**: Band n1, SCS 15kHz, BW 10MHz, DL Center ARFCN 432000
- **N_RB**: 52 (from 3GPP TS 38.101-1 Table 5.3.2-1)
- **HalfGrid**: (52 × 12 × 15) / 2 = 4,680 kHz = 4.68 MHz
- **DL Center Frequency**: 2160.00 MHz
- **DL Point A Frequency**: 2160.00 - 4.68 = 2155.32 MHz
- **DL Point A ARFCN**: 431064

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=src --cov-report=html

# Run specific test
python -m pytest tests/test_frequency_calculator.py::TestFrequencyCalculator::test_point_a_calculation_n77 -v
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
│   └── band_data.py             # 5G band definitions
├── tests/
│   ├── __init__.py
│   └── test_frequency_calculator.py
└── examples/
```

## Standards Compliance

This tool is based on the following 3GPP specifications:
- **3GPP TS 38.104 Release 16**: NR Base Station radio transmission and reception
- **3GPP TS 38.101-1**: NR User Equipment radio transmission and reception (Part 1: Range 1 Standalone)

## Roadmap

### Upcoming Features
- [ ] Additional 5G NR bands for Point A calculation (n3, n7, n28, n78, n79, etc.)
- [ ] SSB frequency candidate calculation for FDD bands
- [ ] SSB frequency candidate calculation for TDD bands
- [ ] GUI interface
- [ ] FR2

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
