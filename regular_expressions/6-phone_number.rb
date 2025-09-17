#!/usr/bin/env ruby
# 6-phone_number.rb
# Usage: ./6-phone_number.rb "string"

puts ARGV[0].scan(/^\d{10}$/).join

