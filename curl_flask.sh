#!/bin/bash

response=$(curl -s http://localhost:8000/)
joke=$(echo "$response" | sed -n 's/.*Your daily chuck joke is: \(.*\)/\1/p')
word_count=$(echo "$joke" | wc -w)
echo "The joke has $word_count words."