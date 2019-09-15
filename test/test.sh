code=$1
json=$2

curl -d @"$json" -H "Content-Type: application/json" -X POST http://localhost:9000/code/$code
