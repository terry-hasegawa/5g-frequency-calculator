"""
Unit tests for 5G NR frequency calculator
Based on 3GPP TS 38.104 Release 16
"""

import unittest
from src.frequency_calculator import FrequencyCalculator


class TestFrequencyCalculator(unittest.TestCase):
    """Test cases for 5G NR frequency calculations"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = FrequencyCalculator()
    
    def test_point_a_calculation_n77(self):
        """Test Point A calculation for Band n77"""
        # Test case: Band n77, SCS 30kHz, BW 100MHz, Center ARFCN 650000
        # Expected Point A ARFCN: 646724 (3400.86 MHz)
        
        point_a_arfcn = self.calc.calculate_point_a_arfcn(
            band='n77',
            scs_khz=30,
            bandwidth_mhz=100,
            center_arfcn=650000
        )
        
        self.assertEqual(point_a_arfcn, 646724, 
                        "Point A ARFCN calculation failed for Band n77")
        
        # Verify Point A frequency
        point_a_freq = self.calc.arfcn_to_frequency('n77', point_a_arfcn)
        self.assertAlmostEqual(point_a_freq, 3400.86, places=2,
                              msg="Point A frequency conversion failed")
    
    def test_ssb_frequency_candidates_n77(self):
        """Test SSB frequency candidates for Band n77"""
        # Expected SSB candidates for the test case
        expected_ssb_candidates = [
            (7992, 647328),  # GSCN 7992, ARFCN 647328
            (7993, 647424),  # GSCN 7993, ARFCN 647424
            # ... more candidates up to GSCN 8047, ARFCN 652608
        ]
        
        ssb_candidates = self.calc.calculate_ssb_candidates(
            band='n77',
            scs_khz=30,
            bandwidth_mhz=100,
            center_arfcn=650000,
            coreset_zero=10
        )
        
        # Test first few candidates
        self.assertGreater(len(ssb_candidates), 0, 
                          "No SSB candidates found")
        
        # Check specific expected values
        self.assertIn((7992, 647328), ssb_candidates,
                     "Expected SSB candidate GSCN 7992 not found")
        
        # Check last expected candidate
        last_candidate = max(ssb_candidates, key=lambda x: x[0])
        self.assertEqual(last_candidate, (8047, 652608),
                        "Last SSB candidate incorrect")
    
    def test_arfcn_frequency_conversion_n77(self):
        """Test ARFCN to frequency conversion for Band n77"""
        # Test Point A ARFCN to frequency
        freq = self.calc.arfcn_to_frequency('n77', 646724)
        self.assertAlmostEqual(freq, 3400.86, places=2)
        
        # Test center ARFCN to frequency  
        freq = self.calc.arfcn_to_frequency('n77', 650000)
        self.assertAlmostEqual(freq, 3450.0, places=2)
        
        # Test some other known values
        freq = self.calc.arfcn_to_frequency('n77', 620000)  # Reference point
        self.assertAlmostEqual(freq, 3000.0, places=2)
    
    def test_point_a_calculation_multiple_cases(self):
        """Test Point A calculation for multiple bandwidth and SCS combinations"""
        
        # Test cases for Band n77 with different configurations
        test_cases = [
            # (SCS, BW, Center_ARFCN, Expected_PointA_ARFCN)
            (30, 100, 650000, 646724),  # Main test case
            (30, 50, 650000, 648404),   # 50MHz bandwidth
            (30, 20, 650000, 649388),   # 20MHz bandwidth  
            (15, 20, 650000, 649364),   # 15kHz SCS
        ]
        
        for scs_khz, bw_mhz, center_arfcn, expected_point_a in test_cases:
            with self.subTest(scs=scs_khz, bw=bw_mhz, center=center_arfcn):
                point_a_arfcn = self.calc.calculate_point_a_arfcn(
                    band='n77',
                    scs_khz=scs_khz,
                    bandwidth_mhz=bw_mhz,
                    center_arfcn=center_arfcn
                )
                
                self.assertEqual(point_a_arfcn, expected_point_a,
                               f"Point A ARFCN mismatch for SCS={scs_khz}, BW={bw_mhz}")
                
                # Verify frequency calculation consistency
                point_a_freq = self.calc.arfcn_to_frequency('n77', point_a_arfcn)
                center_freq = self.calc.arfcn_to_frequency('n77', center_arfcn)
                
                from src.band_data import get_max_rb
                n_rb = get_max_rb(scs_khz, bw_mhz)
                half_grid_mhz = (n_rb * 12 * scs_khz) / 2 / 1000.0
                expected_point_a_freq = center_freq - half_grid_mhz
                
                self.assertAlmostEqual(point_a_freq, expected_point_a_freq, places=2,
                                     msg=f"Point A frequency mismatch for SCS={scs_khz}, BW={bw_mhz}")
    
    def test_point_a_edge_cases(self):
        """Test Point A calculation edge cases"""
        
        # Test minimum bandwidth
        point_a = self.calc.calculate_point_a_arfcn('n77', 30, 10, 650000)
        self.assertIsInstance(point_a, int)
        
        # Test maximum bandwidth
        point_a = self.calc.calculate_point_a_arfcn('n77', 30, 100, 650000)
        self.assertIsInstance(point_a, int)
        
        # Test different SCS values
        for scs in [15, 30, 60]:
            if scs == 60:  # 60kHz SCS has limited bandwidth options
                point_a = self.calc.calculate_point_a_arfcn('n77', scs, 30, 650000)
            else:
                point_a = self.calc.calculate_point_a_arfcn('n77', scs, 20, 650000)
            self.assertIsInstance(point_a, int)
    
    def test_band_info_n77(self):
        """Test band information retrieval for Band n77"""
        band_info = self.calc.get_band_info('n77')
        
        self.assertEqual(band_info['name'], 'n77')
        self.assertEqual(band_info['frequency_range'], 'FR1')
        self.assertIn('dl_freq_low', band_info)
        self.assertIn('dl_freq_high', band_info)
        self.assertIn('arfcn_offset', band_info)
    
    def test_invalid_inputs(self):
        """Test error handling for invalid inputs"""
        # Invalid band
        with self.assertRaises(ValueError):
            self.calc.calculate_point_a_arfcn('n999', 30, 100, 650000)
        
        # Invalid SCS
        with self.assertRaises(ValueError):
            self.calc.calculate_point_a_arfcn('n77', 25, 100, 650000)
        
        # Invalid bandwidth
        with self.assertRaises(ValueError):
            self.calc.calculate_point_a_arfcn('n77', 30, 150, 650000)
        
        # Invalid bandwidth for specific SCS
        with self.assertRaises(ValueError):
            self.calc.calculate_point_a_arfcn('n77', 60, 5, 650000)  # 5MHz not supported for 60kHz SCS
            
        # Invalid ARFCN to frequency conversion
        with self.assertRaises(ValueError):
            self.calc.arfcn_to_frequency('n999', 650000)


if __name__ == '__main__':
    # Run specific test
    unittest.main(verbosity=2)