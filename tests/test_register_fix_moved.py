#!/usr/bin/env python3
"""
Test script to debug register_pk_alias_windows function
"""
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from pkg_py.functions_split.ensure_pk_system_enabled import register_pk_alias_windows
    print("✅ Successfully imported register_pk_alias_windows")
    
    print("🔧 Calling register_pk_alias_windows...")
    register_pk_alias_windows()
    print("✅ register_pk_alias_windows completed")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()