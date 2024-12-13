#!/bin/bash

run_script() {
  script_name="$1"
  working_dir="$2"

  (
    cd "$working_dir" || exit 1
    ./$(basename "$script_name")
  )

  if [ $? -ne 0 ]; then
    echo "Error: $script_name failed"
    return 1
  fi

  echo "Success: $script_name completed"
  return 0
}

compile_all_scripts() {
  base_directory="$1"

  scripts=(
    "c/buildCLib.sh"
  )

  for script in "${scripts[@]}"; do
    script_dir="$base_directory/$(dirname "$script")"
    script_name=$(basename "$script")
    if [ -f "$script_dir/$script_name" ]; then
      echo "Running: $script"
      run_script "$script_name" "$script_dir" || exit 1
    else
      echo "Error: $script not found at $script_dir/$script_name"
    fi
  done
}

base_directory="$(pwd)/src/backend/sorts"
compile_all_scripts "$base_directory"
