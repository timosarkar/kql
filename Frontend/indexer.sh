echo "[" > queries.json
first=true
# Recursively find all .kql files
find .. -type f -name "*.kql" | while read file; do
  filepath=${file#./}
  filepath_encoded=$(echo "$filepath" | sed 's/ /%20/g')
  name=$(basename "$file")
  if [ "$first" = true ]; then
    first=false
  else
    echo "," >> queries.json
  fi
  echo "{ \"name\": \"$name\", \"file\": \"$filepath_encoded\" }" >> queries.json
done
echo "]" >> queries.json

