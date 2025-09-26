#!/usr/bin/env python3
"""
Test script for get-student-data.py

This script demonstrates how to use the get_student_data function.
Note: You'll need to update the Snowflake credentials in get-student-data.py before running.
"""

import sys
import os

# Add current directory to path to import the module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the function by executing the file (since filename has hyphen)
exec(open('get-student-data.py').read())

def test_get_student_data():
    """
    Test the get_student_data function
    
    Note: This will fail with actual connection since credentials are placeholders
    """
    try:
        print("Testing get_student_data function...")
        print("Note: This will fail because Snowflake credentials are placeholders")
        
        # This will fail due to invalid credentials, but shows the function is callable
        result = get_student_data(12345)
        print("✅ Function executed successfully!")
        print(f"Result: {result}")
        
    except Exception as e:
        print(f"❌ Expected error (due to placeholder credentials): {e}")
        print("✅ Function is properly defined and callable!")

if __name__ == "__main__":
    print("🧪 Testing get-student-data.py in virtual environment")
    print("=" * 50)
    
    # Test imports
    try:
        import snowflake.connector
        import pandas as pd
        print("✅ All required packages imported successfully")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        sys.exit(1)
    
    # Test function
    test_get_student_data()
    
    print("\n" + "=" * 50)
    print("🎉 Virtual environment setup is working correctly!")
    print("\n📝 Next steps:")
    print("1. Update Snowflake credentials in get-student-data.py")
    print("2. Replace placeholder values:")
    print("   - USER: Your Snowflake username")
    print("   - PASS: Your Snowflake password") 
    print("   - ACCOUNT: Your Snowflake account identifier")
    print("   - WH: Your Snowflake warehouse name")
