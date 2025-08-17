"""
5G NR Band Data
Based on 3GPP TS 38.104 Release 16
"""

from typing import Dict, Any

# 3GPP TS 38.104 Table 5.4.2.1-1: NR operating bands
NR_BANDS = {
    'n1': {
        'name': 'n1',
        'frequency_range': 'FR1',
        'duplex_mode': 'FDD',
        'dl_freq_low': 2110.0,      # MHz
        'dl_freq_high': 2170.0,     # MHz
        'ul_freq_low': 1920.0,      # MHz  
        'ul_freq_high': 1980.0,     # MHz
        'arfcn_offset': 0,          # N_REF_Offs (0 for frequency range 0-3000 MHz)
        'ul_arfcn_offset': 0,       # N_REF_Offs for UL (same as DL for n1)
        'freq_ref_offset': 0.0,     # F_REF_Offs (0 MHz for frequency range 0-3000 MHz)
        'delta_f_global': 5.0,      # kHz (5 kHz for frequency range 0-3000 MHz)
        'delta_f_raster': 100.0,    # kHz (100 kHz raster from table)
        'supported_scs': [15, 30],  # kHz
        'supported_bandwidths': [5, 10, 15, 20, 25, 30, 40, 50],  # MHz
    },
    'n5': {
        'name': 'n5',
        'frequency_range': 'FR1',
        'duplex_mode': 'FDD',
        'dl_freq_low': 869.0,       # MHz
        'dl_freq_high': 894.0,      # MHz
        'ul_freq_low': 824.0,       # MHz
        'ul_freq_high': 849.0,      # MHz
        'arfcn_offset': 0,          # N_REF_Offs (0 for frequency range 0-3000 MHz)
        'ul_arfcn_offset': 0,       # N_REF_Offs for UL
        'freq_ref_offset': 0.0,     # F_REF_Offs (0 MHz for frequency range 0-3000 MHz)
        'delta_f_global': 5.0,      # kHz (5 kHz for frequency range 0-3000 MHz)
        'delta_f_raster': 100.0,    # kHz (100 kHz raster from table)
        'supported_scs': [15, 30],  # kHz
        'supported_bandwidths': [5, 10, 15, 20, 25, 30, 40, 50],  # MHz
    },
    'n7': {
        'name': 'n7',
        'frequency_range': 'FR1',
        'duplex_mode': 'FDD',
        'dl_freq_low': 2620.0,      # MHz
        'dl_freq_high': 2690.0,     # MHz
        'ul_freq_low': 2500.0,      # MHz
        'ul_freq_high': 2570.0,     # MHz
        'arfcn_offset': 0,          # N_REF_Offs (0 for frequency range 0-3000 MHz)
        'ul_arfcn_offset': 0,       # N_REF_Offs for UL
        'freq_ref_offset': 0.0,     # F_REF_Offs (0 MHz for frequency range 0-3000 MHz)
        'delta_f_global': 5.0,      # kHz (5 kHz for frequency range 0-3000 MHz)
        'delta_f_raster': 100.0,    # kHz (100 kHz raster from table)
        'supported_scs': [15, 30],  # kHz
        'supported_bandwidths': [5, 10, 15, 20, 25, 30, 40, 50],  # MHz
    },
    'n8': {
        'name': 'n8',
        'frequency_range': 'FR1',
        'duplex_mode': 'FDD',
        'dl_freq_low': 925.0,       # MHz
        'dl_freq_high': 960.0,      # MHz
        'ul_freq_low': 880.0,       # MHz
        'ul_freq_high': 915.0,      # MHz
        'arfcn_offset': 0,          # N_REF_Offs (0 for frequency range 0-3000 MHz)
        'ul_arfcn_offset': 0,       # N_REF_Offs for UL
        'freq_ref_offset': 0.0,     # F_REF_Offs (0 MHz for frequency range 0-3000 MHz)
        'delta_f_global': 5.0,      # kHz (5 kHz for frequency range 0-3000 MHz)
        'delta_f_raster': 100.0,    # kHz (100 kHz raster from table)
        'supported_scs': [15, 30],  # kHz
        'supported_bandwidths': [5, 10, 15, 20, 25, 30, 40, 50],  # MHz
    },
    'n12': {
        'name': 'n12',
        'frequency_range': 'FR1',
        'duplex_mode': 'FDD',
        'dl_freq_low': 729.0,       # MHz
        'dl_freq_high': 746.0,      # MHz
        'ul_freq_low': 699.0,       # MHz
        'ul_freq_high': 716.0,      # MHz
        'arfcn_offset': 0,          # N_REF_Offs (0 for frequency range 0-3000 MHz)
        'ul_arfcn_offset': 0,       # N_REF_Offs for UL
        'freq_ref_offset': 0.0,     # F_REF_Offs (0 MHz for frequency range 0-3000 MHz)
        'delta_f_global': 5.0,      # kHz (5 kHz for frequency range 0-3000 MHz)
        'delta_f_raster': 100.0,    # kHz (100 kHz raster from table)
        'supported_scs': [15, 30],  # kHz
        'supported_bandwidths': [5, 10, 15, 20, 25, 30, 40, 50],  # MHz
    },
    'n2': {
        'name': 'n2',
        'frequency_range': 'FR1',
        'duplex_mode': 'FDD',
        'dl_freq_low': 1930.0,      # MHz
        'dl_freq_high': 1990.0,     # MHz
        'ul_freq_low': 1850.0,      # MHz
        'ul_freq_high': 1910.0,     # MHz
        'arfcn_offset': 0,          # N_REF_Offs (0 for frequency range 0-3000 MHz)
        'ul_arfcn_offset': 0,       # N_REF_Offs for UL
        'freq_ref_offset': 0.0,     # F_REF_Offs (0 MHz for frequency range 0-3000 MHz)
        'delta_f_global': 5.0,      # kHz (5 kHz for frequency range 0-3000 MHz)
        'delta_f_raster': 100.0,    # kHz (100 kHz raster from table)
        'supported_scs': [15, 30],  # kHz
        'supported_bandwidths': [5, 10, 15, 20, 25, 30, 40, 50],  # MHz
    },
    'n3': {
        'name': 'n3',
        'frequency_range': 'FR1',
        'duplex_mode': 'FDD',
        'dl_freq_low': 1805.0,      # MHz
        'dl_freq_high': 1880.0,     # MHz
        'ul_freq_low': 1710.0,      # MHz
        'ul_freq_high': 1785.0,     # MHz
        'arfcn_offset': 0,          # N_REF_Offs (0 for frequency range 0-3000 MHz)
        'ul_arfcn_offset': 0,       # N_REF_Offs for UL
        'freq_ref_offset': 0.0,     # F_REF_Offs (0 MHz for frequency range 0-3000 MHz)
        'delta_f_global': 5.0,      # kHz (5 kHz for frequency range 0-3000 MHz)
        'delta_f_raster': 100.0,    # kHz (100 kHz raster from table)
        'supported_scs': [15, 30],  # kHz
        'supported_bandwidths': [5, 10, 15, 20, 25, 30, 40, 50],  # MHz
    },
    'n48': {
        'name': 'n48',
        'frequency_range': 'FR1',
        'duplex_mode': 'TDD',
        'dl_freq_low': 3550.0,      # MHz
        'dl_freq_high': 3700.0,     # MHz
        'ul_freq_low': 3550.0,      # MHz
        'ul_freq_high': 3700.0,     # MHz
        'arfcn_offset': 600000,     # N_REF_Offs (600000 for frequency range 3000-24250 MHz)
        'freq_ref_offset': 3000.0,  # F_REF_Offs (3000 MHz for frequency range 3000-24250 MHz)
        'delta_f_global': 15.0,     # kHz (15 kHz for frequency range 3000-24250 MHz)
        'delta_f_raster': 15.0,     # kHz (15 kHz raster)
        'supported_scs': [15, 30],  # kHz
        'supported_bandwidths': [10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100],  # MHz
    },
    'n77': {
        'name': 'n77',
        'frequency_range': 'FR1',
        'duplex_mode': 'TDD',
        'dl_freq_low': 3300.0,      # MHz
        'dl_freq_high': 4200.0,     # MHz
        'ul_freq_low': 3300.0,      # MHz  
        'ul_freq_high': 4200.0,     # MHz
        'arfcn_offset': 620000,     # N_REF_Offs
        'freq_ref_offset': 3000.0,  # F_REF_Offs (MHz)
        'delta_f_global': 15.0,     # kHz
        'delta_f_raster': 15.0,     # kHz
        'supported_scs': [15, 30, 60],  # kHz
        'supported_bandwidths': [10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100],  # MHz
    }
}

# GSCN (Global Synchronization Channel Number) ranges
# 3GPP TS 38.104 Table 5.4.3.1-1
GSCN_RANGES = {
    'FR1': {
        'range_1': {
            'gscn_min': 7499,
            'gscn_max': 7499,
            'freq_min': 3000.0,  # MHz
            'freq_max': 3000.0,  # MHz
            'step': 1.44,        # MHz
        },
        'range_2': {
            'gscn_min': 7500, 
            'gscn_max': 8255,
            'freq_min': 3001.44,  # MHz
            'freq_max': 4200.0,   # MHz
            'step': 1.44,         # MHz
        }
    }
}


def get_band_info(band: str) -> Dict[str, Any]:
    """
    Get band information for given band
    
    Args:
        band: Band identifier (e.g., 'n77')
        
    Returns:
        Band information dictionary
        
    Raises:
        ValueError: If band not found
    """
    if band not in NR_BANDS:
        raise ValueError(f"Unknown band: {band}")
    
    return NR_BANDS[band].copy()


def get_gscn_range(frequency_range: str) -> Dict[str, Any]:
    """
    Get GSCN range information
    
    Args:
        frequency_range: 'FR1' or 'FR2'
        
    Returns:
        GSCN range information
        
    Raises:
        ValueError: If frequency range not found
    """
    if frequency_range not in GSCN_RANGES:
        raise ValueError(f"Unknown frequency range: {frequency_range}")
    
    return GSCN_RANGES[frequency_range].copy()


def is_valid_scs(band: str, scs_khz: int) -> bool:
    """
    Check if SCS is valid for given band
    
    Args:
        band: Band identifier
        scs_khz: Subcarrier spacing in kHz
        
    Returns:
        True if valid, False otherwise
    """
    if band not in NR_BANDS:
        return False
    
    return scs_khz in NR_BANDS[band]['supported_scs']


# Maximum RB numbers for different SCS and bandwidth combinations
# Based on 3GPP TS 38.101-1 Table 5.3.2-1
MAX_RB_TABLE = {
    15: {  # 15 kHz SCS
        5: 25, 10: 52, 15: 79, 20: 106, 25: 133, 30: 160, 40: 216, 50: 270
    },
    30: {  # 30 kHz SCS  
        5: 11, 10: 24, 15: 38, 20: 51, 25: 65, 30: 78, 40: 106, 50: 133,
        60: 162, 70: 189, 80: 217, 90: 245, 100: 273
    },
    60: {  # 60 kHz SCS
        10: 11, 15: 18, 20: 24, 25: 31, 30: 38, 40: 51, 50: 65, 60: 79,
        70: 93, 80: 107, 90: 121, 100: 135
    },
    120: {  # 120 kHz SCS (FR2)
        50: 32, 100: 66, 200: 132, 400: 264
    }
}


def get_max_rb(scs_khz: int, bandwidth_mhz: int) -> int:
    """
    Get maximum RB number for given SCS and bandwidth
    Based on 3GPP TS 38.101-1 Table 5.3.2-1
    
    Args:
        scs_khz: Subcarrier spacing in kHz
        bandwidth_mhz: Channel bandwidth in MHz
        
    Returns:
        Maximum RB number
        
    Raises:
        ValueError: If invalid SCS or bandwidth combination
    """
    if scs_khz not in MAX_RB_TABLE:
        raise ValueError(f"Unsupported SCS: {scs_khz} kHz")
    
    if bandwidth_mhz not in MAX_RB_TABLE[scs_khz]:
        raise ValueError(f"Unsupported bandwidth {bandwidth_mhz} MHz for SCS {scs_khz} kHz")
    
    return MAX_RB_TABLE[scs_khz][bandwidth_mhz]


def is_valid_bandwidth(band: str, bandwidth_mhz: int) -> bool:
    """
    Check if bandwidth is valid for given band
    
    Args:
        band: Band identifier
        bandwidth_mhz: Bandwidth in MHz
        
    Returns:
        True if valid, False otherwise
    """
    if band not in NR_BANDS:
        return False
    
    return bandwidth_mhz in NR_BANDS[band]['supported_bandwidths']