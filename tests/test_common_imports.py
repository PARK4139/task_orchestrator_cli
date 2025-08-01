#!/usr/bin/env python3
"""
Test script to verify that common_imports.py works correctly with import *
"""

# Import all functions from common_imports using import *
from pkg_py.functions_split.common_imports import *

def test_common_imports():
    """Test that common_imports.py can be imported with * and functions work correctly"""
    
    print("🧪 Testing common_imports.py with import *...")
    
    try:
        print("✓ common_imports.py imported successfully with *")
        
        # Test that we can access functions directly
        print(f"✓ ensure_printed function: {ensure_printed}")
        print(f"✓ get_time_as_ function: {get_time_as_}")
        print(f"✓ ensure_spoken_hybrid function: {ensure_spoken_hybrid}")
        print(f"✓ ensure_console_cleared function: {ensure_console_cleared}")
        
        # Test function execution
        time_str = get_time_as_("now")
        print(f"✓ Function execution test: {time_str[:20]}...")
        
        # Test ensure_printed
        ensure_printed("✓ Import * test successful!", print_color="green")
        
        print("✅ All import * tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Import * test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_common_imports() 