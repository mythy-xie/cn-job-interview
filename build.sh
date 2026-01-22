#!/bin/bash

# Sphinx Build Helper Script
# Provides options for cleaning, building, and viewing documentation

echo "=========================================="
echo "Sphinx Documentation Build Helper"
echo "=========================================="
echo ""
echo "Select an option:"
echo "1) Clean build directory (rm -rf _build/)"
echo "2) Build documentation"
echo "3) Open in Firefox"
echo "4) Clean + Build"
echo "5) Clean + Build + Open"
echo "6) Exit"
echo ""
read -p "Enter your choice [1-6]: " choice

case $choice in
    1)
        echo "Cleaning build directory..."
        rm -rf _build/
        echo "✓ Build directory cleaned!"
        ;;
    2)
        echo "Building documentation..."
        sphinx-build -T -W --keep-going doc _build/html
        if [ $? -eq 0 ]; then
            echo "✓ Build successful!"
        else
            echo "✗ Build failed!"
        fi
        ;;
    3)
        echo "Opening in Firefox..."
        firefox _build/html/index.html &
        ;;
    4)
        echo "Cleaning build directory..."
        rm -rf _build/
        echo "✓ Build directory cleaned!"
        echo ""
        echo "Building documentation..."
        sphinx-build -T -W --keep-going doc _build/html
        if [ $? -eq 0 ]; then
            echo "✓ Build successful!"
        else
            echo "✗ Build failed!"
        fi
        ;;
    5)
        echo "Cleaning build directory..."
        rm -rf _build/
        echo "✓ Build directory cleaned!"
        echo ""
        echo "Building documentation..."
        sphinx-build -T -W --keep-going doc _build/html
        if [ $? -eq 0 ]; then
            echo "✓ Build successful!"
            echo ""
            echo "Opening in Firefox..."
            firefox _build/html/index.html &
        else
            echo "✗ Build failed!"
        fi
        ;;
    6)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid choice. Please enter a number between 1 and 6."
        ;;
esac