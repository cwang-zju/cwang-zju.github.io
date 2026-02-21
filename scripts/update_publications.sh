#!/bin/bash

# Navigate to the project root directory
cd "$(dirname "$0")/.."

# Run the Ruby script
ruby scripts/process_publications.rb
