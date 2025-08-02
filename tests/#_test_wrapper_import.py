#!/usr/bin/env python3
"""
Test script to verify that functions can be imported from wrapper
"""

def test_wrapper_import():
    """Test that functions can be imported from pkg_py.functions_split"""
    
    print("🧪 Testing wrapper import for functions...")
    
    try:
        # Import from wrapper
        from pkg_py.functions_split import ensure_window_title_replaced
        from pkg_py.functions_split import initialize_and_customize_logging_config
        
        print("✓ ensure_window_title_replaced imported successfully from wrapper")
        print(f"✓ Function: {ensure_window_title_replaced}")
        
        print("✓ initialize_and_customize_logging_config imported successfully from wrapper")
        print(f"✓ Function: {initialize_and_customize_logging_config}")
        
        # Test function execution (if it has default parameters)
        # ensure_window_title_replaced()
        # initialize_and_customize_logging_config()
        
        print("✅ Wrapper import test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Wrapper import test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_wrapper_import() 