#!/usr/bin/env ruby
# 8-textme.rb
# Usage: ./8-textme.rb "log_line"

log = ARGV[0]

# Use regex to extract sender, receiver, and flags
sender   = log[/\[from:([^\]]+)\]/, 1]
receiver = log[/\[to:([^\]]+)\]/, 1]
flags    = log[/\[flags:([^\]]+)\]/, 1]

puts "#{sender},#{receiver},#{flags}"

