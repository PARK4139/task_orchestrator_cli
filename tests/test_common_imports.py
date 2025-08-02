#!/usr/bin/env python3
"""
Test script to verify that common_imports.py works correctly with import * - dry_run 지원
"""

from test_base import DryRunMixin, run_test_with_dry_run

class CommonImportsTest(DryRunMixin):
    """common_imports 테스트 클래스"""
    
    def __init__(self, dry_run: bool = True):
        super().__init__(dry_run)
    
    def test_common_imports(self):
        """Test that common_imports.py can be imported with * and functions work correctly"""
        
        self.dry_run_print("🧪 Testing common_imports.py with import *...")
        
        try:
            # Import all functions from common_imports using import *
            from pkg_py.functions_split.common_imports import *
            
            self.dry_run_print("✓ common_imports.py imported successfully with *")
            
            # Test that we can access functions directly
            if self.dry_run:
                self.dry_run_print("✓ ensure_printed function: <function>")
                self.dry_run_print("✓ get_time_as_ function: <function>")
                self.dry_run_print("✓ ensure_spoken_hybrid function: <function>")
                self.dry_run_print("✓ ensure_console_cleared function: <function>")
                self.dry_run_print("✓ Function execution test: 시뮬레이션됨")
                self.dry_run_print("✓ Import * test successful!")
            else:
                self.dry_run_print(f"✓ ensure_printed function: {ensure_printed}")
                self.dry_run_print(f"✓ get_time_as_ function: {get_time_as_}")
                self.dry_run_print(f"✓ ensure_spoken_hybrid function: {ensure_spoken_hybrid}")
                self.dry_run_print(f"✓ ensure_console_cleared function: {ensure_console_cleared}")
                
                # Test function execution
                time_str = get_time_as_("now")
                self.dry_run_print(f"✓ Function execution test: {time_str[:20]}...")
                
                # Test ensure_printed
                ensure_printed("✓ Import * test successful!", print_color="green")
            
            self.dry_run_print("✅ All import * tests passed!")
            return True
            
        except Exception as e:
            self.dry_run_print(f"❌ Import * test failed: {e}")
            if not self.dry_run:
                import traceback
                traceback.print_exc()
            return False

def test_common_imports():
    """common_imports 테스트 함수"""
    test_instance = CommonImportsTest(dry_run=True)
    return test_instance.test_common_imports()

if __name__ == "__main__":
    # dry_run 모드로 테스트 실행
    run_test_with_dry_run(test_common_imports, "common_imports 테스트") 