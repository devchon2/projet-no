for file in *.py; do
    if [[ -s $file ]]; then
        echo "Copying content of $file to output.txt"
        echo "$file" >> output.txt
        cat "$file" | sed '/^\s*$/d' >> output.txt
        echo "Content of $file successfully copied to output.txt"
    else
        echo "Skipping $file (empty file)"
    fi
done
