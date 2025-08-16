"""
5G NR Frequency Calculator
Based on 3GPP TS 38.104 Release 16
"""

from typing import List, Tuple, Dict, Any
from .band_data import get_band_info, is_valid_scs, is_valid_bandwidth, get_max_rb


class FrequencyCalculator:
    """
    Calculator for 5G NR Point A and SSB frequencies
    Based on 3GPP TS 38.104 Release 16
    """
    
    def __init__(self):
        """Initialize the frequency calculator"""
        # TODO: Load band data from configuration
        pass
    
    def calculate_point_a_arfcn(self, band: str, scs_khz: int, bandwidth_mhz: int, 
                               center_arfcn: int, coreset_zero: int = 0, 
                               offset_to_carrier_rb: int = 0) -> int:
        """
        Calculate Point A ARFCN from carrier center ARFCN
        Based on 3GPP TS 38.104 and TS 38.101-1
        
        Method: Calculate via frequency domain
        1. Convert center ARFCN to frequency
        2. Calculate HalfGrid = (N_RB × 12 × Δf) / 2
        3. Point A frequency = Center frequency - HalfGrid
        4. Convert Point A frequency back to ARFCN
        
        Args:
            band: 5G NR band (e.g., 'n77')
            scs_khz: Subcarrier spacing in kHz (15, 30, 60, 120)
            bandwidth_mhz: Channel bandwidth in MHz
            center_arfcn: Center ARFCN of the carrier
            coreset_zero: Control Resource Set Zero configuration (not used in this method)
            offset_to_carrier_rb: offsetToCarrier in RB units (default: 0)
            
        Returns:
            Point A ARFCN
            
        Raises:
            ValueError: If invalid parameters provided
        """
        # Validate inputs
        if not is_valid_scs(band, scs_khz):
            raise ValueError(f"Invalid SCS {scs_khz} kHz for band {band}")
        
        if not is_valid_bandwidth(band, bandwidth_mhz):
            raise ValueError(f"Invalid bandwidth {bandwidth_mhz} MHz for band {band}")
        
        # Get band information
        band_info = get_band_info(band)
        
        # Step 1: Convert center ARFCN to frequency (MHz)
        center_freq_mhz = self.arfcn_to_frequency(band, center_arfcn)
        
        # Step 2: Get maximum RB number and calculate HalfGrid
        n_rb = get_max_rb(scs_khz, bandwidth_mhz)
        half_grid_khz = (n_rb * 12 * scs_khz) / 2
        
        # Step 3: Calculate Point A frequency
        point_a_freq_mhz = center_freq_mhz - (half_grid_khz / 1000.0)  # Convert kHz to MHz
        
        # Step 4: Convert Point A frequency back to ARFCN
        # Using inverse of ARFCN to frequency formula
        freq_ref_offset = band_info['freq_ref_offset']  # MHz
        delta_f_global = band_info['delta_f_global']    # kHz
        arfcn_offset = band_info['arfcn_offset']        # N_REF_Offs
        
        point_a_arfcn = round((point_a_freq_mhz - freq_ref_offset) * 1000 / delta_f_global + arfcn_offset)
        
        return point_a_arfcn
        
    def calculate_point_a_arfcn_fdd(self, band: str, scs_khz: int, bandwidth_mhz: int, 
                                   dl_center_arfcn: int, ul_center_arfcn: int,
                                   offset_to_carrier_rb: int = 0) -> Tuple[int, int]:
        """
        Calculate Point A ARFCN for FDD bands (separate DL and UL)
        Based on 3GPP TS 38.104 and TS 38.101-1
        
        Args:
            band: 5G NR band (e.g., 'n1')
            scs_khz: Subcarrier spacing in kHz (15, 30, 60, 120)
            bandwidth_mhz: Channel bandwidth in MHz
            dl_center_arfcn: DL Center ARFCN
            ul_center_arfcn: UL Center ARFCN
            offset_to_carrier_rb: offsetToCarrier in RB units (default: 0)
            
        Returns:
            Tuple of (DL Point A ARFCN, UL Point A ARFCN)
            
        Raises:
            ValueError: If invalid parameters provided
        """
        # Validate inputs
        if not is_valid_scs(band, scs_khz):
            raise ValueError(f"Invalid SCS {scs_khz} kHz for band {band}")
        
        if not is_valid_bandwidth(band, bandwidth_mhz):
            raise ValueError(f"Invalid bandwidth {bandwidth_mhz} MHz for band {band}")
        
        # Calculate DL Point A
        dl_point_a = self.calculate_point_a_arfcn(
            band, scs_khz, bandwidth_mhz, dl_center_arfcn, 0, offset_to_carrier_rb
        )
        
        # Calculate UL Point A
        ul_point_a = self.calculate_point_a_arfcn_ul(
            band, scs_khz, bandwidth_mhz, ul_center_arfcn, offset_to_carrier_rb
        )
        
        return dl_point_a, ul_point_a
    
    def calculate_point_a_arfcn_ul(self, band: str, scs_khz: int, bandwidth_mhz: int,
                                  ul_center_arfcn: int, offset_to_carrier_rb: int = 0) -> int:
        """
        Calculate UL Point A ARFCN for FDD bands
        
        Args:
            band: 5G NR band (e.g., 'n1')
            scs_khz: Subcarrier spacing in kHz
            bandwidth_mhz: Channel bandwidth in MHz
            ul_center_arfcn: UL Center ARFCN
            offset_to_carrier_rb: offsetToCarrier in RB units (default: 0)
            
        Returns:
            UL Point A ARFCN
        """
        # Get band information
        band_info = get_band_info(band)
        
        # Convert UL center ARFCN to frequency (MHz)
        # For UL, we need to use UL frequency calculation
        freq_ref_offset = band_info['freq_ref_offset']
        delta_f_global = band_info['delta_f_global']
        arfcn_offset = band_info.get('ul_arfcn_offset', band_info['arfcn_offset'])
        
        ul_center_freq_mhz = freq_ref_offset + (delta_f_global * (ul_center_arfcn - arfcn_offset) / 1000.0)
        
        # Calculate HalfGrid
        n_rb = get_max_rb(scs_khz, bandwidth_mhz)
        half_grid_khz = (n_rb * 12 * scs_khz) / 2
        
        # Calculate UL Point A frequency
        ul_point_a_freq_mhz = ul_center_freq_mhz - (half_grid_khz / 1000.0)
        
        # Convert back to ARFCN
        ul_point_a_arfcn = round((ul_point_a_freq_mhz - freq_ref_offset) * 1000 / delta_f_global + arfcn_offset)
        
        return ul_point_a_arfcn
    
    def arfcn_to_frequency(self, band: str, arfcn: int) -> float:
        """
        Convert ARFCN to frequency in MHz
        Based on 3GPP TS 38.104 Section 5.4.2.1
        
        Args:
            band: 5G NR band (e.g., 'n77')
            arfcn: ARFCN value
            
        Returns:
            Frequency in MHz
            
        Raises:
            ValueError: If invalid band or ARFCN
        """
        band_info = get_band_info(band)
        
        # Formula: F_REF = F_REF_Offs + Δf_global(N_REF - N_REF_Offs) / 1000
        # Where:
        # - F_REF_Offs: Reference frequency offset (MHz)
        # - Δf_global: Global frequency grid step (kHz) 
        # - N_REF: NR-ARFCN
        # - N_REF_Offs: ARFCN offset
        
        freq_ref_offset = band_info['freq_ref_offset']  # MHz
        delta_f_global = band_info['delta_f_global']    # kHz
        arfcn_offset = band_info['arfcn_offset']        # N_REF_Offs
        
        frequency = freq_ref_offset + (delta_f_global * (arfcn - arfcn_offset) / 1000.0)
        
        return frequency
    
    def get_band_info(self, band: str) -> Dict[str, Any]:
        """
        Get band information
        
        Args:
            band: 5G NR band (e.g., 'n77')
            
        Returns:
            Dictionary containing band information
            
        Raises:
            ValueError: If invalid band
        """
        return get_band_info(band)
    
    # TODO: Implement SSB and GSCN related methods later
    def calculate_ssb_candidates(self, band: str, scs_khz: int, bandwidth_mhz: int,
                                center_arfcn: int, coreset_zero: int) -> List[Tuple[int, int]]:
        """SSB candidate calculation - to be implemented"""
        raise NotImplementedError("SSB candidate calculation not implemented yet")
    
    def arfcn_to_gscn(self, band: str, arfcn: int) -> int:
        """ARFCN to GSCN conversion - to be implemented"""
        raise NotImplementedError("ARFCN to GSCN conversion not implemented yet")
    
    def gscn_to_arfcn(self, band: str, gscn: int) -> int:
        """GSCN to ARFCN conversion - to be implemented"""
        raise NotImplementedError("GSCN to ARFCN conversion not implemented yet")