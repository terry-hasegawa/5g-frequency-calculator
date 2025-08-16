#!/usr/bin/env python3
"""
5G NR Frequency Calculator - Command Line Interface
Based on 3GPP TS 38.104 Release 16
"""

import argparse
import sys
from typing import Optional

from .frequency_calculator import FrequencyCalculator


def format_output(point_a_arfcn: int, point_a_freq: float, band: str) -> str:
    """Format output for display"""
    return f"Point A ARFCN: {point_a_arfcn} ({point_a_freq:.2f} MHz)"


def calculate_point_a_tdd(calc: FrequencyCalculator, args) -> None:
    """Calculate Point A for TDD bands"""
    try:
        point_a_arfcn = calc.calculate_point_a_arfcn(
            band=args.band,
            scs_khz=args.scs,
            bandwidth_mhz=args.bandwidth,
            center_arfcn=args.center_arfcn
        )
        
        point_a_freq = calc.arfcn_to_frequency(args.band, point_a_arfcn)
        
        print(f"Band: {args.band} (TDD)")
        print(f"SCS: {args.scs} kHz")
        print(f"Bandwidth: {args.bandwidth} MHz")
        print(f"Center ARFCN: {args.center_arfcn}")
        print(f"Center Frequency: {calc.arfcn_to_frequency(args.band, args.center_arfcn):.2f} MHz")
        print("-" * 50)
        print(format_output(point_a_arfcn, point_a_freq, args.band))
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def calculate_point_a_fdd(calc: FrequencyCalculator, args) -> None:
    """Calculate Point A for FDD bands"""
    try:
        dl_point_a, ul_point_a = calc.calculate_point_a_arfcn_fdd(
            band=args.band,
            scs_khz=args.scs,
            bandwidth_mhz=args.bandwidth,
            dl_center_arfcn=args.dl_center_arfcn,
            ul_center_arfcn=args.ul_center_arfcn
        )
        
        dl_point_a_freq = calc.arfcn_to_frequency(args.band, dl_point_a)
        ul_point_a_freq = calc.arfcn_to_frequency(args.band, ul_point_a)
        
        print(f"Band: {args.band} (FDD)")
        print(f"SCS: {args.scs} kHz")
        print(f"Bandwidth: {args.bandwidth} MHz")
        print(f"DL Center ARFCN: {args.dl_center_arfcn}")
        print(f"DL Center Frequency: {calc.arfcn_to_frequency(args.band, args.dl_center_arfcn):.2f} MHz")
        print(f"UL Center ARFCN: {args.ul_center_arfcn}")
        print(f"UL Center Frequency: {calc.arfcn_to_frequency(args.band, args.ul_center_arfcn):.2f} MHz")
        print("-" * 50)
        print(f"DL Point A ARFCN: {dl_point_a} ({dl_point_a_freq:.2f} MHz)")
        print(f"UL Point A ARFCN: {ul_point_a} ({ul_point_a_freq:.2f} MHz)")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def convert_arfcn_to_freq(calc: FrequencyCalculator, args) -> None:
    """Convert ARFCN to frequency"""
    try:
        frequency = calc.arfcn_to_frequency(args.band, args.arfcn)
        print(f"Band: {args.band}")
        print(f"ARFCN: {args.arfcn}")
        print(f"Frequency: {frequency:.2f} MHz")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def show_band_info(calc: FrequencyCalculator, args) -> None:
    """Show band information"""
    try:
        band_info = calc.get_band_info(args.band)
        
        print(f"Band Information: {args.band}")
        print("-" * 30)
        print(f"Name: {band_info['name']}")
        print(f"Frequency Range: {band_info['frequency_range']}")
        print(f"Duplex Mode: {band_info['duplex_mode']}")
        print(f"DL Frequency Range: {band_info['dl_freq_low']:.1f} - {band_info['dl_freq_high']:.1f} MHz")
        print(f"UL Frequency Range: {band_info['ul_freq_low']:.1f} - {band_info['ul_freq_high']:.1f} MHz")
        print(f"Delta F Global: {band_info['delta_f_global']:.1f} kHz")
        print(f"Supported SCS: {band_info['supported_scs']} kHz")
        print(f"Supported Bandwidths: {band_info['supported_bandwidths']} MHz")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="5G NR Frequency Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # TDD Band (n77) Point A calculation
  python -m src.cli point-a --band n77 --scs 30 --bandwidth 100 --center-arfcn 650000
  
  # FDD Band (n1) Point A calculation  
  python -m src.cli point-a-fdd --band n1 --scs 15 --bandwidth 10 --dl-center-arfcn 432000 --ul-center-arfcn 394000
  
  # ARFCN to frequency conversion
  python -m src.cli convert --band n77 --arfcn 650000
  
  # Show band information
  python -m src.cli band-info --band n77
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Point A calculation for TDD bands
    parser_point_a = subparsers.add_parser('point-a', help='Calculate Point A for TDD bands')
    parser_point_a.add_argument('--band', required=True, help='5G NR band (e.g., n77)')
    parser_point_a.add_argument('--scs', type=int, required=True, choices=[15, 30, 60, 120], 
                               help='Subcarrier spacing in kHz')
    parser_point_a.add_argument('--bandwidth', type=int, required=True, 
                               help='Channel bandwidth in MHz')
    parser_point_a.add_argument('--center-arfcn', type=int, required=True,
                               help='Center ARFCN')
    
    # Point A calculation for FDD bands
    parser_point_a_fdd = subparsers.add_parser('point-a-fdd', help='Calculate Point A for FDD bands')
    parser_point_a_fdd.add_argument('--band', required=True, help='5G NR band (e.g., n1)')
    parser_point_a_fdd.add_argument('--scs', type=int, required=True, choices=[15, 30, 60, 120],
                                   help='Subcarrier spacing in kHz')
    parser_point_a_fdd.add_argument('--bandwidth', type=int, required=True,
                                   help='Channel bandwidth in MHz')
    parser_point_a_fdd.add_argument('--dl-center-arfcn', type=int, required=True,
                                   help='DL Center ARFCN')
    parser_point_a_fdd.add_argument('--ul-center-arfcn', type=int, required=True,
                                   help='UL Center ARFCN')
    
    # ARFCN to frequency conversion
    parser_convert = subparsers.add_parser('convert', help='Convert ARFCN to frequency')
    parser_convert.add_argument('--band', required=True, help='5G NR band (e.g., n77)')
    parser_convert.add_argument('--arfcn', type=int, required=True, help='ARFCN to convert')
    
    # Band information
    parser_band_info = subparsers.add_parser('band-info', help='Show band information')
    parser_band_info.add_argument('--band', required=True, help='5G NR band (e.g., n77)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    calc = FrequencyCalculator()
    
    if args.command == 'point-a':
        calculate_point_a_tdd(calc, args)
    elif args.command == 'point-a-fdd':
        calculate_point_a_fdd(calc, args)
    elif args.command == 'convert':
        convert_arfcn_to_freq(calc, args)
    elif args.command == 'band-info':
        show_band_info(calc, args)


if __name__ == '__main__':
    main()