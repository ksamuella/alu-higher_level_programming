#!/bin/bash
code=$(curl -s -o /tmp/curl_body_output_$$ -w "%{http_code}" "$1")
[ "$code" = "200" ] && cat /tmp/curl_body_output_$$ && rm -f /tmp/curl_body_output_$$
